import argparse
from log_analyzer import LogAnalyzer
from error_detector import ErrorDetector
from operation_recorder import OperationRecorder
from reporting import Reporting
from alerter import Alerter
from security import Security
from monitoring import MetricsCollector, HealthChecker, Dashboard
from compliance import AccessControlReporter, SecurityConfigReporter

def run_simulation(security, log_analyzer, error_detector, operation_recorder, reporting, alerter, metrics_collector):
    """Runs the full agent simulation."""
    username = "admin"
    password = "password123"

    if security.authenticate_user(username, password):
        print(f"User {username} authenticated successfully.")

        code = security.two_factor_authentication(username)
        user_code_input = "123456"

        if security.verify_2fa_code(username, user_code_input):
            print("2FA verification successful.")
            if security.authorize_user(username, "all"):
                print(f"User {username} authorized for admin operations.")
                operation_recorder.record_operation("user_login", {"username": username, "status": "success"})
                metrics_collector.increment_operation_count()

                log_analyzer.analyze_logs()
                alerter.check_for_alerts()
                reporting.generate_daily_report()
            else:
                operation_recorder.record_operation("authorization_failure", {"username": username, "required_permission": "all"})
                metrics_collector.increment_operation_count()
                print(f"User {username} is not authorized for this operation.")
        else:
            operation_recorder.record_operation("2fa_failure", {"username": username})
            metrics_collector.increment_operation_count()
            print("2FA verification failed.")
    else:
        operation_recorder.record_operation("authentication_failure", {"username": username})
        metrics_collector.increment_operation_count()
        print("Authentication failed.")

def main():
    """
    Main function to run the banking AI agent.
    """
    parser = argparse.ArgumentParser(description="Banking AI Agent")
    parser.add_argument("--daily-report", action="store_true", help="Generate a daily report.")
    parser.add_argument("--monthly-report", action="store_true", help="Generate a monthly report.")
    parser.add_argument("--yearly-report", action="store_true", help="Generate a yearly report.")
    parser.add_argument("--dashboard", action="store_true", help="Display the monitoring dashboard.")
    parser.add_argument("--access-report", action="store_true", help="Generate an access control report.")
    parser.add_argument("--security-config-report", action="store_true", help="Generate a security configuration report.")
    args = parser.parse_args()

    # Initialize all the components
    log_analyzer = LogAnalyzer("system.log")
    operation_recorder = OperationRecorder("operations.log")
    metrics_collector = MetricsCollector()
    reporting = Reporting(operation_recorder)
    error_detector = ErrorDetector(log_analyzer)
    alerter = Alerter(error_detector, metrics_collector)
    security = Security()
    health_checker = HealthChecker()
    dashboard = Dashboard(metrics_collector, health_checker)
    access_reporter = AccessControlReporter(operation_recorder)
    security_config_reporter = SecurityConfigReporter(security)

    if args.daily_report:
        reporting.generate_daily_report()
    elif args.monthly_report:
        reporting.generate_monthly_report()
    elif args.yearly_report:
        reporting.generate_yearly_report()
    elif args.dashboard:
        dashboard.display()
    elif args.access_report:
        access_reporter.generate_report()
    elif args.security_config_report:
        security_config_reporter.generate_report()
    else:
        run_simulation(security, log_analyzer, error_detector, operation_recorder, reporting, alerter, metrics_collector)

if __name__ == "__main__":
    main()
