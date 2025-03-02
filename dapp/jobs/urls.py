from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('create_job/', views.create_job, name='create_job'),
    path('home/', views.home, name='home'),
    path('accounts/logout/', LogoutView.as_view(next_page='register'), name='logout'),
]