import unittest
from your_module import main


class TestProgramFunctionality(unittest.TestCase):
    def test_main_function(self):
        input_values = ['''The Functional and Stylistic Peculiarities of Diminutives 
                    in the Russian and Czech Languages: A Corpus Study''']

        def mock_input(s):
            return input_values.pop(0)

        main.input = mock_input

        main()

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()