class APAFormatter:
    def __init__(self):
        self.references = []
        
    def add_banxico_sie(self, serie_id, serie_name, year=2026):
        ref = f"Banco de México. ({year}). Sistema de Información Económica. Serie {serie_id}: {serie_name}. Recuperado de https://www.banxico.org.mx/SieAPIRest/service/swagger-ui.html#/Series"
        if ref not in self.references:
            self.references.append(ref)
            
    def add_inegi_inpc(self, bulletin_url, year=2026):
        ref = f"INEGI. ({year}). Índice Nacional de Precios al Consumidor (INPC). Boletín de prensa. Recuperado de {bulletin_url}"
        if ref not in self.references:
            self.references.append(ref)
            
    def add_banxico_calendar(self, calendar_url, year=2026):
        ref = f"Banco de México. ({year}). Calendario de decisiones de política monetaria. Recuperado de {calendar_url}"
        if ref not in self.references:
            self.references.append(ref)

    def generate_references_section(self):
        section = "## Referencias\n\n"
        for ref in sorted(self.references):
            section += f"- {ref}\n"
        return section
