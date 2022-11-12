from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # previous login view
   
    path('', views.dashboard, name='dashboard'), # dashboard 需要 login 成功
    #path('', include('django.contrib.auth.urls')),
    # view by self
    path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add_value/', views.add_value, name='add_value'),
]
