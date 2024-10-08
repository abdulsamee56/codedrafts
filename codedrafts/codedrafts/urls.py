"""
URL configuration for codedrafts project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('bank-management/', views.bank_management, name='bank_management'),
    path('cv/', views.cv_generator, name='cv'),
    path('tracker/', views.macro_tracker, name='macro'),
    path('aboutus/', views.about,name='about'),
    path('projects/', views.projects_view, name='projects'),
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    
]
