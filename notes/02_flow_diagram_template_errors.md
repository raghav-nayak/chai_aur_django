
### Flow diagram
![[django_flow.excalidraw]]


`views.py` is not created by default. So, we need to create it.
You can directly return HttpResponse or render a template.

`views.py`
```python
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("You are at home page") 
    return render(request, "website/index.html")


def about(request):
    return HttpResponse("You are at about page")


def contact(request):
    return HttpResponse("You are at contact page")
```


we are going to create two more directories at root level.
- `static` -> css, js files
- `templates` -> html files

you have to tell which the templates directory to be used in Django. So, you need to update templates dir in `settings.py` file.

This does not work
`<link rel="stylesheet" href="../../static/style.css">`
To include styling sheet files, we need to use templating engine.
You need to use 
```django
{% load static %}
<!DOCTYPE html>
<html>
<head>
...
	<link rel="stylesheet" href="{% static "style.css" %}">
...
```

And also, we need to add this line in the `settings.py`
`STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]`
