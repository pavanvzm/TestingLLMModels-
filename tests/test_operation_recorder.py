import unittest
import sys
import os
import json

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.operation_recorder import OperationRecorder

class TestOperationRecorder(unittest.TestCase):

    def setUp(self):
        self.test_record_file = "test_operations.log"
        self.operation_recorder = OperationRecorder(self.test_record_file)

    def tearDown(self):
        if os.path.exists(self.test_record_file):
            os.remove(self.test_record_file)

    def test_record_operation(self):
        self.operation_recorder.record_operation("test_op", {"data": "test_data"})
        with open(self.test_record_file, 'r') as f:
            line = f.readline()
            record = json.loads(line)
            self.assertEqual(record['operation_type'], 'test_op')
            self.assertEqual(record['details']['data'], 'test_data')

if __name__ == '__main__':
    unittest.main()
