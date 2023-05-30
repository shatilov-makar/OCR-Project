[![Tests](https://github.com/shatilov-makar/OCR-Project/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/shatilov-makar/OCR-Project/actions/workflows/python-app.yml)
# Оцифровка уведомления о готовности к реализации арестованного имущества
## Состав команды:

- Шатилов Макар — Тимлид, развертывание приложения на платформе streamlit;
- Кудрин Данил — Решение задачи NER (распознавание именованных сущностей);
- Шерер Даниил — Алгоритм обработки приложения.

## Описание приложения
Цель приложения - перевод  в текстовый вид фотографии/скана документа определенного формата.

Алгоритм работы:
1. Загрузка скана фотографии, из которой необходимо получить данные в цифровом виде. 
2. Обработка, распознавание текста с помощью yandex vision https://cloud.yandex.ru/services/vision  
3. Вывод результата на UI

Приложение развернуто на платформе Streamlit: https://ocr-documents.streamlit.app
