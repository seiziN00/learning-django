from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages


def form(request):
  return render(request, 'index.html', {})


def goal(request):
  if request.method == 'GET':
    name = request.GET.get('name', 'Guest')
    message = request.GET.get('message', 'No message provided.')
    return render(request, 'success.html', {'name': name, 'message': message})


  if request.method == 'POST':
    name = request.POST.get('name', '')
    quantity = request.POST.get('quantity', '0')

    # Validation
    errors = []
    if not name or len(name) < 3:
      errors.append("The name must be at least 3 characters long.")
    try:
      quantity = int(quantity)
      if quantity <= 0:
        errors.append("Quantity must be greater than zero.")
    except (ValueError, TypeError):
      errors.append("Quantity must be a valid number.")

    if errors:
      for error in errors:
        messages.error(request, error)
      return render(request, 'index.html')

    return render(request, 'success.html', {'name': name, 'quantity': quantity})

  else:
    messages.error(request, "Invalid request method.")