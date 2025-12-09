from django.shortcuts import render, redirect
from .forms import CustomSignupForm

# Create your views here.

def home(request):
    """
    Renders the home page of the website.
    **Template:**
    :template:`home/home.html`
    """
    return render(request, "home/home.html")

def signup_view(request):
    """
    Handles user signup using a custom signup form.
    **Template:**
    :template:`/signup.html`
    """
    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            # Process form data, e.g., create user
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password']
            return redirect('success_page')
    else:
        form = CustomSignupForm()
    
    return render(request, "likeminds/templates/account/signup.html", {"form": form})
