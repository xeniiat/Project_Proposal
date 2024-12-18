import unittest
from unittest.mock import patch, MagicMock
import os
import json
from datetime import datetime
from logger import Logger

class TestLogger(unittest.TestCase):
    def setUp(self):
        self.log_file = "test_logs.json"
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def tearDown(self):
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_create_new_log_file_if_not_exists(self):
        logger = Logger(self.log_file)
        self.assertTrue(os.path.exists(self.log_file))
        with open(self.log_file, "r", encoding="utf-8") as f:
            logs = json.load(f)
        self.assertListEqual(logs, [])

    def test_add_entry_to_existing_log_file(self):
        with open(self.log_file, "w", encoding="utf-8") as f:
            json.dump([{"topic": "Existing Topic", "proposal": "Existing Proposal", "timestamp": "2023-01-01T00:00:00"}], f)

        logger = Logger(self.log_file)
        logger.log("New Topic", "New Proposal")

        with open(self.log_file, "r", encoding="utf-8") as f:
            logs = json.load(f)

        self.assertEqual(len(logs), 2)
        self.assertDictEqual(
            logs[-1],
            {
                "topic": "New Topic",
                "proposal": "New Proposal",
                "timestamp": logs[-1]["timestamp"]  # Проверяем только наличие ключа timestamp
            }
        )

    @patch('logger.datetime')
    def test_timestamp_formatting(self, mock_datetime):
        now = datetime(2023, 1, 1, 12, 34, 56)
        mock_datetime.now.return_value = now

        logger = Logger(self.log_file)
        logger.log("Topic", "Proposal")

        with open(self.log_file, "r", encoding="utf-8") as f:
            logs = json.load(f)

        self.assertEqual(len(logs), 1)
        self.assertDictEqual(
            logs[0],
            {
                "topic": "Topic",
                "proposal": "Proposal",
                "timestamp": "2023-01-01T12:34:56"
            }
        )

    def test_logging_multiple_entries(self):
        logger = Logger(self.log_file)
        topics = ["Topic1", "Topic2", "Topic3"]
        proposals = ["Proposal1", "Proposal2", "Proposal3"]

        for topic, proposal in zip(topics, proposals):
            logger.log(topic, proposal)

        with open(self.log_file, "r", encoding="utf-8") as f:
            logs = json.load(f)

        self.assertEqual(len(logs), len(topics))
        for i, entry in enumerate(logs):
            self.assertDictEqual(
                entry,
                {
                    "topic": topics[i],
                    "proposal": proposals[i],
                    "timestamp": entry["timestamp"]  # Проверяем только наличие ключа timestamp
                }
            )

if __name__ == '__main__':
    unittest.main()