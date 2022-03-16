from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path ('first',views.func1),
    path('pay',views.func2),
    path('second',views.func3)

]
