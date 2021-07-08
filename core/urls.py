"""petcare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('acerca_de/', acerca_de, name='acerca_de'),
    path('contacto/',contacto, name='contacto'),
    path('veterinarios/',veterinarios, name='veterinarios'),
    path('perros/', perros, name='perros'),
    path('gatos/', gatos, name='gatos'),
    path('tienda/',tienda, name='tienda'),
    path('add_producto/', add_producto, name='add_producto'),
    path('add_producto_acceosorios/', add_producto_accesorio, name='add_producto_acceosorios'),
    path('add_producto_limpieza/', add_producto_limpieza, name='add_producto_limpieza'),
    path('add_producto_peluqueria/', add_producto_peluqueria, name='add_producto_peluqueria'),
    path('update_producto_alimento/<idAlimento>', product_update_alimentos, name='update_producto_alimento'),
    path('update_producto_accesorio/<idAccesorio>', product_update_accesorios, name='update_producto_accesorio'),
    path('update_producto_limpieza/<idProducto_limpieza>', product_update_limpieza, name='update_producto_limpieza'),
    path('update_producto_peluqueria/<idProducto_peluqueria>', product_update_peluqueria, name='update_producto_peluqueria'),
    path('product_delete_alimento/<idAlimento>', product_delete_alimento, name='product_delete_alimento'),
    path('product_delete_accesorio/<idAccesorio>', product_delete_accesorio, name='product_delete_accesorio'),
    path('product_delete_limpieza/<idProducto_limpieza>', product_delete_limpieza, name='product_delete_limpieza'),
    path('product_delete_peluqueria/<idProducto_peluqueria>', product_delete_peluqueria, name='product_delete_peluqueria'),
]
