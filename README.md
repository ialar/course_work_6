# course_work_6

## 'Sky-mailing' (service for managing mailings)
Проект реализует сервис «прогревающих» рассылок для информирования и привлечения клиентов.
В приложение встроена автоматическая отправка сообщений с помощью планировщика задач Django APScheduler.

## Стек
* Python
* Django
* HTML
* PostgreSQL
* Redis

## Установка и запуск
1. Клонируйте репозиторий с помощью команды:
    ```shell
   git clone https://github.com/ialar/course_work_6.git
    ```
2. Перейдите в папку проекта:
    ```shell
        cd course_work_6
    ```
3. Установите необходимые зависимости, выполнив команду:
    ```shell
        pip install -r requirements.txt
    ```
Воспользуйтесь шаблоном .env.sample для создания файла `.env`

Создайте БД, примените миграции и загрузите необходимые данные с помощью фикстур (.\fixtures\):
```commandline
psql -U postgres  
postgres=# CREATE DATABASE <db_name>;
CREATE DATABASE
postgres=# \q
```

Запустите Redis:
```commandline
sudo service redis-server start
```

Для запуска рассылки выполните следующую команду:
```shell
py .\manage.py runmailing
```