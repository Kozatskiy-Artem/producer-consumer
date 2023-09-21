from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from core.containers import ServiceContainer
from .forms import LoginForm


def log_in(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.data['email']
            password = form.data['password']
            user = authenticate(request, email=email, password=password)
            if user and user.check_password(password):
                login(request, user)
                return redirect('orders/')
        context = {'error_message': 'Invalid login credentials', 'form': form}
        return render(request, 'producer_consumer/login.html', context)
    else:
        form = LoginForm()
        context = {'form': form}
        return render(request, 'producer_consumer/login.html', context)


@login_required
def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    return render(request, 'producer_consumer/logout.html')


@login_required
def orders_list(request):
    """Get all orders"""

    service = ServiceContainer.service()
    orders = service.get_orders(request.user.id)
    context = {'orders': orders}

    return render(request, 'producer_consumer/orders.html', context)


@login_required
def delete_order(request, order_id):
    """Delete order by id and return message"""

    service = ServiceContainer.service()

    message = service.delete_order(order_id)

    return render(request, 'producer_consumer/closed_order.html', {'message': message})
