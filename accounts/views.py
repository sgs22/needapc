from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from quiz.models import UserResponse


from .forms import (
    LoginForm,
    RegisterForm
)
# Create your views here.
def logout_view(request):
    logout(request)
    return redirect("/")

'''
    TODO: add validation error for incorrect user input for feedback for the user rather than just refreshing the page.
    
'''
def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        # verify valid username and password
        user = authenticate(username=username, password=password)
        if user == None:
            print("Invalid User!")
            # raise form.ValidationError(_('User is invalid'), code='invalid')
            # later add message
            return redirect("/login")
        # perform login
        login(request, user)

        # redirect to a logged in required page
        return redirect("/")

    return render(request, "accounts/login.html", {"form":form})

'''
    This is no longer active as newer form offers AJAX, still using old 'RegisterForm'
'''
def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user_obj.is_active = False
        user_obj.save()
        user_obj.set_password(password)
        user_obj.save()
        # send email confirmation
        return redirect("/login")
    return render(request, "accounts/register.html", {"form": form})



"""
    Current Register form view in use,
    render accounts page and register page

    BUG: When registering user it doesnt register a password just leaves blank?
    MAY HAVE TO SWITCH TO OLD FORM WITH AJAX FOR NOW
    
"""
@login_required
def accounts(request):
    return render(request, 'accounts/accounts.html')

class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = RegisterForm
    success_url = reverse_lazy('accounts')

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


"""
    Checks if the username has already been used in the database
    returns response if taken else will register
"""
def validate_username(request):
    """Check username availability"""
    username = request.GET.get('username', None)
    response = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)

"""
    Checks if the email has already been used in the database
    returns response if taken else will register
"""
def validate_email(request):
    """Check email availability"""
    email = request.GET.get('email', None)
    response = {
        'is_taken': User.objects.filter(email__iexact=email).exists()
    }
    return JsonResponse(response)




