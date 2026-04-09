I read the Django design philosophy in [documentation](https://docs.djangoproject.com/es/6.0/misc/design-philosophies/)

# Views
- views.py: here are all the views (like Controller from MVC model)
- use the `render()` buil-in function to render a template.
- `render()` has a request (HttpRequest), template_name (string) and context (dict).
- `render()` returns a HttpResponse object.

# Django Template Language (DTL)
use {{}} to display variables
use {% %} to execute statements

# Django Templates

Make a template and use {% block %}{% endblock %} to create blocks.
Also create a layout folder and put a base.html file in it. Then use {% extends "./layout/base.html" %} to extend the base.html file.

# Common folders
- templates/
  - layout/
  - partial/
- static/
  - css/
  - images/

# Django built-in templates and filters
- length
- date
- upper
- block
- url
- now 'l, d F Y'
- there is a lot more in [documentation](https://docs.djangoproject.com/en/6.0/ref/templates/builtins/)