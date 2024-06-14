from django.urls import path
from . import views

urlpatterns = [
    path('',  views.getRoutes),
path('api/rooms/<int:id>/', views.delete_room, name='delete_room'),
    path('rooms/', views.getRooms),
    path('rooms/<str:pk>/', views.getRoom),
]
