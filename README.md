# Online Store
Учебный проект онлайн магазина

## Инструменты в проекте:
- Django
- Django ORM
- Django templates
- Bootstrap 
- django-allauth
- Redis 
- Celery


## Особенности проекта:
- Модификация стандартной модели User
- Подтверждение электронной почты
- Логин с помощью OAuth 2.0 Github provider 
- Кэширование с Redis
- Оплата заказа с помощью YooKassa

## На доработку:
- Работает только ручная проверка статуса заказа от YooKassa
- Создать правильную структура проекта
### Пример ручной проверки заказа:
http://127.0.0.1:8000/orders/check_payment/<payment_id>/
payment_id: id платежа
http://127.0.0.1:8000/orders/check_payment/2ede3d52-000f-5000-8000-1686255115b4/
Запускает функцию проверки, обновления заказа и очистки корзины


## Установка и запуск
### Шаги установки

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/Ridmovies/store.git
    ```
2. Перейдите в директорию проекта:
   ```bash
   cd repository
   ```
    
3. Активируйте виртуальное окружение:
    ```bash
    source venv/bin/activate
    ```
   
4. Установите зависимости из [requirements.txt]:
    ```bash
    pip install -r requirements.txt
    ```
   
5. Создайте файл .env в корневой директории проекта и добавьте туда необходимые переменные окружения. Для примера смотри файл [.env.example](.env.example)
   ```bash
   touch .env
   echo "SECRET_KEY=your_secret_key_here" >> .env
   ```

6. Создай Базу данных [postgres](#postgres) или используй [sqlite](#sqlite)
7. Выполните миграцию базы данных:
    ```bash
    python manage.py migrate
    ```
8. Создание суперпользователя
    ```bash
    python manage.py createsuperuser
    ```
9. Запустите сервер разработки:
    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```

## Установка с Docker
### Требования

- Docker
- Docker Compose

### Шаги установки

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/Ridmovies/store.git
    ```
2. Перейдите в директорию проекта:
   ```bash
   cd repository
   ```

3. Создайте файл .env в корневой директории проекта и добавьте туда необходимые переменные окружения. Для примера смотри файл [.env.example](.env.example)
   ```bash
   touch .env
   echo "SECRET_KEY=your_secret_key_here" >> .env
   ```

4. Запустите контейнеры с помощью Docker Compose:
    ```bash
   docker-compose up -d
   ```
   
Подробнее о работе с [Docker](#docker)



### Стартовая страница приложения
        http://127.0.0.1:8000/

### Панель администратора
        http://127.0.0.1:8000/admin



# Develop

# Database
<a id="sqlite"></a>
## Создание базы данных SQLite
В файле [settings.py](store/settings.py) раскомментируйте блок SQLite и закомментируйте Postgres

<a id="postgres"></a>
## Создание базы данных postgres
PostgreSQL присутствует в официальных репозиториях Ubuntu, поэтому для установки достаточно выполнить:
```bash
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
```

переключитесь на сессию данного пользователя:
```bash
sudo su - postgres
```

После чего запустите консоль Postgres:
```bash
psql
```

Чтобы создать новую роль выполните:
```bash
CREATE ROLE имя_роли WITH LOGIN CREATEDB CREATEROLE;
```
Далее задайте новому пользователю пароль:
```bash
\password имя_роли
```

Для создания базы из консоли Postgres, используйте:

```bash
CREATE DATABASE имя_базы;
```

Подключение к базе данных 
```bash
psql -U postgres -d store -h localhost -W
```

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

## Команды для работы с Redis
### Запустить Redis на локальной машине
```bash
sudo service redis-server start
```

### Проверка состояния через команду PING
Команда PING отправляет запрос серверу Redis и ожидает ответа. Если сервер отвечает «PONG», значит он доступен и готов принимать команды.

```bash
redis-cli PING
```

## Команды для работы с Celery
### Запуск рабочего процесса
```bash
celery -A store worker -l INFO
```

### Запуск планировщика
To start the celery beat service:
```bash
celery -A store beat -l INFO
```

<a id="docker"></a>
## Команды для работы с Docker 
собрать образ Docker
```bash
docker build -t store_server .
```

1. Запуск контейнера:
```bash
   docker run -p 5000:5000 --name myapp store_server
```
 Эта команда запускает контейнер в фоновом режиме (-d), перенаправляет порт 5000 внутри контейнера на порт 5000 снаружи (-p 5000:5000) и называет контейнер myapp.


## Команды для работы с Docker Compose
Эти команды помогут управлять контейнерами и образами в вашем проекте, обеспечивая удобный процесс разработки и тестирования.

## Для запуска консоли внутри работающего Docker-контейнера используется команда docker exec
```bash
docker exec -it megano bash 
```


### Остановка и удаление всех сервисов и образов

```bash
docker-compose down --rmi all
```
Эта команда останавливает и удаляет все сервисы, созданные с помощью `docker-compose`, а также удаляет образы, использованные этими сервисами.

### Сборка нового образа

```bash
docker-compose build
```
Эта команда собирает новый образ на основе инструкций в `docker-compose.yml`.