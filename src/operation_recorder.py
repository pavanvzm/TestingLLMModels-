import datetime

class OperationRecorder:
    def __init__(self, record_file):
        self.record_file = record_file

    def record_operation(self, operation_details):
        """
        Records a system operation to the record file.
        """
        timestamp = datetime.datetime.now().isoformat()
        with open(self.record_file, 'a') as f:
            f.write(f"[{timestamp}] {operation_details}\n")
        print(f"Recorded operation: {operation_details}")
