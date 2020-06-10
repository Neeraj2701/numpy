from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from basic_api import views

urlpatterns = [
	path('admin/',admin.site.urls),
    path('basic/',views.API_objects.as_view()),
    path('basic/<int:pk>/',views.API_objects_details.as_view()),

]


urlpatterns=format_suffix_patterns(urlpatterns)

 