from django.urls import path, include
from articles import views

app_name = 'articles'

urlpatterns = [
    path('index/', views.index, name= 'index' ),
]