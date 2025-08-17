import datetime
import json

class OperationRecorder:
    def __init__(self, record_file):
        self.record_file = record_file

    def record_operation(self, operation_type, details):
        """
        Records a system operation to the record file in JSON format.
        """
        timestamp = datetime.datetime.now().isoformat()

        record = {
            "timestamp": timestamp,
            "operation_type": operation_type,
            "details": details
        }

        with open(self.record_file, 'a') as f:
            f.write(json.dumps(record) + '\n')

        print(f"Recorded operation: {operation_type}")
