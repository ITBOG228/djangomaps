from django.shortcuts import render


def default_map(request):
    return render(request, 'default.html', {})
