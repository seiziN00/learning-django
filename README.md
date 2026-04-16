I think import from the current directory in better than just importing from a `.` like:

```python
from . import views

urlpatters = [
  path('', views.root, name='root)
]
```

I think it's more explicit and easier to read. What do you think?

```python
from querydict import views

urlpatterns = [
    path('', views.root, name='root'),
]
```