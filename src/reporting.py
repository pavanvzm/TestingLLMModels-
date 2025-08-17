import json
from datetime import datetime, timedelta

class Reporting:
    def __init__(self, operation_recorder):
        self.operation_recorder = operation_recorder
        self.record_file = self.operation_recorder.record_file

    def _get_operation_logs(self):
        """Reads and parses the operation logs from the record file."""
        logs = []
        try:
            with open(self.record_file, 'r') as f:
                for line in f:
                    logs.append(json.loads(line))
        except FileNotFoundError:
            print(f"Record file not found at {self.record_file}")
        return logs

    def generate_daily_report(self):
        """Generates a daily report of system operations."""
        print("Generating daily report...")
        logs = self._get_operation_logs()

        today = datetime.now().date()
        daily_logs = [log for log in logs if datetime.fromisoformat(log['timestamp']).date() == today]

        report_content = f"Daily Report for {today}\n"
        report_content += "="*30 + "\n"
        for log in daily_logs:
            report_content += f"[{log['timestamp']}] {log['operation_type']}: {log['details']}\n"

        report_filename = f"daily_report_{today}.txt"
        with open(report_filename, 'w') as f:
            f.write(report_content)

        print(f"Daily report saved to {report_filename}")
        return report_filename

    def generate_monthly_report(self):
        """Generates a monthly report of system operations."""
        print("Generating monthly report...")
        logs = self._get_operation_logs()

        current_month = datetime.now().month
        monthly_logs = [log for log in logs if datetime.fromisoformat(log['timestamp']).month == current_month]

        report_content = f"Monthly Report for Month {current_month}\n"
        report_content += "="*30 + "\n"
        for log in monthly_logs:
            report_content += f"[{log['timestamp']}] {log['operation_type']}: {log['details']}\n"

        report_filename = f"monthly_report_{datetime.now().year}-{current_month}.txt"
        with open(report_filename, 'w') as f:
            f.write(report_content)

        print(f"Monthly report saved to {report_filename}")
        return report_filename

    def generate_yearly_report(self):
        """Generates a yearly report of system operations."""
        print("Generating yearly report...")
        logs = self._get_operation_logs()

        current_year = datetime.now().year
        yearly_logs = [log for log in logs if datetime.fromisoformat(log['timestamp']).year == current_year]

        report_content = f"Yearly Report for {current_year}\n"
        report_content += "="*30 + "\n"
        for log in yearly_logs:
            report_content += f"[{log['timestamp']}] {log['operation_type']}: {log['details']}\n"

        report_filename = f"yearly_report_{current_year}.txt"
        with open(report_filename, 'w') as f:
            f.write(report_content)

        print(f"Yearly report saved to {report_filename}")
        return report_filename
