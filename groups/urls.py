from django.urls import path
from . import views

urlpatterns = [
    path('UGlist/', views.UsersGroupsList, name='UGlist'),
]