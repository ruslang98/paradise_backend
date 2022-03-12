### Проект написан на Python 3.9.5

### Установка

Установка зависимостей.

```sh
$ pip install -r requirements.txt
```

### Не забудьте миграции.

```sh
$ python manage.py migrate
```

### Наполнение БД точками и маркировками .

```sh
$ python manage.py fill_db_from_csv
```

```sh
$ python manage.py load_labels
```

### Запуск dev сервера

```sh
$ python manage.py runserver
```


### Django admin

Для доступа в Django admin необходимо создать суперпользователя.

```sh
$ python manage.py createsuperuser
```
### Swagger/Redoc

`BASE_URL/swagger/`

`BASE_URL/redoc/`
