import json
import datetime

LOG_FILE_TXT = "logs/firewall.log"
LOG_FILE_JSON = "logs/firewall.json"

def log_event(event):
    timestamp = str(datetime.datetime.now())

    # Append to plain text log
    with open(LOG_FILE_TXT, "a") as file:
        file.write(f"{timestamp} - {event}\n")

    # Append to JSON log
    try:
        with open(LOG_FILE_JSON, "r") as file:
            logs = json.load(file)
    except:
        logs = []

    logs.append({"timestamp": timestamp, "event": event})

    with open(LOG_FILE_JSON, "w") as file:
        json.dump(logs, file, indent=4)
