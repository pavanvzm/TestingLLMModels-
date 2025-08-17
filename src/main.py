from log_analyzer import LogAnalyzer
from error_detector import ErrorDetector
from operation_recorder import OperationRecorder
from reporting import Reporting
from alerter import Alerter
from security import Security

def main():
    """
    Main function to run the banking AI agent.
    """
    # Initialize all the components
    log_analyzer = LogAnalyzer("system.log")
    error_detector = ErrorDetector(log_analyzer)
    operation_recorder = OperationRecorder("operations.log")
    reporting = Reporting(operation_recorder)
    alerter = Alerter(error_detector)
    security = Security()

    # Simulate a user logging in
    username = "admin"
    password = "password123" # In a real app, this would be securely handled

    if security.authenticate_user(username, password):
        print(f"User {username} authenticated successfully.")
        security.two_factor_authentication(username)
        # Assume 2FA is successful for this simulation

        # Authorize the user for a specific action
        if security.authorize_user(username, "admin"):
            print(f"User {username} authorized for admin operations.")

            # Record an operation
            operation_recorder.record_operation("User 'admin' logged in.")

            # Analyze logs
            log_analyzer.analyze_logs()

            # Check for alerts
            alerter.check_for_alerts()

            # Generate a daily report
            reporting.generate_daily_report()
        else:
            print(f"User {username} is not authorized for this operation.")
    else:
        print("Authentication failed.")

if __name__ == "__main__":
    main()
