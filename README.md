# Online Store
Учебный проект онлайн магазина

## Инструменты в проекте:
- Django
- Django ORM
- Django templates
- Bootstrap (локально)


## Особенности проекта:
- Модификация стандартной модели User


# Develop

## Работа с fixtures
### Экспорт всех данных:
```bash
python manage.py dumpdata > fixtures/all_data.json --format=json 
```

### Экспорт данных конкретной модели:

```bash
python manage.py loaddata product_app.Product >fixtures/products-fixtures.json --format=json
```

### Импорт всех данных:

```bash
python manage.py loaddata fixtures/all_data.json
```

## Линтеры и форматеры:
```bash
black --check --diff .\product_app\views.py
```

```bash
isort --check-only --diff --profile black .\product_app\views.py
```

```bash
mypy --incremental ./product_app/views.py 
```

```bash
flake8 . 
```