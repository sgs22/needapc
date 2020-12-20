from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

"""
Not currently being used,

render accounts page and register page
"""
@login_required
def accounts(request):
    return render(request, 'accounts/accounts.html')

class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
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
