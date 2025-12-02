from django.shortcuts import render

# Create your views here.

def home(request):
    """
    Renders the home page of the website.
    **Template:**
    :template:`home/home.html`
    """
    return render(request, "home/home.html")
