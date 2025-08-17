class Reporting:
    def __init__(self, operation_recorder):
        self.operation_recorder = operation_recorder

    def generate_daily_report(self):
        """
        Generates a daily report of system operations.
        """
        # This would read the records from the OperationRecorder and summarize them.
        print("Generating daily report...")
        print("Daily report generated successfully.")
        return "Daily report."

    def generate_monthly_report(self):
        """
        Generates a monthly report of system operations.
        """
        print("Generating monthly report...")
        print("Monthly report generated successfully.")
        return "Monthly report."

    def generate_yearly_report(self):
        """
        Generates a yearly report of system operations.
        """
        print("Generating yearly report...")
        print("Yearly report generated successfully.")
        return "Yearly report."
