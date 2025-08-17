import unittest
from unittest.mock import Mock, patch
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.monitoring import MetricsCollector, HealthChecker, Dashboard

class TestMonitoring(unittest.TestCase):

    def test_metrics_collector(self):
        collector = MetricsCollector()
        self.assertEqual(collector.get_metrics()["operation_count"], 0)
        collector.increment_operation_count()
        self.assertEqual(collector.get_metrics()["operation_count"], 1)

        self.assertEqual(collector.get_metrics()["error_count"], 0)
        collector.increment_error_count()
        self.assertEqual(collector.get_metrics()["error_count"], 1)

    def test_health_checker(self):
        checker = HealthChecker()
        health = checker.check_system_health()
        self.assertEqual(health["database_connection"], "OK")
        self.assertEqual(health["disk_space"], "OK")

    @patch('builtins.print')
    def test_dashboard(self, mock_print):
        mock_metrics_collector = Mock()
        mock_metrics_collector.get_metrics.return_value = {"ops": 10, "err": 1}

        mock_health_checker = Mock()
        mock_health_checker.check_system_health.return_value = {"db": "OK"}

        dashboard = Dashboard(mock_metrics_collector, mock_health_checker)
        dashboard.display()

        # Check if the print function was called with the expected output
        self.assertIn("Monitoring Dashboard", mock_print.call_args_list[1][0][0])
        self.assertIn("ops: 10", mock_print.call_args_list[4][0][0])
        self.assertIn("err: 1", mock_print.call_args_list[5][0][0])
        self.assertIn("db: OK", mock_print.call_args_list[7][0][0])

if __name__ == '__main__':
    unittest.main()
