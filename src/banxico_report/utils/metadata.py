class MetadataTracker:
    def __init__(self):
        self.api_calls = []
        
    def record_call(self, url, method="GET", params=None):
        call = {
            "method": method,
            "url": url,
            "params": params
        }
        self.api_calls.append(call)
        
    def generate_metadata_section(self):
        section = "## Datos de Reproducibilidad\n\n"
        section += "Se utilizaron las siguientes llamadas a la API de Banxico SIE para obtener los datos:\n\n"
        for call in self.api_calls:
            section += f"- `{call['method']} {call['url']}`\n"
        return section
