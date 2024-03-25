from django.urls import path,include
from Player_data import views
urlpatterns = [
    path('',views.index,name='home'),
    path('add',views.Add,name='add'),
    
]
