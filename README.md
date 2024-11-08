# course_work_6

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/doc/)
[![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)](https://www.jetbrains.com/pycharm/documentation/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white&color=092E20&labelColor=gray)](https://www.djangoproject.com/start/)
[![HTML](https://img.shields.io/badge/HTML-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)](https://docs.github.com/en/actions)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/docs/)
[![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/documentation)

## 'Sky-mailing' (service for managing mailings)
Проект реализует сервис «прогревающих» рассылок для информирования и привлечения клиентов.
В приложение встроена автоматическая отправка сообщений с помощью планировщика задач Django APScheduler.

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

Воспользуйтесь шаблоном .env.sample для создания файла `.env`.
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