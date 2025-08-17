# This file will contain the code for the monitoring features.

class MetricsCollector:
    def __init__(self):
        self.metrics = {
            "operation_count": 0,
            "error_count": 0,
        }

    def increment_operation_count(self):
        """Increments the operation count."""
        self.metrics["operation_count"] += 1

    def increment_error_count(self):
        """Increments the error count."""
        self.metrics["error_count"] += 1

    def get_metrics(self):
        """Returns the current metrics."""
        return self.metrics

class HealthChecker:
    def check_system_health(self):
        """
        Checks the health of the system.
        In a real application, this would check database connections, disk space, etc.
        """
        # For now, we'll just return a dummy status.
        return {
            "database_connection": "OK",
            "disk_space": "OK"
        }

class Dashboard:
    def __init__(self, metrics_collector, health_checker):
        self.metrics_collector = metrics_collector
        self.health_checker = health_checker

    def display(self):
        """Displays the monitoring dashboard."""
        metrics = self.metrics_collector.get_metrics()
        health_status = self.health_checker.check_system_health()

        print("="*50)
        print("Monitoring Dashboard")
        print("="*50)
        print("\n--- Metrics ---")
        for key, value in metrics.items():
            print(f"{key}: {value}")

        print("\n--- System Health ---")
        for key, value in health_status.items():
            print(f"{key}: {value}")

        print("\n" + "="*50)
