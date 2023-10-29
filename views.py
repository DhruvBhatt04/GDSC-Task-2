# orders/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import Order, UserProfile
from .forms import OrderForm

@login_required
def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.creator = request.user
            order.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'add_order.html', {'form': form})

@login_required
def update_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    if request.user == order.creator:
        if request.method == 'POST':
            form = OrderForm(request.POST, instance=order)
            if form.is_valid():
                form.save()
                return redirect('order_list')
        else:
            form = OrderForm(instance=order)
        return render(request, 'update_order.html', {'form': form, 'order': order})
    else:
        # Handle permission denied
        pass

@login_required
def delete_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    if request.user == order.creator:
        order.delete()
    else:
        # Handle permission denied
        pass

@login_required
def order_list(request):
    orders = Order.objects.filter(creator=request.user)
    return render(request, 'order_list.html', {'orders': orders})

@login_required
def search_orders(request):
    if request.method == 'POST':
        priority = request.POST.get('priority')
        orders = Order.objects.filter(creator=request.user, priority=priority)
    else:
        orders = Order.objects.filter(creator=request.user)
    return render(request, 'search_orders.html', {'orders': orders})

# Add views for user profile management, login, and logout as well.
