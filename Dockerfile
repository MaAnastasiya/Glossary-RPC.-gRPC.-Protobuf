FROM python:3.10

# Установка зависимостей
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:/app"

# Копируем код и proto файлы
COPY . /app

# Генерация gRPC файлов (на случай, если что-то не сгенерировано)
RUN python -m grpc_tools.protoc -Iproto --python_out=. --grpc_python_out=. proto/glossary.proto

# Запуск сервера
CMD ["python", "server/server.py"]