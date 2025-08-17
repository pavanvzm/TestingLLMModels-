import re

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file

    def analyze_logs(self):
        """
        Analyzes the system logs to identify relevant events and patterns.
        Returns a list of log entries.
        """
        print(f"Analyzing logs from {self.log_file}...")
        log_entries = []
        try:
            with open(self.log_file, 'r') as f:
                for line in f:
                    match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),(\w+),(.*)", line)
                    if match:
                        log_entries.append({
                            "timestamp": match.group(1),
                            "level": match.group(2),
                            "message": match.group(3).strip()
                        })
        except FileNotFoundError:
            print(f"Error: Log file not found at {self.log_file}")

        print(f"Successfully parsed {len(log_entries)} log entries.")
        return log_entries
