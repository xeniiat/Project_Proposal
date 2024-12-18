import unittest
import tempfile
import os
import json
import pytest
from loader import load_examples


# Проверяем, что функция правильно загружает JSON-файлы из указанной директории
class LoaderTests(unittest.TestCase):
    def test_load_examples_success(self):
        # Создаем временную директорию
        temp_dir = tempfile.mkdtemp()

        # Создаем два файла .json
        example_file1 = os.path.join(temp_dir, 'example1.json')
        example_file2 = os.path.join(temp_dir, 'example2.json')

        # Записываем данные в каждый файл
        with open(example_file1, 'w', encoding='utf-8') as f:
            json.dump({'key': 'value'}, f)

        with open(example_file2, 'w', encoding='utf-8') as f:
            json.dump({'another_key': 'another_value'}, f)

        # Загружаем примеры
        examples = load_examples(temp_dir)

        assert len(examples) == 2
        assert {'key': 'value'} in examples
        assert {'another_key': 'another_value'} in examples

# Проверяем, что функция возвращает пустой список, если в директории нет файлов .json
    def test_load_examples_no_json_files(self):
        # Создаем временную директорию без файлов
        temp_dir = tempfile.mkdtemp()

        # Загружаем примеры
        examples = load_examples(temp_dir)

        assert len(examples) == 0

# Проверяем, что функция корректно обрабатывает ситуацию, когда переданный путь не существует
    def test_load_examples_invalid_path(self):
        # Передаем несуществующий путь
        invalid_path = '/nonexistent/path'

        with pytest.raises(FileNotFoundError):
            load_examples(invalid_path)

# Проверяем, что функция игнорирует файлы, которые не имеют расширение .json
    def test_load_examples_ignore_non_json_files(self):
        # Создаем временную директорию
        temp_dir = tempfile.mkdtemp()

        # Создаем два файла: один .json, другой .txt
        example_file1 = os.path.join(temp_dir, 'example1.json')
        non_json_file = os.path.join(temp_dir, 'not_example.txt')

        # Записываем данные в каждый файл
        with open(example_file1, 'w', encoding='utf-8') as f:
            json.dump({'key': 'value'}, f)

        with open(non_json_file, 'w'):
            pass

        # Загружаем примеры
        examples = load_examples(temp_dir)

        assert len(examples) == 1
        assert {'key': 'value'} in examples


if __name__ == '__main__':
    unittest.main()
