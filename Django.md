---
title:
- Django
author:
- Dario Necco
theme:
- Nalug
date:
- Feb 02, 2022
---

---#
![](Django/django.png)

---#
# About me

![](common/me.jpg)

* Principal Technical Consultant Engineer @ Perforce
* [https://www.linkedin.com/in/dartie/](https://www.linkedin.com/in/dartie/)
* Member of Nalug ([https://www.nalug.tech/](https://www.nalug.tech/))
* Python and Go(lang) developer

---#
# Introduction
* Django is a Python-based free and open-source web framework that follows the model–template–views architectural pattern. It is maintained by the Django Software Foundation, an independent organization established in the US as a 501 non-profit.

* Created in 2003, by the Lawrence Journal-World newspaper, Adrian Holovaty and Simon Willison

* Released publicly under a BSD license in July 2005

* The framework was named after guitarist Django Reinhardt.

* In June 2008, it was announced that a newly formed Django Software Foundation (DSF) would maintain Django in the future.

---## 
# Django MTV

Django follows MVC pattern very closely but it uses slightly different terminology. Django is essentially an MTV (Model-Template-View) framework. Django uses the term Templates for Views and Views for Controller. In other words, in Django views are called templates and controllers are called views.

---#
# MVC

MVC architecture divides an application into the following three layers:

1. Model
1. View
1. Controller

![](Django/mvc.png)

---##
## Model
* Models represents how data is organized in the database. 
* In MVC pattern we use models to define our database tables as well as the relationships between them.

---##
## Views
* A view is what you see when you visit a site. 

* For example, a blog post, a contact form etc, are all examples of views. 

* A View contains all the information that will be eventually sent to the client i.e a web browser. Generally, views are HTML documents.

---##
## Controller
* Controller controls the flow of information. 

* When you request a page that request is passed to the controller then it uses programmed logic to decide what information is needed to pull from the database and what information should it pass to the view. The controller is the heart of the MVC architecture because it acts as a glue between models and views.

---##
## Steps involved in an MVC application

1. Web browser or client sends the request to the web server, asking the server to display a blog post.

1. The request received by the server is passed to the controller of the application.

1. The controller asks the model to fetch the blog post.

1. The model sends the blog post to the controller.

1. The controller then passes the blog post data to the view.

1. The view uses blog post data to create an HTML page.

1. At last, the controller returns the HTML content to the client.


---##
## Note

* Django calls **Controller** the "view", and the **View** the "template"


---# 
# GET vs POST request

* `GET`: is used to request data from a specified resource (not modify).
    * GET requests can be cached and remain in the browser history
    * GET requests can be bookmarked
    * GET requests should never be used when dealing with sensitive data
    * GET requests have length restrictions

```
/test/demo_form.php?name1=value1&name2=value2
```

* `POST`: is used to send data to a server to create/update a resource.
    * POST requests are never cached and don't remain in the browser history
    * POST requests cannot be bookmarked
    * POST requests have no restrictions on data length


---#
# Why Django

* Among others python web frameworks (flask, fastapi, etc), it provides everything out-of-box: database, authentication, template engine.

* It allows to switch easily from a database to another (by default sqlite3 is used)

---#
# Installation and Setup

### 1 - Create virtual environment

```bash
# Install virtualenv module
pip3 install virtualenv

# Create virtual environment
virtualenv ${virtual-environment-name}   

# Activate virtual environment
source ${virtual-environment-name}/bin/activate  #    Linux
${virtual-environment-name}\Scripts\activate.bat #    Windows
```

### 2 - Install Django

```bash
pip3 install django
```

### 3 - Create Django project

```bash
# create django project
django-admin startproject ${project-name} . 
```

---##

* Supposing we call the project "core"
```
<current-folder>/
│
└── core/
    │
    ├── core/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    │
    └── manage.py
```

---##

* If the dot is omitted, the additional top-level project folder is avoided
```
<current-folder>/
│
├── core/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── manage.py
```

---## 

### 4 - Create Django app

* Django is formed of apps, which allow to keep the source code separated and organized.

```bash
django-admin startapp ${app-name}
```

---##

```
<project-folder>/
│
├── example/
│   │
│   ├── migrations/
│   │   └── __init__.py
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── <project-name>/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── manage.py
```

---##


```bash
{data-line-numbers="18|19|13|11|5"}
<project-folder>/
│
├── example/
│   │
│   ├── migrations/
│   │   └── __init__.py
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── <project-name>/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── manage.py
```

---##

### 5 - Declare app in Django project

* In `/settings.py`, to **INSTALLED_APPS** list, add:
    
```bash
'app.apps.AppConfig'  # main app
```
    
where:

- `app` is the folder name
- `apps` refers to `app\apps.py`
- `AppConfig` is the Class name

---##

### 6 - Set template folder

* In `/settings.py`, to **TEMPLATES** list, add the template path:
```bash
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # new
        ...
    },
]
```

* Create `templates` folder in the project root

* The template engine is `jinja2`

---##

### 7 - Apply the changes

```bash
python manage.py makemigrations
python manage.py migrate
```

---## 

### 8 - Create the first user (admin)

```bash
python manage.py createsuperuser
```

or 

```bash
python manage.py createsuperuser --username ${username} --email ${email}
```

---##

### 9 - Run Django server

```bash
python manage.py runserver
```

* specify additional info

```bash
python manage.py runserver ${clientIP}:${port}
```

```bash
python manage.py runserver 0.0.0.0:8000
```

!!! note

    `0.0.0.0` allows the connection from all clients, however check that `ALLOWED_HOSTS` is set to `["*"]` in the `/settings.py` file.


---##

### 9 - Create the first route

* /urls.ypy

```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "home.html", {})
```


---#

# Use static files

* It allows to serve static files (js, image, css, etc.)

* Per Django structure, static files are located in each app

* Collect all apps' static files into the main static folder

```python
python manage.py collectstatic --noinput --clear
```

* Use static files in template for rendering

```html
{% load static %}

...

<link rel="stylesheet" href="{% static "css/style.css" %}">
```

---##

## `settings.py` configuration

```python
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra lookup directories for collectstatic to find static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
```


---# 
# Additional settings (`/settings.py`)

* Allow all hosts to connect:

```python
ALLOWED_HOSTS = ['*']
```

* Enable/disable DEBUG: Detailed error pages: if your app raises an exception when DEBUG is True, Django will display a detailed traceback, including a lot of metadata about your environment

```python
DEBUG = True
```

!!! warning

    &bull; `DEBUG = True` exposes the server to security flaws
    
    &bull; Due to storage of each SQL query execution and other debug info, it consumes more memory on a production server.


---#

# Django Admin interface

* connect to `/admin/` route (e.g.: [http://127.0.0.1:8000](http://127.0.0.1:8000))

![](Django/django-admin.png)

---#

# Store data into the database (models)

* Database connection settings in `/settings.py`

```python
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

* The database file is created at the django project level

* [Mozilla - Django Models](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models)

---##

## Supported databases
* PostgreSQL
* MySQL
* SQLite
* Oracle
* MariaDB


---##

# Create a new table

1. Edit `/models.py` adding classes (tables) and fields.
1. Apply the changes with

```python
python manage makemigrations  # creates migrations files
python manage migrate         # execute migrations scripts
```

* Fields reference: [Model field reference](https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-options)


---##

```python
from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
```


---##

# Advanced topics

## Models Options

* Order fields, verbose names

`-` prefix, which indicates descending order.

```python
ordering = ['-release_date']
```

* Assign a custom name to db table: by default, the table name is formed of `<app-name><Model-Class-Name>` all lowercase.

```python
class Person(models.Model):
    class Meta:
        db_table = 'my_table'
```

---##

* `verbose_name` and `verbose_name_plural`

If you create a database table called 'Child' and register it in the admin.py file and go to the admin page, you'll see 'Childs'.

```python
class Child(models.Model):
    name= models.CharField(max_length=100, verbose_name="Child's First Name and Last Name")
    weight= models.DecimalField(max_digits=3, decimal_places=2)

    class Meta:
        verbose_name = 'Child'
        verbose_name_plural = 'Children'
```

* [Django - Model Options](https://docs.djangoproject.com/en/4.0/ref/models/options)

---##

## Override default methods

* `save()`
* `delete()`
* `__str__()`

```python
from django.db import models
 
# importing slugify from django
from django.utils.text import slugify
 
# Create your models here.
class GeeksModel(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.SlugField()
 
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(GeeksModel, self).save(*args, **kwargs)
```

[Django - Models](https://docs.djangoproject.com/en/4.0/topics/db/models/)


---##

## Methods in Model classes

* Custom Models methods can be written 

```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def is_infant(self):
        import datetime
        if int((date.today() - birthDate).days / days_in_year) <= 1:
            return True
        else:
            return False

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)
```

---##

* `@property` decorator allows to use it as a property, rather than a method

```python
Person.full_name
# instead of
Person.full_name()
```

---#

# Routing (`urls.py`)

```python
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my-route/', views.my_view),
]
```

* When route `/my-route/` is hit, function `my_view` in `view.py` is called.

* `name` keyword, allows to give a name to the url and refer to it by name in controller or template

```python
redirect('app.main')
```

```html
<a href="{% url 'app.main' %}">Go to main</a>
```


* [urls](https://docs.djangoproject.com/en/4.0/topics/http/urls)

---##

## Variables in route

```python
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my-route/<int:variable>', views.my_view),
]
```

* Multiple combinations can now hit our route: `my-route/1` is a valid one.

---##

Types accepted:

* `str` - Matches any non-empty string, excluding the path separator, '/'. This is the default if a converter isn’t included in the expression.
* `int` - Matches zero or any positive integer. Returns an int.
* `slug` - Matches any slug string consisting of ASCII letters or numbers, plus the hyphen and underscore characters. For example, building-your-1st-django-site.
* `uuid` - Matches a formatted UUID. To prevent multiple URLs from mapping to the same page, dashes must be included and letters must be lowercase. For example, 075194d3-6885-417e-a8a8-6c931e272f00. Returns a UUID instance.
* `path` - Matches any non-empty string, including the path separator, '/'. 


---##

## Bypass views.py

```python
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('about/', TemplateView.as_view(template_name="about.html")),
]
```

`TemplateView.as_view(template_name="about.html")` allows to render the template `about.html`

---#

# Controller (`views.py`)

```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse, Http404, HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from app.models import Table

@login_required
def my_view(request, mode):
    if request.method == "GET":
        return HttpResponse("Hello World!")
```

---##

## Decorators

* Function that takes another function and extends the behavior of the latter function without explicitly modifying it.

* Decorators provide a simple syntax for calling higher-order functions.

* `@login_required` allows to render the webpage only if the user is authenticated.

    ```python
    from django.contrib.auth.decorators import login_required

    @login_required
    def my_view(request, mode):
        # ...
    ```

---##

* `@require_http_methods` restricts access to views based on the request method. 

    ```python
    @require_http_methods(["GET", "POST"])
    def my_view(request):
        # I can assume now that only GET or POST requests make it this far
        # ...
        pass
    ```

---##

## Custom decorators

* Custom decorators can be written for achieving different scopes.

---##

# Render a template
* `views.py`
```
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse, Http404, HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from app.models import Table

@login_required
def my_view(request, mode):
    if request.method == "GET":
        name = "Dario"
        return render(request, "Template.html.jinja", {"name": name})
```

---##

* `/template/Template.html.jinja`

```html
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
    Hello {{ name }}
</body>
</html>
```

---#

## Template organization

### extends

* `base.html.jinja`

```html
<!DOCTYPE html>
<html>
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Title</title>
  </head>
 <body>

    {% block content %}

    {% endblock %} 
      
  </body>
</html>
```

---##


* `home.html.jinja`

```html
{% extends 'base.html.jinja' %}

{% block content %}

<h1>Homepage</h1>

{% endblock %}
```


---##


### includes

* `navbar.html.jinja2`

```html
<!--Navbar-->
<nav class="navbar navbar-expand-sm navbar-light bg-light">
  ...
</nav>
```

* `home.html.jinja`

```html
{% extends 'base.html.jinja' %}

{% block content %}
{% include 'navbar.html.jinja' %}

<h1>Homepage</h1>

{% endblock %}
```

---#

## Template syntax (Jinja2)

### Variable

* string

```html
{{ variable }}
```

* Objects use dot notation

```html
{{ my_dict.key }}
{{ my_object.attribute }}
{{ my_list.0 }}
```

* Comment

```html
{# this won't be rendered #}
```

---##

* Filters: transform the values of variables and tag arguments

```html
{{ variable|title }}
```

`django -> Django`


---##

## Custom Filters

```html
{{ variable|title }}
```

`django -> Django`


---##

## Conditions (if, elif, and else)

```html
{% if athlete_list %}
    Number of athletes: {{ athlete_list|length }}
{% elif athlete_in_locker_room_list %}
    Athletes should be out of the locker room soon!
{% else %}
    No athletes.
{% endif %}
```

---##

## List Iteration (For loop)

```html
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% endfor %}
</ul>
```

## Dictionary iteration

```html
<ul>
{% for athlete, age in athlete_dict.items %}
    <li>{{ athlete.name }} - Age : {{ age }}</li>
{% endfor %}
</ul>
```

---##

## Get user information in the template

```html
{{ user.first_name }}
```

---#

# Submit info (from webpage to the server)

* `POST` method is used
* `csrf_token` is required: [CSRF](https://docs.djangoproject.com/en/4.0/ref/csrf/)

* `myTemplate.html.jinja2`
    ```html
    <form id="myForm" action="/my-url/" method="POST" enctype="multipart/form-data">
    {% csrf_token %}

        <input type="text" id="fname" name="fname">
        <input type="text" id="lname" name="lname[]">
    <!-- ... -->
    </form>    
    ```

* `views.py`
    ```
    request.POST.get('fname')
    request.POST.getlist('lname')
    ```

---##

# AJAX

```javascript
/* AJAX definition */
function AJAX(url, data, method='GET', async=true){
    return new Promise(function(resolve, reject) {
        var formData = new FormData();

        for (var key in data) {
            // check if the property/key is defined in the object itself, not in parent
            if (data.hasOwnProperty(key)) {
                formData.append(key, data[key]);
            }
        }

        var xhr = new XMLHttpRequest();

        // Add any event handlers here...
        xhr.onload = function() {
            resolve(this.responseText);
        };
        xhr.onerror = reject;

        xhr.open(method, url, async);
        xhr.send(formData);
        //return false; // To avoid actual submission of the form
    });
}
```

---##

```javascript
/* AJAX call */
let settings_dict = {};
settings_dict['refresh_timeout'] = timeout;

let settings_json = JSON.stringify(settings_dict);

AJAX("/update_db_settings/" + settings_json, "POST")
.then(function(result) {
    // Code depending on result
    ;
})
.catch(function() {
    // An error occurred
});
```


---#

# Store and retrieve data

* Supposing this model

```python
class Person(models.Model):
    first_name = models.CharField(...)
    last_name = models.CharField(...)
    birth_date = models.DateField(...)
```

## Store

```python
new_person = Person.objects.create(
    first_name="Dario",
    last_name="Necco"
)

new_person.save()
```


---##

## Retrieve data from the database


### 1 - Using objects

```python
person = Person.objects.get(id=1).first()
```

```python
Person.objects.order_by().values_list('first_name')

Person.objects.order_by().values('first_name')

Person.objects.all().values('first_name')
```

### 2 - Raw query

```python
for p in Person.objects.raw('SELECT * FROM myapp_person'):
    print(p)
```

or, avoiding the model completely:

```python
from django.db import connection, transaction
cursor = connection.cursor()

# Data modifying operation - commit required
cursor.execute("UPDATE app_person SET first_name = 'Dario' WHERE id = 1")
transaction.commit_unless_managed()

# Data retrieval operation - no commit required
cursor.execute("SELECT first_name FROM app_person WHERE id = 1")
row = cursor.fetchone()
```

---#

# Extra

---#

## Extend Django commands 

1. Create `my_custom_command.py` in `<project>/<app>/management/commands`
1. Write the function in it: it will be executed every time `python manage.py my_custom_command` is executed

```python
from django.core.management.base import BaseCommand
from django.utils import timezone

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)
```

---#

## Extend User information

* `models.py`

    ```python
    class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        role = models.IntegerField(default=0)
        phone = models.CharField(max_length=30, blank=True)
        birth_date = models.DateField(null=True, blank=True)
        picture = models.BinaryField(blank=True)
        signature = models.BinaryField(blank=True)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    ```

---##

* `views.py`: Access to all information

    ```python
    from django.contrib.auth import get_user_model

    UserModel = get_user_model()
    all_users = UserModel.objects.all().select_related("profile")
    ``` 

---##

* Example of retrieving user information with all info

```python
def get_all_users(key="username"):
    users_dict = {}
    UserModel = get_user_model()
    all_users = UserModel.objects.all().select_related("profile")
    all_roles = Roles.objects.all()

    for user in all_users:
        try:
            user_profile = user.profile
            user_profile_dict = user_profile.__dict__
        except:
            user_profile = None
            user_profile_dict = {}

        user_dict = user.__dict__

        # populate user dictionary
        users_dict[user_dict[key]] = {**user_profile_dict, **user_dict}

    return users_dict
```


---#

## Use https instead of http

1. Install [mkcert](https://github.com/FiloSottile/mkcert)
    ```bash
    brew install mkcert
    ```

    for Linux and MacOs, or for Windows:
    ```bash
    choco install mkcert
    ```


1. Generate a certificate
    ```bash
    mkcert -cert-file cert.pem -key-file key.pem localhost 127.0.0.1
    ```

---##

1. Configure Django server to work with https
    1. Installed required packages
        ```python
        pip install django-extensions Werkzeug
        ```

    1. Add `django_extensions` to the `INSTALLED_APPS` list:

        ```python
        INSTALLED_APPS = [
            # other apps
            "django_extensions",
        ]
        ```

1. Run the server

    ```bash
    python manage.py runserver_plus --cert-file cert.pem --key-file key.pem
    ```

---#

## Build API

1. Install the required package
    ```bash
    pip install djangorestframework
    ```

1. Create a dedicate app for the api (I called it `api`)
    ```bash
    django-admin.py startapp api
    ```

1. Add `rest_framework` and your app to the `INSTALLED_APPS` list:

    ```python
    INSTALLED_APPS = [
        # other apps
        "rest_framework",       # <-- rest_framework
        'example.api',          # <-- project app
    ]
    ```    

---##

1. Apply the changes
    ```bash
    python manage.py migrate
    ```

1. Add route in `url.py`
    ```python
    from django.urls import path
    from myapi.core import views

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('hello/', views.HelloView.as_view(), name='hello'),  # <-- api
    ]
    ```

---##


1. Add code in the `views.py`
    ```python
    from rest_framework.views import APIView
    from rest_framework.response import Response

    class HelloView(APIView):
        def get(self, request):
            content = {'message': 'Hello, World!'}
            return Response(content)
    ```

---##

## Add API authentication

* Add code in the `views.py`
    ```python
    {data-line-numbers="3,6"}
    from rest_framework.views import APIView
    from rest_framework.response import Response
    from rest_framework.permissions import IsAuthenticated  # <-- Auth

    class HelloView(APIView):
        permission_classes = (IsAuthenticated,)             # <-- Auth

        def post(self, request):
            content = {'message': 'Hello, World!'}
            return Response(content)

        def get(self, request):
            content = {'message': 'Hello, World!'}
            return Response(content)
    ```

---##

* Add code to `settings.py`
    ```python
    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',  # <-- Returns the json instead of a webpage: https://stackoverflow.com/questions/51800895/django-returning-webpage-instead-of-json 
        ),
        'DEFAULT_PARSER_CLASSES': [
            'rest_framework.parsers.JSONParser',  # <- Handles JSON requests
            'rest_framework.parsers.FormParser',  # <- Handles x-www-form-urlencoded requests
        ],
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.TokenAuthentication',  # <-- Auth
        ],
    ```

---##

* Add route for api-token

    ```python
    from django.contrib import admin
    from django.urls import path
    from myapi.core import views
    from rest_framework.authtoken.views import obtain_auth_token            # <-- Request Token


    urlpatterns = [
        path('admin/', admin.site.urls),
        path('hello/', views.HelloView.as_view(), name='hello'),            # <-- api
        path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- Request Token
    ]
    ```

* Apply the changes
    ```bash
    python manage.py migrate
    ```

---##

* Create a token for a user

    ```bash
    # create user
    python manage.py createsuperuser --username dartie --email dartie@example.com

    # create token: it will return a string to annotate (token)
    python manage.py drf_create_token dartie
    ```

* Create a token using python code

    ```python
    def generate_or_renew_token(user):
        from rest_framework.authtoken.models import Token

        User_to_update = User.objects.get(username=user)
        token, created = Token.objects.get_or_create(user=User_to_update)  # get token info

        if not created:
            token.delete()  # delete current token
            token, created = Token.objects.get_or_create(user=User_to_update)  # regenerate token

        return token
    ```

---##

## Make requests

* Using the terminal

```bash
# BASH
curl http://127.0.0.1:8000/hello/ -H "Authorization: Token 9054f7aa9305e012b3c2300408c3dfdf390fcddf"
```

* With python code

```python
# python
import requests

url = 'http://127.0.0.1:8000/hello/'
headers = {'Authorization': 'Token 9054f7aa9305e012b3c2300408c3dfdf390fcddf'}
r = requests.get(url, headers=headers)
```

* Request Token using http python module

```bash
http post http://127.0.0.1:8000/api-token-auth/ username=vitor password=123
```


--------
To see:
* https://www.webforefront.com/django/namedjangourls.html#:~:text=The%20most%20basic%20technique%20to,a%20view%20method%20or%20template.
    * `template_name` in urls.py
    * `name` in urls.py