from django.contrib import admin
from django.urls import path
from student import views
from rest_framework.urlpatterns import format_suffix_patterns




urlpatterns = [
    path('admin/', admin.site.urls),
    path('Stud/',views.get),

]

urlpatterns=format_suffix_patterns(urlpatterns)
