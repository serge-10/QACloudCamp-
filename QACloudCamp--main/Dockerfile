# Используем базовый образ Python
FROM python:3.11

# Установка зависимостей
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# Копирование файлов проекта
COPY . /app

# Установка рабочей директории
WORKDIR /app

# Запуск команды pytest при запуске контейнера
CMD pytest
