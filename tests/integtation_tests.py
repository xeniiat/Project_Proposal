import unittest
from io import StringIO
from unittest.mock import patch
from main import main


@patch('sys.stdout', new_callable=StringIO)
class TestMainFunction(unittest.TestCase):

    @patch('loader.load_examples')
    @patch('proposal_generator.ProposalGenerator.generate')
    @patch('logger.Logger.log')
    def test_main_function(self, mock_logger, mock_generation, mock_loader, mock_stdout):
        # Подготавливаем данные для тестов
        mock_loader.return_value = ["Example Content"]
        mock_generation.return_value = "Generated Proposal"

        # Запуск основной функции
        with patch('builtins.input', return_value="Test Topic") as mock_input:
            main()

        output = mock_stdout.getvalue().strip()
        expected_output = """Welcome to the Project Proposal Generator with GPT-2!
                            Enter the topic for your Project Proposal: 

                                Generated Project Proposal:
                                Generated Proposal"""

        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
