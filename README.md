# Online Store
Учебный проект онлайн магазина

## Инструменты в проекте:
- Django
- Django ORM
- Django templates
- Bootstrap 


## Особенности проекта:
- Модификация стандартной модели User
- Подтверждение электронной почты


# Develop

# Database
## Работа с fixtures
### Экспорт всех данных:
```bash
python manage.py dumpdata > fixtures/all_data.json --format=json 
```

### Экспорт данных конкретной модели:

```bash
python manage.py dumpdata products.ProductCategory > fixtures/product-category-fixtures.json --format=json 
```

### Импорт всех данных:

```bash
python manage.py loaddata fixtures/all_data.json
```

## Перенос данных из PostgreSQL
### Экспорт и импорт дампа
Используйте утилиту pg_dump для создания дампа базы данных:
```
pg_dump -U username -h hostname -p port dbname > backup.sql
```

### Экспорт и импорт дампа для **Windows**
```bash
& "C:\Program Files\PostgreSQL\15\bin\pg_dump.exe" '-U' 'postgres' '-h' 'localhost' '-p' '5432' 'store' > backup.sql
```

### Импортируйте данные из созданного дампа
```
psql -U username -d new_dbname -f backup.sql
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