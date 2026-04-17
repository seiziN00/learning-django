To order data use `objects.all().order_by('data')`

To make custom filters use double underscore `__` between field and filter name. For example, to filter by date greater than `2020-01-01` use `objects.all().filter(data__gt='2020-01-01')`

#### Most common lookups:
- `__gt` - greater than
- `__gte` - greater than or equal
- `__lt` - less than
- `__lte` - less than or equal
- `__exact` - exact match
- `__iexact` - exact match case insensitive
- `__contains` - contains
- `__icontains` - contains case insensitive
- `__startswith` - starts with
- `__istartswith` - starts with case insensitive
- `__endswith` - ends with
- `__iendswith` - ends with case insensitive
- `__in` - in list
- `__range` - in range
- `__isnull` - is null
- `__regex` - regex match
- `__iregex` - regex match case insensitive
- `__year` - specific year


By default Django uses `AND` operator. To use `OR` operator use `Q` objects. For example:

```python
from django.db.models import Q

Products.objects.filter(
    Q(name__icontains="laptop") | Q(price__lt=10)
)
```

There's a complete lookups in the [documentation](https://docs.djangoproject.com/en/6.0/topics/db/queries/#field-lookups)

---

To update data just reasign the field and save the object. For example:

```python
product = Products.objects.get(id=1)
product.name = "New name"
product.save()
```