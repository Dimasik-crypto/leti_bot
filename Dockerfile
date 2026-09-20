FROM python:3.12-slim

WORKDIR /app

# Устанавливаем aiogram НАПРЯМУЮ — не зависим от requirements.txt
RUN pip install --no-cache-dir aiogram

# Копируем всё содержимое репозитория
COPY . .

# Запускаем бота
CMD ["python", "leti.py"]
