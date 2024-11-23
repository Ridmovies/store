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