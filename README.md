# Лабораторна робота 3

## Тема: Валідація, обробка помилок, ORM

### Мета роботи:
- Покращити проект шляхом додавання валідації вхідних даних, обробки помилок, та використання ORM з базою даних.
- Реалізувати новий функціонал відповідно до варіанту.

### Варіант 18 — Облік доходів
Реалізовано систему для обліку доходів користувачів з наступними можливостями:
1. **Створення рахунку користувача**: Унікальний рахунок з балансом.
2. **Поповнення балансу**: Додавання коштів на рахунок.
3. **Списання коштів**: Зняття коштів з рахунку, з перевіркою на наявність достатнього балансу.
4. **Перевірка балансу**: Отримання поточного стану рахунку.

### Інструкція з налаштування та запуску

1. Клонування репозиторію:
    ```bash
    git clone <URL_репозиторію>
    cd backend_lab_3

2. Встановлення залежностей:
    ```bash
    pip install -r requirements.txt

3. Запуск бази даних:
    ```bash
    docker-compose up -d

4. Ініціалізація бази даних:
    ```bash
    flask db upgrade

5. Запуск серверу:
    ```bash
    python run.py
