from django.urls import path
from .views import Create_Room, Message_View, Login_View, Index_View

urlpatterns = [
    path('', Index_View, name='index'),
    path('login/', Login_View, name='login'),
    path('create-room/', Create_Room, name='create_room'),
    path('room/<str:room_name>/', Message_View, name='messages'),
]
