import json
import os
from datetime import datetime


class Logger:
    def __init__(self, log_file="logs.json"):
        self.log_file = log_file
        if not os.path.exists(log_file):
            with open(log_file, "w", encoding="utf-8") as f:
                json.dump([], f)

    def log(self, topic, proposal):
        """Добавляет запись в лог."""
        with open(self.log_file, "r", encoding="utf-8") as f:
            logs = json.load(f)

        logs.append({
            "topic": topic,
            "proposal": proposal,
            "timestamp": datetime.now().isoformat()
        })

        with open(self.log_file, "w", encoding="utf-8") as f:
            json.dump(logs, f, ensure_ascii=False, indent=4)
