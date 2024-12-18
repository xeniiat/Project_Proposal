from loader import load_examples
from proposal_generator import ProposalGenerator
from logger import Logger


def main():
    print("Welcome to the Project Proposal Generator with GPT-2!")

    examples_path = "examples"
    examples = load_examples(examples_path)
    if not examples:
        print("No examples found. Please add files to the 'examples' folder.")
        return

    topic = input("Enter the topic for your Project Proposal: ")

    generator = ProposalGenerator()
    proposal = generator.generate(topic, examples)

    logger = Logger()
    logger.log(topic, proposal)

    print("\nGenerated Project Proposal:\n")
    print(proposal)


if __name__ == "__main__":
    main()
