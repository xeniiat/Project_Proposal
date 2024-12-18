import pytest
from unittest.mock import patch
from proposal_generator import ProposalGenerator
# from config import MODEL_NAME, MAX_TOKENS, TEMPERATURE, TOP_P, OUTPUT_DIR


@pytest.fixture(scope='module')
def generator():
    return ProposalGenerator()


@patch('transformers.GPT2LMHeadModel.from_pretrained', autospec=True)
@patch('transformers.GPT2Tokenizer.from_pretrained', autospec=True)
def test_generate(mock_model, mock_tokenizer, generator):
    topic = "Climate Change"
    examples = []
    min_words = 50

    mock_model.return_value.generate.return_value = [generator.tokenizer.encode("Generated text")]
    mock_tokenizer.return_value.decode.return_value = "Generated text"

    generated_text = generator.generate(topic, examples, min_words=min_words)

    assert isinstance(generated_text, str)
    assert len(generated_text.split()) >= min_words


def test_save_proposal(generator, tmpdir):
    topic = "Test Topic"
    proposal = "This is a test proposal."

    generator.save_proposal(topic, proposal)

    saved_file = tmpdir.join(f'{topic.replace(" ", "_")}_proposal.txt')
    assert saved_file.read() == proposal
    