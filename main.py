from loader import load_examples
from proposal_generator import ProposalGenerator
from logger import Logger

def main():
    print("Добро пожаловать в генератор Project Proposal на базе GPT-4!")

    # Шаг 1: Загрузка примеров
    examples_path = "examples"
    examples = load_examples(examples_path)
    if not examples:
        print("Примеры не найдены. Проверьте папку 'examples'.")
        return

    # Шаг 2: Получение темы от пользователя
    topic = input("Введите тему вашего Project Proposal: ")

    # Шаг 3: Генерация предложения
    generator = ProposalGenerator()
    proposal = generator.generate(topic, examples)

    # Шаг 4: Сохранение логов
    logger = Logger()
    logger.log(topic, proposal)

    # Шаг 5: Вывод результата
    print("\nСгенерированный Project Proposal:\n")
    print(proposal)
    print("\nРезультат сохранён в логах (logs/generation_log.json).")

if __name__ == "__main__":
    main()
