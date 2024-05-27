from django.shortcuts import render

# Create your views here.


def index(request):
    context = {}
    return render(request, "folio/index.html", context)

def home(request):
    return render(request, "folio/home.html", {})

def services(request):
    return render(request, "folio/services.html", {})

def portfolio(request):
    return render(request, "folio/portfolio.html", {})

def journal(request):
    return render(request, "folio/journal.html", {})

def about(request):
    return render(request, "folio/about.html", {})

def contact(request):
    return render(request, "folio/contact.html", {})

def blog_single(request):
    return render(request, "folio/blog-single.html", {})

def browse(request):
    #return render(request, "folio/catalogue/browse.html", {})
    return render(request, "catalogue/browse.html", {})

