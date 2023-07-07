
# Startproject

```shell
django-admin startproject django_project .
```

Assumes PG has already been set. Otherwise wait.

```shell
python manage.py makemigrations [app]	# [app] is optional
python manage.py migrate				# Run all staged migrations

```

# Create App

To create and add an app to the project FOUR things must be done.

## Create the app

Here we create an app called `pages`, which will hold static html.

```shell
python manage.py startapp pages
```

## Add app to PROJECT settings.py

```shell
# django_project/settings.py

INSTALLED_APPS = [
	"django.contrib.admin",
	"django.contrib.auth",
	"django.contrib.contenttypes",
	"django.contrib.sessions",
	"django.contrib.messages",
	"django.contrib.staticfiles",
	# Local
	"pages.apps.PagesConfig", 				# new
]
```

## Update PROJECT urls.py to include APP urls

```shell
# django_project/urls.py

from django.contrib import admin
from django.urls import path, include
urlpatterns = [
	path("admin/", admin.site.urls),
	path("", include("pages.urls")),		# new
]
```

## Create APP urls.py

```shell
#app/urls.py

from django.urls import path
from .views import home_page_view

urlpatterns = [
	path("", home_page_view, name="home")	# new
]
```

## Update APP models.py (optional)

```shell
#app/models.py

class HomePage(models.Model):				# new
	pass
```

## Update APP views.py

```shell
#app/views.py

from .models import HomePage  				# new

class HomePageListView(ListView):			# new
    model = HomePage
    context_object_name = "home_list"
    template_name = "static/html/home_list.html"
```

## Create APP templates (optional)

Update project settings.py

```shell
#django_project/settings.py

TEMPLATES = [
	{
		...
		"DIRS": [BASE_DIR / "templates"],	# new
		...
	}
]
```

```shell
mkdir templates
touch templates/_base.html templates/home.html
```

## Write APP

# Create Superuser

```shell
python manage.py createsuperuser
```

# Collect Static

run the command python manage.py collectstatic which will combine all static
files into a new staticfiles directory.

```shell
$ docker-compose exec web python manage.py collectstatic
131 static files copied to '/code/staticfiles'.
```

This will create a staticfiles directory with four subdirectories:
admin, css, images, and js. The first one is the static assets of the Django admin app and the other three we specified. That’s why there are 122 files copied over.

# Run tests

```shell
python manage.py test
```
