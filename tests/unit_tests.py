import unittest
from your_module import generate_proposal


class TestProposalGenerator(unittest.TestCase):
    def test_generate_proposal(self):
        topic = ('''The Functional and Stylistic Peculiarities of Diminutives 
                    in the Russian and Czech Languages: A Corpus Study''')
        expected_output = '''The project proposal for the topic "The Functional and Stylistic Peculiarities of 
                            Diminutives in the Russian and Czech Languages: A Corpus Study" created successfully.'''

        result = generate_proposal(topic)
        self.assertEqual(result, expected_output)

    def test_invalid_topic(self):
        topic = ""
        expected_error_message = "The topic must be entered"

        with self.assertRaises(ValueError) as context:
            generate_proposal(topic)

        self.assertTrue(expected_error_message in str(context.exception))


if __name__ == '__main__':
    unittest.main()