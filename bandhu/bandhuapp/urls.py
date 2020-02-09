from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('cause1/', views.cause1, name="cause1"),
    path('cause2/', views.cause2, name="cause2"),
    path('cause3/', views.cause3, name="cause3"),
    path('cause4/', views.cause4, name="cause4"),
    path('cause5/', views.cause5, name="cause5"),
]