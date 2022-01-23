"""churn_prediction_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name = 'login'),
    path('login_user/',views.login_user, name = 'login_user'),
    path('post_login/',views.post_login, name = 'post_login'),
    path('post_login_user/',views.post_login_user, name = 'post_login_user'),
    path('post_add_user/',views.post_add_user, name = 'post_add_user'),
    path('logout/',views.logout, name = 'logout'),
    path('dashboard/',views.dashboard, name = 'dashboard'),
    path('customers/',views.customers, name = 'customers'),
    path('manage_users/',views.manage_users, name = 'manage_users'),
    # path('demographics/',views.demographics, name = 'demographics'),
    # path('services/',views.services, name = 'services'),
    # path('result/',views.result, name = 'result'),
    # path('post_get_demographics/',views.post_get_demographics,),
    # path('post_get_services/',views.post_get_services,),
    path('import_customers/',views.import_customers,),
    path('delete_user/',views.delete_user,),
    path('edit_user/',views.edit_user,),
    path('batch_list/',views.batch_list, name="batch_list"),
]

