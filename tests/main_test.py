import unittest
from unittest.mock import patch
from loader import load_examples
from proposal_generator import ProposalGenerator
from logger import Logger


class TestLoader(unittest.TestCase):
    @patch('loader.os.listdir')
    def test_load_examples(self, mock_listdir):
        # Настраиваем список файлов для имитации содержимого папки
        mock_listdir.return_value = ['example1.txt', 'example2.txt']

        # Имитация чтения файла
        with patch('builtins.open') as mock_open:
            mock_file = mock_open.return_value.__enter__.return_value
            mock_file.read.side_effect = ["Example content 1", "Example content 2"]

            examples = load_examples("examples")
            self.assertEqual(len(examples), 2)
            self.assertIn("Example content 1", examples)
            self.assertIn("Example content 2", examples)


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
