from django.urls import path
from . import views

app_name = 'books'
 
urlpatterns = [
   path('', views.books, name="list"),
   path('add_form/', views.add, name="add"),
   path('delete/', views.delete, name="delete"),
   path('search/', views.search, name="search")
]
