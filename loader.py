import json
import os


def load_examples(path):
    """Loading examples from JSON-files."""
    examples = []
    for file_name in os.listdir(path):
        if file_name.endswith(".json"):
            with open(os.path.join(path, file_name), "r",
                      encoding="utf-8") as f:
                examples.append(json.load(f))
    return examples
