class ErrorDetector:
    def __init__(self, log_analyzer):
        self.log_analyzer = log_analyzer

    def detect_errors(self):
        """
        Detects errors in the system logs.
        Returns a list of error log entries.
        """
        print("Detecting errors in system logs...")
        log_entries = self.log_analyzer.analyze_logs()

        error_logs = [entry for entry in log_entries if entry['level'] == 'ERROR']

        if error_logs:
            print(f"Found {len(error_logs)} errors.")
        else:
            print("No errors detected.")

        return error_logs
