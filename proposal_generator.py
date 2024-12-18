import os
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from config import MODEL_NAME, MAX_TOKENS, TEMPERATURE, TOP_P, OUTPUT_DIR


class ProposalGenerator:
    def __init__(self):
        """Загружает локальную модель и токенизатор."""
        print("Loading the GPT-2 model...")
        self.tokenizer = GPT2Tokenizer.from_pretrained(MODEL_NAME)
        self.model = GPT2LMHeadModel.from_pretrained(MODEL_NAME)
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    def generate(self, topic, examples, min_words=2000):
        """Генерирует текст по частям для длинных последовательностей."""
        if self.tokenizer.pad_token_id is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        prompt = self.create_prompt(topic, examples)
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt", truncation=True, max_length=1024)
        generated_text = prompt  # Начинаем с prompt

        while len(generated_text.split()) < min_words:
            output = self.model.generate(
                input_ids=input_ids,
                max_new_tokens=500,
                temperature=0.7,
                top_p=0.9,
                do_sample=True,
                pad_token_id=self.tokenizer.pad_token_id
            )
            new_tokens = output[0][input_ids.shape[-1]:]  # Новые токены после текущего input_ids
            new_text = self.tokenizer.decode(new_tokens, skip_special_tokens=True)

            if not new_text.strip():  # Проверка на пустой результат
                break

            generated_text += " " + new_text  # Добавляем новые токены к общему тексту

            # Обновляем input_ids с учетом нового текста, обрезая до max_length
            input_ids = self.tokenizer.encode(generated_text[-1024:], return_tensors="pt", truncation=True,
                                              max_length=1024)

        return generated_text

    def create_prompt(self, topic, examples, max_length=700):
        """Создает текст запроса с ограничением длины."""
        prompt = f"Generate a Project Proposal on the topic '{topic}'.\n\n"
        current_length = len(self.tokenizer.encode(prompt))

        for i, example in enumerate(examples):
            if current_length >= max_length:
                break

            if "title" in example:
                example_text = f"Example {i + 1}:\nTopic: {example['title']}\n"
                for section, content in example.get("sections", {}).items():
                    example_text += f"{section}:\n{content[:100]}...\n"  # Усечение длинного текста

                example_tokens = len(self.tokenizer.encode(example_text))
                if current_length + example_tokens <= max_length:
                    prompt += example_text
                    current_length += example_tokens
        return prompt
