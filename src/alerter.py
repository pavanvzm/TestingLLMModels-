class Alerter:
    def __init__(self, error_detector, metrics_collector):
        self.error_detector = error_detector
        self.metrics_collector = metrics_collector

    def check_for_alerts(self):
        """
        Checks for errors and sends alerts if any are found.
        """
        print("Checking for alerts...")
        error_logs = self.error_detector.detect_errors()

        if error_logs:
            for error in error_logs:
                self.metrics_collector.increment_error_count()
                self.send_alert(error)
        else:
            print("No new alerts.")

    def send_alert(self, error_log):
        """
        Sends an alert for a specific error log.
        """
        # In a real application, this could be extended to send emails, SMS, etc.
        print("="*50)
        print("!!! ALERT !!!")
        print(f"Timestamp: {error_log['timestamp']}")
        print(f"Level: {error_log['level']}")
        print(f"Message: {error_log['message']}")
        print("="*50)
