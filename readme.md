# Сайт посещения хранилища банка с записями в базу данных.

## Данный сайт обрабатывает базу данных с картами доступа в хранилище банка, записывая посещения и вычисляя время нахождения в хранилище

[![Supported Versions](https://img.shields.io/pypi/pyversions/requests.svg)](https://pypi.org/project/requests)

### Как установить:

для подключения к базе данных нужно ввести данные самой базы в файле .env, в формате:

```python
'ENGINE': 'paste_here_engine',
'HOST': 'paste_here_host',
'PORT': 'paste_here_port',
'NAME': 'aste_here_host_name',
'USER': 'paste_here_host_user',
'PASSWORD': 'paste_here_host_password'
```
Так же потребуется версия Django 3.2
Python3 должен быть уже установлен.

### Затем нужно создать папку виртуального окружения:

```shell
 python -m venv venv
```
 
### После запустить виртуальное окружение:

```shell
venv\Scripts\activate.bat
```

### Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```shell
pip install -r requirements.txt
```

### Далее запустить проект командой:

```shell
python manage.py runserver 0.0.0.0:8000
```

## Цель проекта:
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
