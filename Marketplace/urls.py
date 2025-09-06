from django.contrib import admin
from django.urls import path, include
from core.views import home # añadido
from market.views import product_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), # añadido ruta base
    path('accounts/', include('allauth.urls')), # requerido por el Allauth
    path('products/', include("market.urls"))
]
