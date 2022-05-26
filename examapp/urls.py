from django.urls import path

from examapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('login_view/', views.login_view, name='login_view'),

]
