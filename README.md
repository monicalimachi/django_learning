# TRY DJANGO
Pyhton 3.9
- Install requirements
```bash
    pip install -r requirements.txt
```
- Helpful commands general to review all  subcommands, example create new project
```bash
    django-admin
    djang-admin createproject nameproject .
```
- Commands to run server
```bash
    python manage.py runserver
    python manage.py migrate
    python manage.py createsuperuser
    User:
    Password:
```
Install app components, all needed
```bash
    python manage.py startapp products
    python manage.py startapp blog 
    python manage.py startapp pages ...
```

After create and config any app go to settings.py and add own apps 
After any change run:
```bash
    python manage.py makemigrations
    python manage.py migrate
```

- Another option to create products object in the Python Shell 
    (Go to the root of the python projects)
```bash
    python manage.py shell
    > from products.models import Product
    > Product.objects.all()
    > Product.objects.create(title='New Product2', description='another one', price='19.312', summary='sweet')
```
Displays the objects created
```bash
    Product.objects.all()
```
- Review the type of fields django supports:
https://docs.djangoproject.com/en/4.0/ref/models/fields/




