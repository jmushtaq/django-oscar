from django.shortcuts import render

# Create your views here.


def index(request):
    context = {}
    return render(request, "assets/index.html", context)

def home(request):
    return render(request, "assets/home.html", {})

def services(request):
    return render(request, "assets/services.html", {})

def portassets(request):
    return render(request, "assets/portassets.html", {})

def journal(request):
    return render(request, "assets/journal.html", {})

def about(request):
    return render(request, "assets/about.html", {})

def contact(request):
    return render(request, "assets/contact.html", {})

def blog_single(request):
    return render(request, "assets/blog-single.html", {})

def browse(request):
    #return render(request, "assets/catalogue/browse.html", {})
    return render(request, "catalogue/browse.html", {})

def index2(request):
    return render(request, "assets/index2.html", {})

