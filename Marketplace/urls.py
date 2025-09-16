from django.contrib import admin
from django.urls import path, include
from core.views import home # añadido
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), # añadido ruta base
    path('accounts/', include('allauth.urls')), # requerido por el Allauth
    path('products/', include("market.urls")),
    path('profiles/', include("perfil.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
