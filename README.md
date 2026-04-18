### PostgreSQL connection

You must have installed PostgreSQL and created a database.
Then, change the sqlite engine in settings to postgresql engine.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

Execute: `python manage.py migrate`
Look at the database and see the tables.

> Obviously you must have created a ``.env`` file with the database credentials. But in this case isn't important.