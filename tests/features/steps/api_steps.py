from behave import given, when, then
import os
from banxico_report.utils.config import load_config

@given('un token de SIE válido')
def step_impl(context):
    os.environ['SIE_TOKEN'] = 'test_token'
    context.token = 'test_token'

@given('el año actual es 2026')
def step_impl(context):
    context.year = 2026

@when('ejecuto el generador de reportes')
def step_impl(context):
    from banxico_report.generator import ReportGenerator
    generator = ReportGenerator()
    context.report = generator.generate()

@then('debería ver una tabla Markdown con las fechas de las reuniones de 2026')
def step_impl(context):
    assert "| Fecha reunión |" in context.report
    assert "2026-02-12" in context.report

@then('las reuniones pasadas deben tener datos de inflación, tasa y variación FIX')
def step_impl(context):
    # Based on our mock data for 2026-01-01
    assert "5.05" in context.report # core
    assert "4.66" in context.report # annual
    assert "0.0500" in context.report # fix

@then('las reuniones futuras deben tener celdas vacías')
def step_impl(context):
    # Future meetings have empty cells after the date
    assert "2026-12-17 |  |  |  |  |  |" in context.report

@then('el reporte debe guardarse en un archivo con marca de tiempo')
def step_impl(context):
    from banxico_report.utils.persistence import save_report
    path = save_report(context.report)
    assert os.path.exists(path)
