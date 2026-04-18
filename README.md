## Relations in Django

``OneToOneField`` is likely a ``ForeignKey``, but It's used to stores aditional information like a biography or a profile picture for a user. Instead modify the table of users.

So, if you can extend a user, do inheritance multi-table, use ``OneToOneField``.

To make a many to one relationship, use ``ForeignKey`` and the `_set`.

To make a many to many relationship, use ``ManyToManyField``.
It creates an intermediate table to store the relations.
Use the `add()` method to add a new relation.
Use the `remove()` method to remove a relation.

There's more information in the [documentation](https://docs.djangoproject.com/en/6.0/topics/db/examples/)