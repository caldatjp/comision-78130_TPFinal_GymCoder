from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # 🔹 necesario para servir archivos media en desarrollo

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("appgym.urls")),
    path("equipamiento/", include("equipamiento.urls")),
    path("", include("accounts.urls")),
]

# 🔹 Agrega este bloque al final para servir las imágenes del avatar en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
