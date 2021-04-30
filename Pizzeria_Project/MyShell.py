import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizzas.models import Pizza, Topping

pizzas = Pizza.objects.all()
toppings = Topping.objects.all()

for p in pizzas:
    print(f"Pizza ID: {p.id}    Pizza: {p}")

for t in toppings:
    print(f"Pizza: {t.pizza}    Topping: {t}")