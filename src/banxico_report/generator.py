from datetime import date
from .parsers.calendar import CalendarParser
from .parsers.inflation import InflationParser
from .parsers.target import TargetFetcher
from .api.rates import RatesFetcher
from .api.exchange import ExchangeRateFetcher
from .api.factory import SIEProviderFactory
from .generators.table import TableGenerator
from .generators.references import APAFormatter
from .templates.engine import RuleEngine
from .templates.insights_es import INSIGHTS_TEMPLATES
from .utils.config import get_token
from .utils.logger import setup_logger
from .utils.metadata import MetadataTracker
from .models.meeting import MeetingStatus

logger = setup_logger(__name__)

class ReportGenerator:
    def __init__(self):
        token = get_token()
        self.metadata_tracker = MetadataTracker()
        self.sie_provider = SIEProviderFactory.get_provider(token)
        
        if hasattr(self.sie_provider, 'client'):
             # If it's the real provider, we might want to attach the tracker
             # This is a bit of a leak but okay for now to maintain telemetry
             self.sie_provider.client.tracker = self.metadata_tracker

        self.calendar_parser = CalendarParser()
        self.inflation_parser = InflationParser()
        self.target_fetcher = TargetFetcher()
        self.rates_fetcher = RatesFetcher(self.sie_provider)
        self.exchange_fetcher = ExchangeRateFetcher(self.sie_provider)
        
        self.table_generator = TableGenerator()
        self.apa_formatter = APAFormatter()
        self.rule_engine = RuleEngine(INSIGHTS_TEMPLATES)

    def generate(self):
        """
        Orchestrates the report generation.
        """
        logger.info("Starting complete report generation process")
        
        meetings = self.calendar_parser.get_meetings()
        meetings_data = []
        latest_past_meeting = None
        
        for m in meetings:
            data = {
                'date': m.date,
                'status': m.status
            }
            
            if m.status == MeetingStatus.PAST:
                # Fetch data for past meetings
                inflation = self.inflation_parser.get_latest_inflation(m.date)
                data['core_inflation'] = inflation.core_inflation
                data['annual_inflation'] = inflation.annual_inflation
                data['inflation_target'] = self.target_fetcher.get_inflation_target()
                data['target_rate'] = self.rates_fetcher.get_target_rate(m.date)
                data['fix_variation'] = self.exchange_fetcher.get_fix_variation(m.date)
                
                # Add references
                self.apa_formatter.add_banxico_sie("TI52", "Tasa objetivo", m.date.year)
                self.apa_formatter.add_banxico_sie("SF43718", "Tipo de cambio FIX", m.date.year)
                self.apa_formatter.add_inegi_inpc(inflation.source_url, m.date.year)
                
                latest_past_meeting = data
            
            meetings_data.append(data)
            
        # 1. Title
        report = f"# Reporte de Inflación Banxico {self.calendar_parser.year}\n\n"
        
        # 2. Table
        report += self.table_generator.generate_table(meetings_data)
        report += "\n"
        
        # 3. Analytical Insights
        if latest_past_meeting:
            report += "## Análisis de Coyuntura\n\n"
            insights_data = {
                "year": self.calendar_parser.year,
                "latest_date": latest_past_meeting['date'],
                "inflation_annual": latest_past_meeting['annual_inflation'],
                "inflation_core": latest_past_meeting['core_inflation'],
                "inflation_target": latest_past_meeting['inflation_target'],
                "target_rate": latest_past_meeting['target_rate'],
                "fix_variation": latest_past_meeting['fix_variation']
            }
            
            report += self.rule_engine.render("intro", insights_data) + "\n\n"
            report += self.rule_engine.render("inflation_analysis", insights_data) + "\n\n"
            report += self.rule_engine.render("market_context", insights_data) + "\n\n"
            
        # 4. Technical Metadata
        report += self.metadata_tracker.generate_metadata_section()
        report += "\n"
        
        # 5. References
        report += self.apa_formatter.generate_references_section()
        
        return report
