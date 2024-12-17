import os
import json


def load_examples(path):
    """Загружает примеры Project Proposal из папки."""
    examples = []
    for file_name in os.listdir(path):
        if file_name.endswith(".json"):
            with open(os.path.join(path, file_name), "r", encoding="utf-8") as f:
                examples.append(json.load(f))
    return examples
