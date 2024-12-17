import os
import json
import tempfile
import unittest
import shutil
from datetime import datetime

from logger import Logger


class TestLoggerInitialization(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.logger = Logger(log_dir=self.temp_dir)

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_create_log_directory(self):
        # Проверяем, что директория для логов создана
        self.assertTrue(os.path.isdir(self.temp_dir))

    def test_initialize_empty_log_file(self):
        # Проверяем, что файл логов создан и содержит пустой массив
        log_file = os.path.join(self.temp_dir, "generation_log.json")
        with open(log_file, "r", encoding="utf-8") as f:
            content = json.load(f)
        self.assertEqual(content, [])


class TestLoggerLogging(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.logger = Logger(log_dir=self.temp_dir)

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_add_new_entry_to_log(self):
        # Добавляем новую запись
        self.logger.log("Test Topic", "Test Proposal")

        # Читаем лог-файл и проверяем наличие новой записи
        log_file = os.path.join(self.temp_dir, "generation_log.json")
        with open(log_file, "r", encoding="utf-8") as f:
            logs = json.load(f)

        self.assertEqual(len(logs), 1)
        entry = logs[0]
        self.assertIn("topic", entry)
        self.assertIn("proposal", entry)
        self.assertIn("timestamp", entry)
        self.assertEqual(entry["topic"], "Test Topic")
        self.assertEqual(entry["proposal"], "Test Proposal")

    def test_multiple_entries_in_log(self):
        # Добавляем несколько записей
        self.logger.log("Topic 1", "Proposal 1")
        self.logger.log("Topic 2", "Proposal 2")

        # Читаем лог-файл и проверяем количество записей
        log_file = os.path.join(self.temp_dir, "generation_log.json")
        with open(log_file, "r", encoding="utf-8") as f:
            logs = json.load(f)

        self.assertEqual(len(logs), 2)
        first_entry = logs[0]
        second_entry = logs[1]
        self.assertEqual(first_entry["topic"], "Topic 1")
        self.assertEqual(second_entry["topic"], "Topic 2")


class TestLoggerReadingLogs(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.logger = Logger(log_dir=self.temp_dir)

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_read_existing_logs(self):
        # Добавляем две записи
        self.logger.log("Topic 1", "Proposal 1")
        self.logger.log("Topic 2", "Proposal 2")

        # Читаем лог-файл и проверяем количество записей
        log_file = os.path.join(self.temp_dir, "generation_log.json")
        with open(log_file, "r", encoding="utf-8") as f:
            logs = json.load(f)

        self.assertEqual(len(logs), 2)
        first_entry = logs[0]
        second_entry = logs[1]
        self.assertEqual(first_entry["topic"], "Topic 1")
        self.assertEqual(second_entry["topic"], "Topic 2")

    def test_read_empty_log_file(self):
        # Читаем пустой лог-файл
        log_file = os.path.join(self.temp_dir, "generation_log.json")
        with open(log_file, "r", encoding="utf-8") as f:
            logs = json.load(f)

        self.assertEqual(logs, [])

if __name__ == '__main__':
    unittest.main()
