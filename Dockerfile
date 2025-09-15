# Используем официальный образ Python
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости для сборки psycopg2
RUN apt-get update && apt-get install -y gcc python3-dev libpq-dev


# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Запускаем FastAPI-сервер
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
