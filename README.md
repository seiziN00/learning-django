Only Django.
This repository is a journey of my Django projects.

### Tools

- Git
- uv
- Obsidian
- Anki
- ChatGPT-5.3
- Gemini 3 Flash
- Qwen3.6-Plus
- NotebookLM

# 60 minutes

Django Documentation Content → [Documentation](https://docs.djangoproject.com/en/6.0/contents/#:~:text=app)

1. I read this post in the official documentation → [FAQ: General](https://docs.djangoproject.com/en/6.0/faq/general/), oh, there is a audio of the pronuntiation: [audio](https://www.red-bean.com/~adrian/django_pronunciation.mp3)
2. Architecture and structure of a Django project
   - Model View template: View is like a Controller. Template is the HTML that is displayed.
3. To create a Django project, run this command:
   ```bash
   django-admin startproject my_project
   ```
4. To create a Django app, run this command:
   ```bash
   python manage.py startapp my_app
   ```
5. Define a function in the `views.py` to return a HttpResponse and show the message "Hello Django!" in the browser.
6. Make a `urls.py` file and add the url to the `views.py` file.
7. To make a url in the root url, just add the url in the `urls.py` file in the root directory of the project.
   ```python
   // from django.url import include
   urlpatterns = [
       path('', include('my_app.urls')),
   ]
   ```
8. To run the Django project, run this command:
   ```bash
   python manage.py runserver
   ```

# Next steps

- [ ] Read the Django's cache framework [documentation](https://docs.djangoproject.com/en/6.0/topics/cache/)
- [ ] Read the Django's design philosophies [documentation](https://docs.djangoproject.com/en/6.0/misc/design-philosophies/)
- [ ]
