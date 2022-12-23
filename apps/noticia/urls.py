from django.urls import path
from .views import NoticiaListview, CategoriaListview
from . import views

app_name = 'apps.noticia'

urlpatterns = [
    path("noticias", NoticiaListview.as_view(), name='noticias'),
    path("categorias", CategoriaListview.as_view(), name='categorias'),
    path('listarporcategoria/<str:categoria>',views.listarporcategoria, name='listarporcategoria'),
    path('AgregarNoticia/', views.AgregarNoticia.as_view(),name="AgregarNoticia"),
    path('AgregarCategoria/', views.AgregarCategoria.as_view(),name="AgregarCategoria"),
    path('BorrarCategoria/<pk>', views.BorrarCategoria.as_view(),name="BorrarCategoria"),
    path('Leerpost/<int:id>', views.LeerPost, name="Leerpost"),
    path('BorrarNoticia/<pk>', views.BorrarNoticia.as_view(),name="BorrarNoticia"),
    path('ActualizarNoticia/<pk>', views.ActualizarNoticia.as_view(), name="ActualizarNoticia"), 
]
