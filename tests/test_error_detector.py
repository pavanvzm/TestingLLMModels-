import unittest
from unittest.mock import Mock
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.error_detector import ErrorDetector

class TestErrorDetector(unittest.TestCase):

    def test_detect_errors(self):
        mock_log_analyzer = Mock()
        mock_log_analyzer.analyze_logs.return_value = [
            {"timestamp": "2023-10-27 10:00:00", "level": "INFO", "message": "Info message"},
            {"timestamp": "2023-10-27 10:02:00", "level": "ERROR", "message": "Error message"},
        ]
        error_detector = ErrorDetector(mock_log_analyzer)
        error_logs = error_detector.detect_errors()
        self.assertEqual(len(error_logs), 1)
        self.assertEqual(error_logs[0]['level'], 'ERROR')

if __name__ == '__main__':
    unittest.main()
