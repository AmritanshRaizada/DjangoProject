"""
URL configuration for myproject project.

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
from myapp.views import student_list, home,student_detail, student_create, student_update, student_delete,teacher_detail



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('student/<int:id>/', student_detail, name='student-detail'),
    path('student/create/', student_create, name='student-create'),
    path('student/<int:id>/update/', student_update, name='student-update'),
    path('student/<int:id>/delete/', student_delete, name='student-delete'),
    path('teacher/<int:id>/', teacher_detail, name='teacher-detail')

]
