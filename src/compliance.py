# This file will contain the code for the compliance reporting features.
import json
from datetime import datetime

class AccessControlReporter:
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

    def generate_report(self):
        """Generates a report on access control events."""
        print("Generating access control report...")
        logs = self._get_operation_logs()

        access_events = [log for log in logs if log['operation_type'] in [
            'user_login', 'authentication_failure', '2fa_failure', 'authorization_failure'
        ]]

        today = datetime.now().date()
        report_content = f"Access Control Report for {today}\n"
        report_content += "="*30 + "\n"
        for event in access_events:
            report_content += f"[{event['timestamp']}] {event['operation_type']}: {event['details']}\n"

        report_filename = f"access_control_report_{today}.txt"
        with open(report_filename, 'w') as f:
            f.write(report_content)

        print(f"Access control report saved to {report_filename}")
        return report_filename

class SecurityConfigReporter:
    def __init__(self, security):
        self.security = security

    def generate_report(self):
        """Generates a report on the current security configuration."""
        print("Generating security configuration report...")

        roles = self.security.roles

        today = datetime.now().date()
        report_content = f"Security Configuration Report for {today}\n"
        report_content += "="*30 + "\n"
        for role, permissions in roles.items():
            report_content += f"Role: {role}\n"
            report_content += f"  Permissions: {', '.join(permissions)}\n"

        report_filename = f"security_config_report_{today}.txt"
        with open(report_filename, 'w') as f:
            f.write(report_content)

        print(f"Security configuration report saved to {report_filename}")
        return report_filename
