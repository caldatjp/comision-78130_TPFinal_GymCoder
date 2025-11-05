from django.contrib import admin
from django.urls import path, include
from appgym.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("appgym.urls")),
    path('equipamiento/', include('equipamiento.urls')),  
]
