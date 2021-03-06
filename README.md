# Шаблоны Форм
## Описание
Данный проект представляет собой REST API бекэнд для поиска шаблона форм, хранящихся в TinyDB (db.json).  
[Тестовое задание](https://docs.google.com/document/d/1fMFwPBs53xzcrltEFOpEG4GWTaQ-5jvVLrNT6_hmC7I/edit#)
## Дисклеймер
Данный проект был написан и протестирован с использованием **Python 3.9.6**, поэтому рекомендуется использовать именно эту версию, но полагаю версии выше будут также работать.  
## Установка
Для начала склонируйте данный репозиторий на свою локальную машину с помощью команды:
```
git clone https://github.com/Strategka/formcom.git
```
Переходим в корень репозитория:
```
cd formcom
```
Далее установите зависимости, указанные в requirements.txt:  
```
pip install -r requirements.txt
```
После установки зависимостей, можно запускать проект:
```
uvicorn main:app
```
Или, если хотите редактировать проект без перезапуска:
```
uvicorn main:app --reload
```
В приветственном сообщении будет написана ссылка к API.  
По умолчанию ссылка - **http://localhost:8000/**
## Тестирование
После запуска проекта, выполните скрипт:
```
python3 test.py
```
Она выполнит пару тестовых запросах и выведет результат работы.  
