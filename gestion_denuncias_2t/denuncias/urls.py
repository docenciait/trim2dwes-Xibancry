from django.urls import path
from .views import lista_denuncias, crear_denuncia, editar_denuncia, eliminar_denuncia

urlpatterns = [
    path('denuncias/', lista_denuncias.as_view(), name='lista_denuncias'),
    path('denuncias/crear/', crear_denuncia.as_view(), name='crear_denuncia'),
    path('denuncias/editar/<int:id>/', editar_denuncia.as_view(), name='editar_denuncia'),
    path('denuncias/eliminar/<int:id>/', eliminar_denuncia.as_view(), name='eliminar_denuncia'),
]