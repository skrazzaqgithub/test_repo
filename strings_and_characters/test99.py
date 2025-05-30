import os
import json
from datetime import datetime
def extract_username():
    logs_failure_dir = "/var/log/failurelogs"
    os.makedirs('logs_failure_dir', exists_ok=True)
    def save_log(test_name):
        time_stamp = datetime.now().strftime("%Y-%M-%D_%h-%m-%s")
        log_filename = os.path.join('logs_failure_dir', f"{test_name}_{time_Stamp}.json")
        with open('log_filename', 'w') as logfile:
            json.dump({'request_info': request, 'response_info': response}, log_filename, indent=4)
            print(f"Failure logs are generated: {log_filename}")
        return logfile
    return save_log
    def occurrences_of_username('')