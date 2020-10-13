from django.urls import path
from museu import views

urlpatterns = [
    path('user/', views.user_list),
    path('historia/', views.historia_list),
    path('upload/', views.upload_list),
]