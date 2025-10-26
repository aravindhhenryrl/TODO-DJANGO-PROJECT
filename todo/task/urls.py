from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='home'),
    path('update_task/<str:pk>/',views.UpadateTask,name='update_task'),
    path('delete_task/<str:pk>/',views.DeleteTask,name='delete_task'),
]

