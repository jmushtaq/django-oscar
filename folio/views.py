from django.shortcuts import render

# Create your views here.


def index(request):
    context = {}
    return render(request, "folio/index.html", context)

def blog_single(request):
    context = {}
    return render(request, "folio/blog-single.html", context)

