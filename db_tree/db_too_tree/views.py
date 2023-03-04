from django.shortcuts import render


def index(request, title):
    return render(
        request,
        'index.html',
        {'title': title}
    )
