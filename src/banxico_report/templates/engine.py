from string import Template

class RuleEngine:
    def __init__(self, templates):
        """
        templates: dict of string.Template objects or strings.
        """
        self.templates = {k: Template(v) if isinstance(v, str) else v for k, v in templates.items()}
        
    def render(self, template_name, data):
        """
        Renders a template with the provided data.
        """
        if template_name not in self.templates:
            raise ValueError(f"Template {template_name} not found.")
            
        return self.templates[template_name].safe_substitute(data)
