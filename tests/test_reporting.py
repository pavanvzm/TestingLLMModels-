import unittest
from unittest.mock import Mock, patch
import sys
import os
from datetime import datetime

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.reporting import Reporting

class TestReporting(unittest.TestCase):

    def setUp(self):
        self.mock_operation_recorder = Mock()
        self.mock_operation_recorder.record_file = "test_operations.log"
        self.reporting = Reporting(self.mock_operation_recorder)

    @patch('src.reporting.datetime')
    def test_generate_daily_report(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 10, 27)
        with patch('builtins.open', unittest.mock.mock_open()) as mock_file:
            with patch.object(self.reporting, '_get_operation_logs', return_value=[
                {"timestamp": "2023-10-27T10:00:00", "operation_type": "login", "details": {"user": "admin"}}
            ]):
                report_filename = self.reporting.generate_daily_report()
                self.assertEqual(report_filename, "daily_report_2023-10-27.txt")
                mock_file.assert_called_with("daily_report_2023-10-27.txt", 'w')

if __name__ == '__main__':
    unittest.main()
