from django.http import HttpResponse


def root(request):
  name = request.GET.get('name') or 'world'
  return HttpResponse(f'Hello, {name}!')