practice_django4

# Начало работы

`pip install django`

## Формы

[cripsy-forms](https://django-crispy-forms.readthedocs.io/en/latest/install.html)

`pip install django-crispy-forms==1.14.0`

## Авто-очистка
[cleanup](https://github.com/un1t/django-cleanup)

`pip install django-cleanup==6.0.0`

## Редактор изображений

[pillow](https://pypi.org/project/Pillow/)

`pip install pillow==9.2.0`

## Текстовый редактор

[ckeditor](https://pypi.org/project/django-ckeditor/)

[документация на русском](https://russianblogs.com/article/5550650974/)

`pip install django-ckeditor==6.4.2`

## Каналы

[channels](https://channels.readthedocs.io/en/stable/)

`python -m pip install -U channels`

## Аутентификация

[django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)

`pip install django-allauth==0.51.0`

## Настройка dotenv

[dotenv](https://pypi.org/project/python-dotenv/)

[документация на русском](https://pythobyte.com/python-dotenv-module-90588/)

`pip install python-dotenv==0.20.0`

```python

# settings.py
## importing the load_dotenv from the python-dotenv module
from dotenv import load_dotenv

## using existing module to specify location of the .env file
from pathlib import Path
import os

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

# retrieving keys and adding them to the project
# from the .env file through their key names
SECRET_KEY = os.getenv("SECRET_KEY")
DOMAIN = os.getenv("DOMAIN")
EMAIL = os.getenv("EMAIL")
```


## ???

[braces](https://django-braces.readthedocs.io/en/latest/)

`pip install django-braces==1.15.0`

## Документирование проекта при помощи `mkdocs`

[mkdocs](https://www.mkdocs.org/)

`pip install mkdocs`

[плагин mkdocs](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin)

`pip install mkdocs-awesome-pages-plugin`