class Alerter:
    def __init__(self, error_detector):
        self.error_detector = error_detector

    def check_for_alerts(self):
        """
        Checks for errors and sends alerts if any are found.
        """
        # This would use the ErrorDetector to check for issues and then
        # trigger alerts through email, SMS, or another notification system.
        print("Checking for alerts...")
        # Simulate checking for errors
        errors = self.error_detector.detect_errors()
        if errors != "No errors detected.":
            self.send_alert(errors)
        else:
            print("No new alerts.")

    def send_alert(self, error_message):
        """
        Sends an alert.
        """
        print(f"ALERT: An error has occurred: {error_message}")
