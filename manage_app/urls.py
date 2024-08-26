"""
URL configuration for emp_manage_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from ..emp_manage_proj import views
# from .views.all_emp.views import all_emp
from .import views



urlpatterns = [
    path('', views.index, name ='index'),
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('contact_us',views.contact_us_view,name='contact_us'),
    path('about_us',views.about_us_view,name='about_us'),
    path('create_emp', views.create_emp, name ='create_emp'),
    path('remove_emp/<int:emp_id>', views.remove_emp, name ='remove_emp'),
    path('update_emp/<int:emp_id>', views.update_emp, name ='update_emp'),
    path('do_update_emp/<int:emp_id>', views.do_update_emp, name ='do_update_emp'),

    path('all_emp',views.all_emp , name ='all_emp'),
]
