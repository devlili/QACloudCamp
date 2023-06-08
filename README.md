# Проект с автотестами для API-эндпоинтов

Данный проект представляет собой автоматизированные тесты для проверки работоспособности API-эндпоинтов. Тесты реализованы с использованием языка программирования Python, библиотеки `requests` для взаимодействия с API и библиотеки `pytest` для организации и запуска автотестов.

## API-эндпоинты
API, с которым взаимодействуют автотесты, располагается по следующему URL: https://jsonplaceholder.typicode.com/. В рамках проекта тестируются следующие методы API:

- GET /posts: Получение списка постов.
- POST /posts: Создание нового поста.
- DELETE /posts/{id}: Удаление поста по идентификатору.<br><br>
Каждый из этих методов может принимать параметры userId, id, title и body.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/devlili/QACloudCamp.git
```

```
cd QACloudCamp
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

## Запуск автотестов

 Для запуска всех автотестов выполните следующую команду:
 ```
 pytest
 ```


## Запуск автотестов в контейнере Docker

1. Установите Docker: https://www.docker.com/get-started
2. Соберите Docker-образ из Dockerfile с помощью команды:
```
docker build -t my-test-app .
```

Здесь `my-test-app` - это имя вашего Docker-образа. Вы можете выбрать любое другое имя.

3. Запустите контейнер на основе созданного образа с помощью команды:
```
docker run my-test-app
```
Запустив эту команду, контейнер будет создан, и автотесты будут выполнены внутри контейнера Docker.


## Автор

Лилия Альмухаметова
