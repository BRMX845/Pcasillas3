from django.urls import path
from .views import UsuariosList ,CasillaList,DepartamentoList,AlquilerCasillasList
urlpatterns = [
    path('usuarios/',UsuariosList.as_view()),
    path('usuarios/<int:pk>/',UsuariosList.as_view(),name='Usuarios-detail'),
    path('departamentos/',DepartamentoList.as_view()),
    path('departamentos/<int:pk>/',DepartamentoList.as_view(),name='departamento-detail'),
    path('casillas/',CasillaList.as_view()),
    path('casillas/<int:pk>/',CasillaList.as_view(),name='casillas-detail'),
    path('alquilercasillas/',AlquilerCasillasList.as_view()),
    path('alquilercasillas/<int:pk>/',AlquilerCasillasList.as_view(),name='alquiler-detail'),
]