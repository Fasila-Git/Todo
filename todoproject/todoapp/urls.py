
from django.urls import path
from . import views

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskId>/',views.delete,name='delete'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('cbvhome/',views.TaskListView.as_view(),name='cbvhome'),
    path('cbvdetails/<int:pk>/',views.TaskDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete'),
]