1
    ```shell
    django-admin startproject my_project
    cd my_project
    python manage.py startapp users
    ```
2
    # Add `users` to the `INSTALLED_APPS` in `my_project/my_project/settings.py`

    ```python
    INSTALLED_APPS = [
        "users",
        # ...,
    ]
    ```
3
    ```shell
    python manage.py migrate
    python manage.py runserver
    ```
4
    # So that we should not need to set up a strong password everytime, we will comment out password validators in `my_project/my_project/settings.py`

    ```python
    AUTH_PASSWORD_VALIDATORS = [
        # {
        #     "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        # },
        # {
        #     "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        # },
        # {
        #     "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        # },
        # {
        #     "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        # },
    ]
    ```
5
    # Create a admin user

    ```shell
    python manage.py createsuperuser
    ```
6




    # Create a base template called `base.html` in `users/templates/`:

    ```html
    <h1>Welcome to Awesome Website</h1>
    {% block content %} {% endblock %}
    ```
7

    # create another template `users/templates/dashboard.html`:

    ```html
    {% extends 'base.html' %} {% block content %} Hello, {{ user.username |
    default:'Guest' }}! {% endblock %}
    ```
8
    # Set up views for the template to work:

    ```python
    from django.shortcuts import render

    def dashboard(request):
        return render(request, "dashboard.html")
    ```
9

    # Create a `users/urls.py` and add the following:

    ```python
    from django.conf.urls import url
    from users.views import dashboard

    urlpatterns = [
        url(r"^dashboard/", dashboard, name="dashboard"),
    ]
    ```
10

    #   Now, add the application's URL to the main project's URL

    ```python
    from django.conf.urls import include, url
    from django.contrib import admin

    urlpatterns = [
        url(r"^", include("users.urls")),
        url(r"^admin/", admin.site.urls),
    ]
    ```
11



    # Add the URLs provided by the Django authentication system in `users/urls.py`:

    ```python
    from django.conf.urls import include, url
    # from ...

    urlpatterns = [
        url(r"^accounts/", include("django.contrib.auth.urls")),
        url(r"^dashboard/", dashboard, name="dashboard"),
    ]
    ```
12

    # For login page, Django will try to use a template called `registration/login.html`.
    # So, create the file `users/templates/registration/login.html`

    ```html
    {% extends 'base.html' %} {% block content %}
    <h2>Login</h2>

    <form method="post">
      {% csrf_token %} {{ form.as_p }}
      <input type="submit" value="Login" />
    </form>

    <a href="{% url 'dashboard' %}">Back to dashboard</a>
    {% endblock %}
    ```
13
    # Add some more CSS to improve the looks of `users/templates/base.html`:

    ```html
    <style>
      label,
      input {
        display: block;
      }
      span.helptext {
        display: none;
      }
    </style>

    <h1>Welcome to Awesome Website</h1>
    <!-- ... -->
    ```
14
    # Let's define another redirect url. In `my_project/settings.py` add the following at the end:

    ```python
    LOGIN_REDIRECT_URL = "dashboard"
    ```
15

    ```python
    LOGOUT_REDIRECT_URL = "dashboard"
    ```
16
    # Let's add logout link to the dashboard and a link to login as well.
    In `users/templates/users/dashboard.html` add:

    ```html
    {% extends 'base.html' %} {% block content %} Hello, {{ user.username | default:
    'Guest' }}!

    <div>
      {% if user.is_authenticated %}
      <a href="{% url 'logout' %}">Logout</a>
      {% else %}
      <a href="{% url 'login' %}">Login</a> {% endif %}
    </div>
    {% endblock %}
    ```
