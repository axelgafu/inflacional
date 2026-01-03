from datetime import date
from ..models.meeting import MeetingStatus

class TableGenerator:
    def __init__(self):
        self.headers = [
            "Fecha reunión",
            "Inflación subyacente anual (%)",
            "Inflación anual (INPC) (%)",
            "Meta de inflación vigente (% ± pp)",
            "Tasa de interés objetivo (%)",
            "Variación diaria FIX (MXN)"
        ]

    def generate_table(self, meetings_data):
        """
        Generates a Markdown table from the provided data.
        meetings_data is a list of dicts or objects containing values for each row.
        """
        table = "| " + " | ".join(self.headers) + " |\n"
        table += "| " + " | ".join(["---"] * len(self.headers)) + " |\n"
        
        for meeting in meetings_data:
            row = []
            row.append(str(meeting['date']))
            
            if meeting['status'] == MeetingStatus.FUTURE:
                # Fill with empty spaces for future meetings
                row.extend([""] * (len(self.headers) - 1))
            else:
                row.append(f"{meeting.get('core_inflation', ''):.2f}" if meeting.get('core_inflation') is not None else "")
                row.append(f"{meeting.get('annual_inflation', ''):.2f}" if meeting.get('annual_inflation') is not None else "")
                row.append(meeting.get('inflation_target', ""))
                row.append(f"{meeting.get('target_rate', ''):.2f}" if meeting.get('target_rate') is not None else "")
                row.append(f"{meeting.get('fix_variation', ''):.4f}" if meeting.get('fix_variation') is not None else "")
            
            table += "| " + " | ".join(row) + " |\n"
            
        return table
