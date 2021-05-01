from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pizza, Topping, Comment
from .forms import PizzaForm, ToppingForm, CommentForm
from django.http import Http404
# Create your views here.

def index(request):
    ''' The home page for Pizzeria '''
    return render(request, 'pizzas/index.html')

@login_required
def pizzas(request):
    pizzas = Pizza.objects.filter(owner=request.user).order_by('date_added')
    context = {'pizzas':pizzas}
    return render(request, 'pizzas/pizzas.html', context)

@login_required
def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('-date_added')
    if pizza.owner != request.user:
        raise Http404
    context = {'pizza':pizza, 'toppings':toppings}
    return render(request, 'pizzas/pizza.html', context)

@login_required
def new_pizza(request):
    if request.method != 'POST':
        form = PizzaForm()
    else:
        form = PizzaForm(data=request.POST)
        if form.is_valid():
            new_pizza = form.save(commit=False)
            new_pizza.owner = request.user
            new_pizza.save()
            
            return redirect('pizzas:pizzas')
    context = {'form':form}
    return render(request, 'pizzas/new_pizza.html', context)

@login_required
def new_topping(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if pizza.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = ToppingForm()
    else:
        form = ToppingForm(data=request.POST)
        if form.is_valid():
            new_topping = form.save(commit=False)
            new_topping.pizza = pizza
            new_topping.save()
            return redirect('pizzas:pizza', pizza_id=pizza_id)
    context = {'form':form, 'pizza':pizza}  #passing pizza because we want to see the pizza, not the number that represents its id
    return render(request, 'pizzas/new_topping.html', context)

@login_required
def edit_topping(request,topping_id):
    topping = Topping.objects.get(id=topping_id)
    pizza = topping.pizza
    if pizza.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = ToppingForm(instance=topping)
    else:
        form = ToppingForm(instance=topping, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:pizza',pizza_id=pizza.id)
    context = {'topping':topping, 'pizza':pizza, 'form':form}
    return render(request, 'pizzas/edit_topping.html', context)

@login_required
def comments(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    comments = Comment.object.filter(id=pizza_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.pizza = pizza
            comments.owner = request.user
            comments.save()
            return redirect('pizzas:pizza',pizza_id=pizza_id)
    context = {'pizza':pizza, 'comments':comments}
    return render(request, 'pizzas/comments.html', context) 

    '''
    if request.method == 'POST' and request.POST.get("btn1"):
        comment = request.POST.get("comment")
        Comment.objects.create(pizza_id=pizza_id,name=comment,date_added=date.today())
    comments = Comment.object.filter(pizza=pizza_id)
    pizza = Pizza.objects.get(id=pizza_id)

    context = {'pizza':pizza, 'comments':comments}
    return render(request, 'pizzas/comments.html', context)
    '''



