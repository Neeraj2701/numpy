from django.contrib import admin
from django.urls import path
from crudexample import views
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.show),
    path('form/',views.create),
    path('edit/<int:id>',views.edit),
    path('upd/<int:id>',views.upd),
    path('destroy/<int:id>',views.destroy),

]

	