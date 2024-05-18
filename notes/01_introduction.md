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

#### Advantages
Django has several advantages over other web frameworks, here are some of the key ones:

- **Batteries-Included:** Unlike some other frameworks that are more minimal, Django boasts a "batteries-included" philosophy. This means it comes with a wide range of built-in features out of the box, like user authentication, templating, and an admin panel. This saves developers time and effort as they don't need to find or implement these functionalities from scratch.
    
- **Python:** Django is built on Python, a popular general-purpose programming language known for its readability and beginner-friendly syntax. This makes Django itself easier to learn and use, especially for developers who are already familiar with Python.
    
- **Security:** Django prioritizes security and offers built-in features to guard against common web vulnerabilities like SQL injection and cross-site scripting (XSS) attacks. This helps developers build secure applications without needing to be experts in web security.
    
- **Scalability:** Django applications can be scaled to handle large amounts of traffic or data. This is achieved through features like database abstraction and the ability to distribute the application across multiple servers.
    
- **Large Community & Resources:** Django has a vast and active community of developers. This means there's a wealth of online resources, tutorials, and forums available for help and learning. Additionally, there's a larger pool of Django developers to hire from if needed.
    
- **Versatility:** Django is suitable for building a wide range of web applications, from simple blogs to complex social networking sites and e-commerce platforms. Its flexibility allows it to adapt to various project needs.
    

It's important to note that Django might not be the best choice for every project. For instance, if you're building a very small and simple website, a more lightweight framework might be a better option. However, for many web development projects, Django's advantages make it a compelling choice.

#### Drawbacks
Django is a powerful tool but it does have some drawbacks to consider:

- **Learning Curve:** While Django is known for being beginner-friendly compared to lower-level frameworks, its structure and "batteries-included" approach can have a steeper learning curve for those new to web development or Python itself. The range of features can be overwhelming at first.
    
- **Monolithic Structure:** Django enforces a particular way of structuring your project. This can be helpful for organization but also limits flexibility. If you need a highly customized architecture, Django's opinionated approach might be restrictive.
    
- **Overhead:** Django's extensive features come with some overhead. It can be more resource-intensive than minimal frameworks, potentially leading to slower performance for very simple websites.
    
- **Not Ideal for Microtasks:** Django excels at building complex web applications. For smaller projects or API-driven applications, a more lightweight framework might be a better fit.
    
- **Tight Coupling:** Django components can be tightly coupled, making it more challenging to swap out specific functionalities or integrate with external libraries.
    
- **Security Reliance:** While Django offers built-in security features, it's still important for developers to understand security best practices. Over-reliance on the framework can lead to vulnerabilities if not used carefully.
    

Overall, Django is a great choice for many web development projects, but it's wise to be aware of its potential drawbacks to see if it aligns well with your specific needs.


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
