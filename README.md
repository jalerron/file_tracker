# File tracker

Данный сервис  используется для обработки загружаемых данных администратором. 
API для приема документов со стороны фронтенда. 
При поступлении документа от зарегистрированного пользователя, сервис уведомляет по почте администраторов платформы. 
После того, как администратор подтвердил документ, отправляет письмо пользователю, который загружал документ. 

## Используемый стэк
      
- python
- postgresql
- docker
- Django + DRF


## Запуск проекта

   1. Склонирвоать репозиторий 
```bash
   git clone <https://github.com/jalerron/file_tracker.git>
  ```
   2. Установить docker и docker-compose. Инструкция представлена ниже

      https://docs.docker.com/get-docker/

   3. Выполнить две команды в корне склонированного репозитория для запуска сервиса:
```bash
      1. docker-compose build
      2. docker-compose up
```

## В данном сервисе автоматически создается администратор:

```angular2html
    USERNAME - admin
    PASSWORD - 123qweASD
    EMAIL - admin@admin.admin
```

## Документация API

Документация API доступна после запуска сервера по адресу: http://localhost:8000/redoc/ или http://localhost:8000/swagger/