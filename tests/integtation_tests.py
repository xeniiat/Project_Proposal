import os
import unittest
from your_module import generate_and_save_proposal


class TestProposalIntegration(unittest.TestCase):
    def setUp(self):
        self.topic = '''The Functional and Stylistic Peculiarities of Diminutives 
                    in the Russian and Czech Languages: A Corpus Study'''
        self.filename = f"{self.topic.replace(' ', '_')}.txt"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_generate_and_save_proposal(self):
        generate_and_save_proposal(self.topic)

        self.assertTrue(os.path.exists(self.filename))
        with open(self.filename, 'r') as file:
            content = file.read()
            self.assertIn('''The Functional and Stylistic Peculiarities of Diminutives 
                    in the Russian and Czech Languages: A Corpus Study''', content)


if __name__ == '__main__':
    unittest.main()