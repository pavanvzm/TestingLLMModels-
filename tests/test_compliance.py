import unittest
from unittest.mock import Mock, patch
import sys
import os
from datetime import datetime

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.compliance import AccessControlReporter, SecurityConfigReporter

class TestCompliance(unittest.TestCase):

    @patch('src.compliance.datetime')
    def test_access_control_reporter(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 10, 27)
        mock_operation_recorder = Mock()

        with patch('builtins.open', unittest.mock.mock_open()) as mock_file:
            with patch.object(AccessControlReporter, '_get_operation_logs', return_value=[
                {"timestamp": "2023-10-27T10:00:00", "operation_type": "user_login", "details": {"user": "admin"}}
            ]):
                reporter = AccessControlReporter(mock_operation_recorder)
                report_filename = reporter.generate_report()
                self.assertEqual(report_filename, "access_control_report_2023-10-27.txt")
                mock_file.assert_called_with("access_control_report_2023-10-27.txt", 'w')

    @patch('src.compliance.datetime')
    def test_security_config_reporter(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 10, 27)
        mock_security = Mock()
        mock_security.roles = {"admin": ["all"], "analyst": ["read"]}

        with patch('builtins.open', unittest.mock.mock_open()) as mock_file:
            reporter = SecurityConfigReporter(mock_security)
            report_filename = reporter.generate_report()
            self.assertEqual(report_filename, "security_config_report_2023-10-27.txt")
            mock_file.assert_called_with("security_config_report_2023-10-27.txt", 'w')

if __name__ == '__main__':
    unittest.main()
