### Forms in Django

Hay dos formas de usar los formularios, con HTML o con Django Forms.

La primera forma es simplemente usar HTML puro, entonces creas una carpeta templates con una archivo HTML que contenga un form que luego importas en la vista y renderizas.

En el mejor de los casos para que el código y la estructura del proyecto sea lo más limpia posible, se recomienda crear una carpeta **forms** para los formularios, así solo se usa un `{% include 'forms/contact.html' %}`.

Para validar los datos, se usa una comparación con métodos HTTP, por ejemplo para comparar si no es GET:


```python
if request.method != 'GET':
    # Validar datos
```

Para obtener el valor:

```python
name = request.GET['name']
```