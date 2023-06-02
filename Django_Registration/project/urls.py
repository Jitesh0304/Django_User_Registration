from django.contrib import admin
from django.urls import path,include
from regis import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepg'),
    path('reg/', include('regis.urls')),
]
