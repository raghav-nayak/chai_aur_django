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
