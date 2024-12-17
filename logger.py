import os
import json
from datetime import datetime

class Logger:
    def __init__(self, log_dir="logs"):
        self.log_file = os.path.join(log_dir, "generation_log.json")
        os.makedirs(log_dir, exist_ok=True)

        # Если файла нет, создаем его
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w", encoding="utf-8") as f:
                json.dump([], f)

    def log(self, topic, proposal):
        """Сохраняет информацию о сгенерированном Project Proposal."""
        with open(self.log_file, "r", encoding="utf-8") as f:
            logs = json.load(f)

        logs.append({
            "topic": topic,
            "proposal": proposal,
            "timestamp": datetime.now().isoformat()
        })

        with open(self.log_file, "w", encoding="utf-8") as f:
            json.dump(logs, f, ensure_ascii=False, indent=4)
