There is a third-package called django-seed, which can be used to populate the database with dummy data.

So, install with `uv add django-seed`, it will install the package and its dependencies and add it to the `pyproject.toml` file.
Also you've noticed that is missing the `psycopg2` package, even if you're not using PostgreSQL.

---

To get data use `objects.all()` and to get offset and limit use `objects.all()[offset:limit]`.
To get a single object use `objects.get(id=1)`.
To filter objects use `objects.filter(name__contains="John")`.