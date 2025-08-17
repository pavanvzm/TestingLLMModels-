import unittest
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.log_analyzer import LogAnalyzer

class TestLogAnalyzer(unittest.TestCase):

    def setUp(self):
        self.test_log_file = "test_system.log"
        with open(self.test_log_file, 'w') as f:
            f.write("2023-10-27 10:00:00,INFO,User 'admin' logged in successfully.\n")
            f.write("2023-10-27 10:02:00,ERROR,Failed to connect to database.\n")
        self.log_analyzer = LogAnalyzer(self.test_log_file)

    def tearDown(self):
        os.remove(self.test_log_file)

    def test_analyze_logs(self):
        log_entries = self.log_analyzer.analyze_logs()
        self.assertEqual(len(log_entries), 2)
        self.assertEqual(log_entries[0]['level'], 'INFO')
        self.assertEqual(log_entries[1]['level'], 'ERROR')

if __name__ == '__main__':
    unittest.main()
