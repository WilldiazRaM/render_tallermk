from django.urls import path
from .views import home, eliminarCurriculum , listar_trabajo4Mecanico, contacto, galeriaMecanicos, agregar_mecanico, listar_mecanico, modificar_mecanico, eliminar_mecanico, login_usuario, registro_mecanico, agregar_trabajo, listar_trabajos, modificar_trabajo, autorizar_trabajo, rechazar_trabajo, trabaja_con_nosotros, listarTrabajoHome, listarCurriculums, verPostulacion
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name="home"),
    path('contacto/', contacto, name="contacto"),    
    path('galeriaMecanicos/', galeriaMecanicos, name="galeriaMecanicos"),
    path('Mantenedor/mecanico/agregar', agregar_mecanico, name="agregar_mecanico"),
    path('Mantenedor/mecanico/listar', listar_mecanico, name="listar_mecanico"),
    path('Mantenedor/mecanico/modificar/<rut>', modificar_mecanico, name="modificar_mecanico"),
    path('Mantenedor/mecanico/eliminar/<rut>', eliminar_mecanico, name="eliminar_mecanico"),
    path('login_usuario/', login_usuario, name="login_usuario"),
    path('registro_mecanico', registro_mecanico, name="registro_mecanico"),
    path('Mantenedor/Trabajo/agregar', agregar_trabajo, name="agregar_trabajo"),  
    path('Mantenedor/Trabajo/listar', listar_trabajos, name="listar_trabajo"),
    path('Mantenedor/Trabajo/listar/mecanico', listar_trabajo4Mecanico, name="listar_trabajo4Mecanico"),
    path('Mantenedor/Trabajo/modificar/<titulo>/', modificar_trabajo, name="modificar_trabajo"),
    path('Mantenedor/Trabajo/autorizar/<int:pk>/', autorizar_trabajo, name="autorizar_trabajo"),
    path('Mantenedor/Trabajo/rechazar/<int:pk>/', rechazar_trabajo, name="rechazar_trabajo"),
    path('Mantenedor/Trabajo/listarTrabajoHome/<str:titulo>/', listarTrabajoHome, name="listarTrabajosHome"),
    path('TrabajaConNosotros/', trabaja_con_nosotros , name="trabaja_con_nosotros"),
    path('Mantenedor/Curriculum/listarCurriculum', listarCurriculums , name="listarCurriculum"),
    path('Mantenedor/Curriculum/detallePostulacion/<pk>/' , verPostulacion, name="verPostulacion"),
    path('Mantenedor/Curriculum/eliminarPostulacion/<pk>/' , eliminarCurriculum, name="eliminarCurriculum")
                
        ] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)