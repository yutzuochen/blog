from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# from django.contrib import messages
from .forms import LoginForm
# from .models import Profile
from django.contrib.auth.decorators import login_required
# from django import template
# from ..blog.models import Post

# register = template.Library()

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})




@login_required
def dashboard(request):
    user_point = request.user.point
    print("user_point in dashboard: ", user_point)
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard',
                    'user_point':user_point})

@login_required
def add_value(request):
    bank_value = request.user.point
    bank_account = "4005216588"
    return render(request,
                  'account/add_value.html',
                  {'bank_account':bank_account,'bank_value':bank_value})

# @register.simple_tag
# def total_posts():
#     return Post.published.count()