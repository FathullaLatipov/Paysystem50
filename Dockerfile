# Указываем какой язык программирования и его весию
FROM python:latest
# Копируем наш проект внутри Docker и там создаем папку paysistem50
COPY . /paysistem50
# И говорим Docker что наш рабочий проект это paysistem50
WORKDIR /paysistem50
# Установка библиотек
RUN pip install -r requirements.txt
# Запуск проекта
CMD ["python", "manage.py", "runserver"]
