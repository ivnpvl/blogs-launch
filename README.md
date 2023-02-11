## yatube_project
Социальная сеть блогеров для публикации личных дневников. 
Пользователи могут публиковать записи на своей странице, заходить на чужие
страницы, подписываться на авторов и комментировать их записи. 

## Технологии
- Python   3.9.16
- Django   2.2.19
- pytz     2022.7.1
- sqlparse 0.4.3

## Инструкции по запуску в dev-режиме
Копируйте проект из репозитория:
```
git clone <project-url>
```
Установите виртуальное окружение и необходимые пакеты:
``` 
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Запустите проект в dev-режиме:
```
python3 manage.py runserver
```

## Автор
Ivan Pavlov (divaythfyr@mail.ru)