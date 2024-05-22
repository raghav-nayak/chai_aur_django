article: https://chaicode.com/blogs/how-to-add-tailwind-to-your-django-project-and-django-admin

Django tailwind package : https://pypi.org/project/django-tailwind/

```sh
$ uv pip install django-tailwind
Resolved 4 packages in 445ms
Downloaded 1 package in 22ms
Installed 1 package in 4ms
 + django-tailwind==3.8.0

$ uv pip install 'django-tailwind[reload]'
Audited 1 package in 10ms

-- upgrade pip
$ python -m ensurepip --upgrade
Looking in links: /var/folders/yg/bsj5xd9x39z3rtq5sh6dmcgm0000gn/T/tmpl35hscin
Processing /var/folders/yg/bsj5xd9x39z3rtq5sh6dmcgm0000gn/T/tmpl35hscin/pip-24.0-py3-none-any.whl
Installing collected packages: pip
Successfully installed pip-24.0

$ python -m pip install --upgrade pip
Requirement already satisfied: pip in ./.venv/lib/python3.12/site-packages (24.0)

$ python -m pip install 'django-tailwind[reload]'
Requirement already satisfied: django-tailwind[reload] in ./.venv/lib/python3.12/site-packages (3.8.0)
Requirement already satisfied: django>=3.2.14 in ./.venv/lib/python3.12/site-packages (from django-tailwind[reload]) (5.0.6)
Collecting django-browser-reload<2.0.0,>=1.12.1 (from django-tailwind[reload])
  Downloading django_browser_reload-1.12.1-py3-none-any.whl.metadata (9.8 kB)
Requirement already satisfied: asgiref<4,>=3.7.0 in ./.venv/lib/python3.12/site-packages (from django>=3.2.14->django-tailwind[reload]) (3.8.1)
Requirement already satisfied: sqlparse>=0.3.1 in ./.venv/lib/python3.12/site-packages (from django>=3.2.14->django-tailwind[reload]) (0.5.0)
Downloading django_browser_reload-1.12.1-py3-none-any.whl (12 kB)
Installing collected packages: django-browser-reload
Successfully installed django-browser-reload-1.12.1
```

add app in the `settings.py`
```python
INSTALLED_APPS = [
    ...
    "tailwind",
]
```

```sh
$ python manage.py tailwind init
Cookiecutter is not found, installing...
...
Successfully installed Jinja2-3.1.4 MarkupSafe-2.1.5 arrow-1.3.0 binaryornot-0.4.4 certifi-2024.2.2 chardet-5.2.0 charset-normalizer-3.3.2 click-8.1.7 cookiecutter-2.6.0 idna-3.7 markdown-it-py-3.0.0 mdurl-0.1.2 pygments-2.18.0 python-dateutil-2.9.0.post0 python-slugify-8.0.4 pyyaml-6.0.1 requests-2.31.0 rich-13.7.1 six-1.16.0 text-unidecode-1.3 types-python-dateutil-2.9.0.20240316 urllib3-2.2.1
  [1/1] app_name (theme):
Tailwind application 'theme' has been successfully created. Please add 'theme' to INSTALLED_APPS in settings.py, then run the following command to install Tailwind CSS dependencies: `python manage.py tailwind install`
```

you will see `theme`(default) folder

add tailwind app `theme` in the `settings.py`
```python
INSTALLED_APPS = [
    ...
    "tailwind",
    "theme",
]

TAILWIND_APP_NAME = "theme"

INTERNAL_IPS = ["127.0.0.1"]
```

Now, we can install the tailwind app
```sh
$ python manage.py tailwind install

added 124 packages, and audited 125 packages in 23s

31 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
npm notice
npm notice New minor version of npm available! 10.4.0 -> 10.8.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v10.8.0
npm notice Run npm install -g npm@10.8.0 to update!
npm notice
```

#### To automatically reload when there is any changes in tailwind, we need to do the following things.

we need to start the tailwind app by running it in parallel
`$ python manage.py tailwind start`
For production, use `build` instead of `start`


in `settings.py` file
	add `NPM_BIN_PATH = "/usr/local/bin/npm"`
	under INSTALLED_APPS, add `"django_browser_reload"`
	under MIDDLEWARE, add `"django_browser_reload.middleware.BrowserReloadMiddleware"`

in `urls.py` file
	add `path("__reload__", include("django_browser_reload.urls"))` under `urlpatterns`


#### Admin panel
When you run `runserver` command, you see unapplied migration(s) error.
```shell
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
May 21, 2024 - 18:12:30
Django version 5.0.6, using settings 'django_project.settings'
```

to apply migration, 
```shell
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```


This is important to run admin panel.

```shell
$ python manage.py createsuperuser
Username (leave blank to use 'raghavnayak'): raghav
Email address:
Password:
Password (again):
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

To access admin panel, you need to use 
http://127.0.0.1:8000/admin

you can create non-admin users or groups in the admin panel.


if you want to reset the admin password
`python manage.py changepassword <user_name>`

```shell
$ python manage.py changepassword raghav
Changing password for user 'raghav'
Password:
Password (again):
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
Password:
Password (again):
Passwords do not match. Please try again.
Password:
Password (again):
Passwords do not match. Please try again.
CommandError: Aborting password change for user 'raghav' after 3 attempts
```

