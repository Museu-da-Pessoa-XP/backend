<<<<<<< HEAD:backend/urls.py
"""back URL Configuration
=======
"""backend URL Configuration
>>>>>>> 6cbaf4b968db735e3f49e59266bd92c9cd525eec:museubackend/museubackend/urls.py

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework.urlpatterns import format_suffix_patterns
from museu import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', views.UserView.as_view()),
    path('historia/', views.HistoriaView.as_view()),
]
<<<<<<< HEAD:backend/urls.py
urlpatterns = format_suffix_patterns(urlpatterns)
=======
urlpatterns = format_suffix_patterns(urlpatterns)
>>>>>>> 6cbaf4b968db735e3f49e59266bd92c9cd525eec:museubackend/museubackend/urls.py
