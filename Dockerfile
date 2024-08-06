FROM python:3.10-slim
LABEL authors="joyli"

# Обновление и установка зависимостей системы
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Установка рабочего каталога
WORKDIR /app

# Копирование файлов зависимостей в контейнер
COPY requirements.txt requirements.txt

# Установка Python-зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода в контейнер
COPY . .

# Установка стандартного пользователя для запуска приложения
RUN useradd -m appuser
USER appuser

# Определение команды для запуска контейнера
CMD ["python", "app.py"]
