# Проект 'PracticREST'
 
## Описание:

Проект PracticREST - это проект по обучению основам фреймворка django.

## Установка:

1. Клонируйте репозиторий:
```commandline
git clone https://github.com/SergeyBordeychuk/PracticREST.git
```
2. Установите зависимости:
```commandline
pip install -r requirements.txt
```

## Функционал
1. Запуск сервера
```commandline
python manage.py runserver
```

2. Действие на сервере
```commandline
Просмотр, создание, изменение и удаление уроков, курсов и платежей.
```

3. Новый функционал
```commandline
Добавлена подписка и документация по ссылке /swagger/
```

4. Закрыть сервер
CTRL+C

5. Docker
```commandline
Для запуска можно использовать команду docker-compose up -d --build
```
6. Проверка работоспособности каждого сервиса
```commandline
docker ps
```
```commandline
docker stats
```
```commandline
docker-compose logs
```
