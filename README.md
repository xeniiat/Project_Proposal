# Генератор Project_Proposal

Описание
Данный проект представляет собой генератор Project Proposal ВКР(Выпускной квалификационной работы в НИУ ВШЭ для выпускников программы "Фундаментальная и прикладная лингвистика"), который использует модель GPT2 для создания текстов на заданную тему. Приложение загружает примеры из папки, анализирует структуру текстов и генерирует новый текст с сохранением разделов и логической последовательности.

Задачи и ответсвенные за них: 

    Екатерина Хомутова — разработка интерфейса;
    
    Воронцова Анна — написание тестов для проверки интерфейса;
    
    Торгашева Ксения — технический писательство и настройка CI

# Структура проекта
Файлы и их назначение:
proposal_generator.py — модуль, содержащий класс ProposalGenerator, который отвечает за генерацию текста предложения. Он включает методы для загрузки модели, создания запроса, генерации текста и сохранения результата.

examples — папка, содержащая файлы формата json, в которых хранятся тексты-примеры Project Proposal.

main.py — основной скрипт запуска программы. Здесь происходит взаимодействие с пользователем через консоль, загрузка примеров, вызов генератора и вывод результатов.

loader.py — модуль для загрузки примеров из файлов формата JSON. 

logger.py — модуль для ведения журнала событий. Записывает информацию о теме и сгенерированном предложении вместе с меткой времени.

config.py — файл конфигурации, содержащий параметры модели и пути к каталогам.

tests — пакет тестов, проверяющий интерфейс программы.

.github — папка, в которой хранится yaml файл для автотестов.

