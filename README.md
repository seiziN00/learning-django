Each model in Django apps is represented by a class that subclasses django.db.models.Model. Each attribute of the model represents a database field.

### Some of the commonly used field types are:

1. ``CharField``: is a VARCHAR.
2. ``TextField``: is a TEXT.
3. ``IntegerField``: is an INTEGER.
4. ``FloatField``: is a FLOAT. Good for measure, but not for money.
5. ``DecimalField``: is a DECIMAL. Good for money.
5. ``DateField``: is a DATE. It uses Python's datetime.date to store the date.
TimeField is a TIME. It uses Python's datetime.time to store the time.
7. ``DateTimeField``: is a DATETIME. It uses Python's datetime.datetime to store the date and time. To create a record with the current date and time, use **auto_now_add=True**. To update the record with the current date and time, use **auto_now=True**.
8. ``BooleanField``: is a BOOLEAN. It allows three states: True, False and None (NULL).
9. ``ForeignKey``: is a INTEGER with a foreign key constraint.
10. ``OneToOneField``: is a INTEGER with a one-to-one constraint. Useful to extend a model.
11. ``ManyToManyField``: is a INTEGER with a many-to-many constraint. Creates a intermediate table.
12. ``FileField``: is a VARCHAR with a file upload validator. Stores the path in the DB and the file in the MEDIA_ROOT directory (or in the cloud like S3).
13. ``ImageField``: is a VARCHAR with an image upload validator. Inherits from FileField.
14. ``EmailField``: is a VARCHAR with an email validator.
15. ``URLField``: is a VARCHAR with a URL validator.
16. ``UUIDField``: is a VARCHAR with a UUID validator.
SlugField: is a VARCHAR with a slug validator. Useful for clean URLs.
17. ``BinaryField``: is a BLOB.
18. ``DurationField``: is a BIGINT.
19. ``GenericIPAddressField``: is a VARCHAR with an IP address validator.
20. ``IPAddressField``: is a VARCHAR with an IP address validator.
21. ``PositiveIntegerField``: is a INTEGER with a positive validator.

There are more in the [official documentation](https://docs.djangoproject.com/en/6.0/ref/models/fields/)

Some key tips:
- `null=True` and `blank=True` are different. `null=True` means that the field can be NULL in the database. `blank=True` means that the field can be empty in the form.
- `default` is used to set a default value for the field. It can be a value or a callable.
- `editable=False` means that the field is not editable in the admin.
- `unique=True` means that the field must be unique in the database.
- `on_delete` is used to set the behavior when the referenced object is deleted. It can be `CASCADE`, `PROTECT`, `SET_NULL`, `SET_DEFAULT`, `SET()`, `DO_NOTHING`.

For PostgreSQL there are more fields like `ArrayField` or `JSONField`.

To show migrations state: ```python manage.py showmigrations <app_name>```

---

The ``urls.py`` file must be created in the app folder. It is used to define the URLs of the app. It is similar to the ``urls.py`` file in the project folder, but it is specific to the app.

The class name must be in singular and in capital letters. The table name is in lowercase and plural.

### Save data in a database

There are two forms to save data:
- comment = Comment(parameters) and then comment.save()
- comment = Comment.objects.create(parameters)

The second option is the best one. It is more concise and it is more efficient, also returns a the saved object with the id.

### Delete data in a database

- comment = Comment.objects.get(id=1)
- comment.delete()

or with a filter:
- Comment.objects.filter(id=1).delete()
