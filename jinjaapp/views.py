from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about us.html")

def gallery(request):
    return render(request, "gallery.html")


