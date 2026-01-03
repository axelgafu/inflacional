import click
from .generator import ReportGenerator
from .utils.persistence import save_report
from .utils.logger import setup_logger
from .utils.config import load_config

logger = setup_logger(__name__)

@click.group()
def cli():
    """Generador de reportes de inflación de Banxico."""
    load_config()

@cli.command()
def generate():
    """Genera un nuevo reporte de inflación."""
    try:
        generator = ReportGenerator()
        report_content = generator.generate()
        
        # Print to console
        click.echo(report_content)
        
        # Save to file
        file_path = save_report(report_content)
        click.echo(f"\nReporte guardado en: {file_path}")
        
    except Exception as e:
        logger.error(f"Error fatal: {e}")
        click.echo(f"Error: {e}", err=True)
        exit(1)

if __name__ == "__main__":
    cli()
