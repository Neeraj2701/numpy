from django.contrib import admin
from django.urls import path
from traveler import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tour/',views.func),

]

urlpatterns=format_suffix_patterns(urlpatterns)