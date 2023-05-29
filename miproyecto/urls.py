from django.urls import path, re_path # es la funcion que nos provee django para asociar urls a vistas
from . import views #importo las vistas para que funcine
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.url_invalida2), #Si esta vacio luego de "mi proyecto"
    path('english/', views.english, name='saludar_ingles'),
    # path('español/', views.index),
    # path('saludar/<str:nombre>', views.saludar),
    # path('calcular/<int:numero>', views.calcular),
    path('', views.index), #Luego de ser redireccionado acá al no marcar ruta, volvemos a redireccionar al index, lo cual hace que el index de nuestra vista en "miproyecto" se la página principal
    path('proyectos/<int:anio>/<int:mes>',
         views.ver_proyectos, name="ver_proyectos"),#Con el name indico que inequivocamente nos va a dirigir a esa vista
    path('cursos/detalle/<slug:nombre_curso>',
         views.curso_detalle, name="curso_detalle"),
    re_path(r'^cursos/(?P<nombre>\w+)/$', views.cursos, name='cursos'),
    path('redireccionar/', views.redireccion, name='redireccion'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
