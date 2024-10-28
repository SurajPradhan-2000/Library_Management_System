"""
URL configuration for Library_Management_System project.

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
from django.urls import path
from Library import views as lviews
from myadmin import views as aviews

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',lviews.index),
    path('',lviews.home),
    path('a_home',lviews.a_home),
    path('add_book/',lviews.add_book),  
    path('view_books/',lviews.view_books),
    path('view_students',lviews.view_students), 
    path('issue_book',lviews.issue_book), 
    path('admin_login',lviews.admin_login),
    path('student_registration',lviews.student_registration),
    path('student_login',lviews.student_login),
    path('s_home',lviews.s_home),
    path('profile',lviews.profile),
    path('view_issued_books',lviews.view_issued_books),
    path("logout/", lviews.Logout, name="logout"),
    path("edit_profile/", lviews.edit_profile, name="edit_profile"),
     path("change_password/", lviews.change_password, name="change_password"),
    path("delete_book/<int:myid>/", lviews.delete_book, name="delete_book"),
    path("delete_student/<int:myid>/", lviews.delete_student, name="delete_student"),
 

    #myadmin
    
    
     path('admin/', admin.site.urls),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
