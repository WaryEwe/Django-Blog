from django.shortcuts import render, redirect


def home_view(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None

    context = {
        'username':username,
    }
    return render(request, 'home.html', context)