from django.shortcuts import render

from .models import CustomUser


def information_about_all_users(request):
    users = list(CustomUser.objects.all())

    context = {'orders': users}
    return render(request, 'producer_consumer/page.html', context)
