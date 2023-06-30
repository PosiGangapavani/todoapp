from django.urls import path
from . import views
urlpatterns = [
    path('addTask/',views.addTask,name='addTask'),
    path('mark_as_complete/<int:pk>/',views.mark_as_complete,name='mark_as_complete'),
    path('mark_as_undone/<int:pk>/',views.mark_as_undone,name='mark_as_undone'),
    path('edit_task/<int:pk>/',views.edit_task,name='edit_task'),
    path('delete_task/<int:pk>/',views.delete_task,name='delete_task'),
]