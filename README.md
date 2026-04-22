## Django Forms

Para trabajar con Django Forms se suele crear un archivo `forms.py`.
En este archivo se definen las clases que heredan de `forms.Form`.
El nombre de la clase suele ser el nombre del modelo + la palabra `Form`.

```python
from django import forms

class CommentForm(forms.Form):
  pass
```

Es muy parecido a los modelos de Django.
Algunas formas básicas:

- ``CharField``
- p
- ``URLField``
- ``EmailField``
- ``IntegerField``
- ``FloatField``
- ``BooleanField``
- ``DateField``
- ``TimeField``
- ``DateTimeField``
- ``ChoiceField``
- ``MultipleChoiceField``
- ``FileField``
- ``ImageField``

Muchos contienen parámetros como ``max_length``, ``min_length``, ``required``, ``widget``, ``label``, ``initial``.

Para más información, revisar la [documentación](https://docs.djangoproject.com/en/6.0/topics/forms/#building-a-form-in-django)

Para mostrar el formulario en el template, se puede usar el tag `{{ form }}` o `{{ form.as_p }}` o `{{ form.as_table }}` o `{{ form.as_ul }}`.
Obviamente se le debe pasar el formulario como **contexto** en la vista.

#### Para actualizar la información de un formulario

Algo interesante, es que se puede actualizar la información de un formulario con un diccionario instanciando el formulario.

```python
comment_form = CommentForm({'name': 'Sirius', 'web_page': 'https://www.google.com', 'comment': 'Hola desde Django'})
```