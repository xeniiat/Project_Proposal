import openai
from config import OPENAI_API_KEY, MODEL_NAME, MAX_TOKENS, TEMPERATURE
import os

class ProposalGenerator:
    def __init__(self, output_dir="generated"):
        openai.api_key = OPENAI_API_KEY
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)  # Создаем папку для сохранения текстов

    def generate(self, topic, examples):
        """Генерирует Project Proposal на заданную тему с разделами."""
        # Формируем контекст из примеров
        sections = self.extract_sections(examples)

        # Подготовка запроса к GPT-4
        prompt = self.create_prompt(topic, sections)

        # Запрос к модели
        response = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=[{"role": "system", "content": "Ты создаешь Project Proposal."},
                      {"role": "user", "content": prompt}],
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE
        )

        proposal = response['choices'][0]['message']['content']

        # Сохранение результата
        self.save_proposal(topic, proposal)

        return proposal

    def extract_sections(self, examples):
        """Извлекает секции из примеров."""
        sections = {}
        for example in examples:
            for section, content in example["sections"].items():
                if section not in sections:
                    sections[section] = []
                sections[section].append(content)
        return sections

    def create_prompt(self, topic, sections):
        """Создает текст запроса для GPT-4."""
        prompt = f"Создай Project Proposal на тему '{topic}'. Следующие примеры содержат структуру текста:\n\n"

        for section, contents in sections.items():
            prompt += f"Раздел {section}:\n"
            for content in contents:
                prompt += f"- {content}\n"
            prompt += "\n"

        prompt += "Создай новый текст с такими же разделами."
        return prompt

    def save_proposal(self, topic, proposal):
        """Сохраняет сгенерированный текст в файл."""
        filename = os.path.join(self.output_dir, f"{topic.replace(' ', '_')}_proposal.txt")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(proposal)
        print(f"Сгенерированный текст сохранен в {filename}")
