"""midterm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
    path("api/students", views.get_students, name="get_students")
]

from django.urls import path
from . import views

urlpatterns = [
    path("api/students", views.create_student, name="create_student")
]

from django.urls import path
from . import views
  
urlpatterns = [
      path("api/students/<int:id>", views.get_student, name="get_student")
]

from django.urls import path
from . import views
  
urlpatterns = [
      path("api/students/<int:id>", views.get_student, name="get_student")
]

from django.urls import path
from . import views
  
urlpatterns = [
    path("api/students/<int:id>", views.update_student, name="update_student")
]

urlpatterns = [
    path("api/students/<int:id>", views.delete_student, name="delete_student")
]