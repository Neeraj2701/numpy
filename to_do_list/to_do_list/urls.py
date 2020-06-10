from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.apioverview,name='api-overview'),
    path('task-list/',views.tasklist,name='task-List'),
    path('task-detail/<str:pk>/',views.taskdetail,name='task-detail'),
    path('task-create/',views.taskcreate,name='task-create'),
    path('task-update/<str:pk>/',views.taskupdate,name='task-update'),
    path('task-delete/<str:pk>/',views.taskdelete,name='task-delete'),

]
