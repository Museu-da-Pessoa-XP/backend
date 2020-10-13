from django.urls import path
from museu import views

urlpatterns = [
    path('user/', views.UserDetails.as_view()),
    path('historia/', views.HistoriaDetails.as_view()),
    path('upload/', views.UploadDetails.as_view()),
]