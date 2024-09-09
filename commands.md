1. python -m venv venv
2. venv\Scripts\activate
3. pip install django
4. pip install --upgrade pip
5. mkdir app_backend
6. cd app_backend
7. django-admin startproject backend .
8. python manage.py runserver
9. python manage.py migrate
10. python manage.py createsuperuser
11. python manage.py startapp core
12. python manage.py makemigrations cart
13. for /r %i in (*.py) do @echo %i | findstr /i /v "__init__.py" && del "%i"
14. for /r %i in (*.pyc) do del "%i"
15. python manage.py dbshell
16. sqlite> .table
17. sqlite> DROP TABLE <table>;

<!-- Go to backend >>> settings.py and add 'core' to the INSTALLED_APPS -->

![alt text](image.png)

18. pip install djoser

<!-- Add 'djoser', 'rest_framework', 'rest_framework.authtoken' to the INSTALLED_APPS in settings.py -->

<!-- Add the below code at the bottom of settings.py -->

<!--
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}
-->

<!-- Go to backend >>> urls.py and import include -->

# from django.urls import path, include

<!-- Add the following code after [path('admin/', admin.site.urls),] in urls.py -->

#    path('auth/', include('djoser.urls')),
#    path('auth/', include('djoser.urls.authtoken')),

19. python manage.py migrate

[
    1. Sign up || http://127.0.0.1:8000/auth/users/
    2. Login || http://127.0.0.1:8000/auth/token/login/
    3. Profile || http://127.0.0.1:8000/auth/users/me/
    4. Set password || http://127.0.0.1:8000/auth/users/set_password/
    5. Set username || http://127.0.0.1:8000/auth/users/set_username/
]

#Creating Categories
20. python manage.py makemigrations [app]
21. python manage.py migrate [app]

22. pip freeze > requirements.txt
23. pip install -r requirements.txt

FashionAdmin
fashion@admin.com
Fashion2002
