Django is a **high-level web framework** written in Python. That means it's a toolkit for web developers that lets them build websites faster and easier. Here are some of the reasons why Django is popular:

- **Rapid development:** Django provides pre-built components and tools that handle common web development tasks. This saves developers time and effort compared to starting from scratch.
- **Security:** Django is designed with security in mind and helps developers avoid common security vulnerabilities.
- **Scalability:** Django can be used to build websites of all sizes, from small personal blogs to large enterprise applications.
- **Maintainability:** Django code is well-organized and easy to understand, which makes it easier for developers to maintain and update websites over time.

Here are some of the types of websites that can be built with Django:

- Content management systems (CMS)
- Social networking sites
- E-commerce websites
- Data analysis tools
- And many more!

Why Django?
- ridiculously fast
- reassuringly secure
- exceedingly scalable

#### to create virtual environment and install packages
we are going to use uv(https://pypi.org/project/uv/). An extremely fast Python package installer and resolver, written in Rust. Designed as a drop-in replacement for common `pip` and `pip-tools` workflows.

```sh
$ brew install uv

$ uv venv

$ $ tree .venv
.venv
├── CACHEDIR.TAG
├── bin
│   ├── activate
│   ├── activate.bat
│   ├── activate.csh
│   ├── activate.fish
│   ├── activate.nu
│   ├── activate.ps1
│   ├── activate_this.py
│   ├── deactivate.bat
│   ├── pydoc.bat
│   ├── python -> /usr/local/Cellar/python@3.12/3.12.3/Frameworks/Python.framework/Versions/3.12/bin/python3.12
│   ├── python3 -> python
│   └── python3.12 -> python
├── lib
│   └── python3.12
│       └── site-packages
│           ├── _virtualenv.pth
│           └── _virtualenv.py
└── pyvenv.cfg

4 directories, 16 files

$ source .venv/bin/activate
```

```sh
$ uv pip install Django
Resolved 3 packages in 143ms
Downloaded 3 packages in 1.07s
Installed 3 packages in 167ms
 + asgiref==3.8.1
 + django==5.0.6
 + sqlparse==0.5.0
```


#### Creating a Django project
Two main commands with `djangoadmin`
- `django-admin startproject`
- `django-admin startapp`

```sh
$ django-admin startproject django_project

$ tree django_project
django_project
├── django_project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

1 directory, 6 files
```

```sh
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
May 14, 2024 - 16:47:42
Django version 5.0.6, using settings 'django_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

As you can see, the default port is 8000 used for running the application. If you want to specify a particular port, you need to specify the port number at the end of the command.
```sh
$ python manage.py runserver 8001
```

The `runserver` command creates `db.sqlite3` file. It is the default db.

#### file structure

As you can see `django_project` has a project called `django_project` folder within it.
`manage.py` is the entry point of the project. This file is at root level of the project. 

```sh
$ tree django_project
django_project
├── db.sqlite3
├── django_project
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── settings.cpython-312.pyc
│   │   ├── urls.cpython-312.pyc
│   │   └── wsgi.cpython-312.pyc
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```


`django_project/settings.py` -> is the settings file which contains different values like
- BASE_DIR
- SECRET_KEY
- ALLOWED_HOSTS
- INSTALLED_APPS
- MIDDLEWARE
- ROOT_URLCONF
- TEMPLATES
- WSGI_APPLICATION
- DATABASES
- AUTH_PASSWORD_VALIDATORS
- LANGUAGE_CODE
- TIME_ZONE
- USE_I18N
- USE_TZ
- STATIC_URL
- DEFAULT_AUTO_FIELD


Another important file is `urls.py` which stores all the routing in the project.
