import pytest
from banxico_report.generators.references import APAFormatter

def test_apa_banxico_sie():
    formatter = APAFormatter()
    formatter.add_banxico_sie("TI52", "Tasa objetivo", 2026)
    ref = formatter.references[0]
    assert "Banco de México. (2026)" in ref
    assert "Serie TI52: Tasa objetivo" in ref
    assert "Recuperado de" in ref

def test_apa_inegi_inpc():
    formatter = APAFormatter()
    formatter.add_inegi_inpc("http://test.com", 2026)
    ref = formatter.references[0]
    assert "INEGI. (2026)" in ref
    assert "Recuperado de http://test.com" in ref
