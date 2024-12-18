import unittest
from unittest.mock import patch
from Project_Proposal.loader import load_examples
from Project_Proposal.proposal_generator import ProposalGenerator
from Project_Proposal.logger import Logger
import json


class TestLoader(unittest.TestCase):
    @patch('loader.os.listdir')
    def test_load_examples(self, mock_listdir):
        # Настраиваем список файлов для имитации содержимого папки
        mock_listdir.return_value = ['example1.json', 'example2.json']

        # Имитация чтения файла
        mock_json_data = [
            {"key1": "value1"},
            {"key2": "value2"}
        ]
        with patch('builtins.open', create=True) as mock_open:
            mock_file = mock_open.return_value.__enter__.return_value
            mock_file.read.side_effect = [json.dumps(mock_json_data[0]), json.dumps(mock_json_data[1])]

            # Тестируем функцию
            examples = load_examples("dummy_path")

            # Проверяем, что функция вернула правильные данные
            self.assertEqual(len(examples), 2)
            self.assertIn(mock_json_data[0], examples)
            self.assertIn(mock_json_data[1], examples)


class TestProposalGenerator(unittest.TestCase):

    @patch('proposal_generator.ProposalGenerator.generate')
    def test_generate_proposal(self, mock_generate):
        # Устанавливаем возвращаемое значение для generate
        mock_generate.return_value = "This is a generated proposal."

        generator = ProposalGenerator()
        proposal = generator.generate("Test Topic", [])
        self.assertEqual(proposal, "This is a generated proposal.")


class TestLogger(unittest.TestCase):

    @patch('logger.Logger.log')
    def test_log(self, mock_log):
        logger = Logger()
        logger.log("Test Topic", "Test Proposal")
        mock_log.assert_called_once_with("Test Topic", "Test Proposal")


if __name__ == '__main__':
    unittest.main()
