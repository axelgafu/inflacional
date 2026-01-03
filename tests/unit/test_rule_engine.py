import pytest
from banxico_report.templates.engine import RuleEngine

def test_rule_engine_render():
    templates = {"test": "Hello ${name}!"}
    engine = RuleEngine(templates)
    result = engine.render("test", {"name": "World"})
    assert result == "Hello World!"

def test_rule_engine_missing_var():
    templates = {"test": "Hello ${name}!"}
    engine = RuleEngine(templates)
    # safe_substitute should not raise error for missing var
    result = engine.render("test", {})
    assert result == "Hello ${name}!"
