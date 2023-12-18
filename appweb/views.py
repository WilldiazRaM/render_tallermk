from django.shortcuts import render, redirect, get_object_or_404
from .models import Mecanico, Trabajo, Curriculum
from .forms import Contacto, ContactoForm, MecanicoForm, AgregarTrabajoForm, ModificarTrabajoForm, CurriculumForm
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login
from django.contrib import messages 



# Create your views here.
def home(request):
    trabajos = Trabajo.objects.filter(autorizado=True, imagenes__isnull=False)

    context = {
        'trabajos': trabajos
    }
    messages.info(request, "AppWeb Taller RAYO MKWEEN ")
    return render(request, 'home.html', context)

def contacto(request):
    data = {
    'form' : ContactoForm,
    'mensaje' :""
    }

    if request.method == "POST":
        formulario = ContactoForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Contacto guardado"
            messages.success(request, "Formulario Enviado con Éxito")
        else:
            data['form'] = formulario
            data['mensaje'] = 'Ocurrio un error' 
            messages.warning(request, "No se pudo enviar el Formulario")  
    
    
    return render(request, 'contacto.html', data)





def galeriaMecanicos(request):
    mecanicos = Mecanico.objects.all()
    data = {
        'mecanicos': mecanicos
    }

    if request.method == "POST":
        valor_buscar = request.POST.get("valor_buscar")
        if valor_buscar != "":
            mecanicos_filtrados = Mecanico.objects.filter(nombre=valor_buscar)
            data["mecanicos"] = mecanicos_filtrados
            print(valor_buscar)
        else:
            data["mecanicos"] = Mecanico.objects.all()

    return render(request, 'galeriaMecanicos.html', data)

def agregar_mecanico(request):
    data = {
        'form': MecanicoForm,
        'mensaje': ""
    }

    if request.method == 'POST':
        formulario = MecanicoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Mecanico Guardado"
            messages.success(request, "Mecanico Agregado Correctamente")
        else:
            data['form'] = formulario
            data['mensaje'] = "-Ocurrió un error-"
            messages.error(request, "No se pudo agregar el Mecanico")

    return render(request, "Mantenedor/mecanico/agregar.html", data)


def listar_mecanico(request):

    mecanicos = Mecanico.objects.all()
    
    data = {
        'mecanicos': mecanicos
        
        
    }

    return render(request, "Mantenedor/mecanico/listar.html", data)



def modificar_mecanico(request, rut):

    mecanico = get_object_or_404(Mecanico, rut=rut)

    data= {
        "form": MecanicoForm(instance=mecanico)
    }

    if request.method == "POST":
        formulario = MecanicoForm(data=request.POST, instance=mecanico, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mecanido modificado con Exito")
            return redirect(to="listar_mecanico")
        else:
            data['form'] = formulario
            data['mensaje'] = "Ocurrio un error"

    return render(request, "Mantenedor/mecanico/modificar.html", data)


def eliminar_mecanico(request, rut):
    mecanico = get_object_or_404(Mecanico, rut=rut)

    mecanico.delete()
    messages.success(request, "Mecanido Eliminado")

    return redirect(to=listar_mecanico)


def login_usuario(request):

    print("Bienvenido: " +request.user.username)
    print("este es el login")

    #obtener todo los grupos al que pertenece usuario
    print('grupos:', request.user.groups.all())

    #validar si un usuario pertenece a un grupo determinado
    if request.user.groups.filter(name='Mecanico'):
     print("Es un Mecanico")
        
    return redirect(to="home")


def registro_mecanico(request):
    data = {
        "mensaje": ""
    }
    if request.POST:
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        correo = request.POST.get("correo")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            data["mensaje"] = "Las contraseñas deben ser iguales."
        else:
            try:
                usu = User()
                usu.set_password(password1)
                usu.email = correo
                usu.username = nombre
                usu.last_name = apellido
                usu.first_name = nombre
                usu.save()

                grupo = Group.objects.get(name="mecanico")
                usu.groups.add(grupo)

                data['mensaje'] = 'Usuario creado con éxito'

                user = authenticate(username=usu.username, password=password1)
                login(request, user)
                return redirect(to='home')
            except Exception as e:
                data['mensaje'] = 'Error al registrar: {}'.format(str(e))

    return render(request, "registration/registro.html", data)


def agregar_trabajo(request):

    data = {
        'form': AgregarTrabajoForm,
        'mensaje':""

    }
    if request.method == "POST":
        formulario = AgregarTrabajoForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Trabajo Guardado con Exito ")
            data['mensaje']= "Trabajo Guardado"
        else:
            data['form'] = formulario
            data['mensaje'] = "Ocurrio un error al agregar El trabajo"

    return render(request, "Mantenedor/Trabajo/agregarTrabajo.html", data)


def listar_trabajos (request):

    trabajos = Trabajo.objects.all()

    data = {
            'trabajos': trabajos
            }

    return render(request, "Mantenedor/Trabajo/listarTrabajo.html", data)



def listar_trabajo4Mecanico(request):   

    trabajos = Trabajo.objects.all()

    data = { 
        'trabajos' : trabajos
    } 
        
    return render(request, "Mantenedor/Trabajo/listarTrabajoMecanico.html", data)






def modificar_trabajo(request, titulo):
    trabajo = get_object_or_404(Trabajo, titulo=titulo)

    data = {
        "form": AgregarTrabajoForm(instance=trabajo)
    }

    return render(request, "Mantenedor/Trabajo/modificarTrabajo.html", data)    

def autorizar_trabajo(request, pk):
    trabajo = get_object_or_404(Trabajo, pk=pk)
    trabajo.autorizado = True
    trabajo.save()
    return redirect('listar_trabajo')

def rechazar_trabajo(request, pk):
    trabajo = get_object_or_404(Trabajo, pk=pk)
    trabajo.autorizado = False
    trabajo.save()
    return redirect('listar_trabajo')


def trabaja_con_nosotros(request):

    data = {

        'form': CurriculumForm,
        'mensaje':""
        
    }
    if request.method == "POST":
        formulario = CurriculumForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Curriculum Enviado con Exito!"
            messages.success(request, "Postulacion enviada correctamente")
        else:
            data['form'] = formulario
            data['mensaje'] = "Ocurrio un error"

    
    return render(request, "TrabajaConNosotros.html", data)


def listarTrabajoHome(request, titulo):
    trabajos = Trabajo.objects.filter(titulo=titulo)

    data = {
        "trabajos": trabajos,
        "titulo": titulo
    }

    return render(request, "Mantenedor/Trabajo/listarTrabajoHome.html", data)

def listarCurriculums(request):
    curriculums = Curriculum.objects.all()
    
    data = {
        'curriculums': curriculums
    }

    return render(request, "Mantenedor/Curriculum/listarCurriculum.html", data)

def verPostulacion(request, pk):

    curriculum = get_object_or_404(Curriculum,pk=pk)

    data = {
        'curriculum' : curriculum
    }


    return render(request, "Mantenedor/Curriculum/detalleCurriculum.html", data)

def eliminarCurriculum(request, pk):

    curriculum = get_object_or_404(Curriculum, pk=pk)
    curriculum.delete()
    messages.success(request, "Postulacion Eliminada Correctamente")

    return redirect(to=listarCurriculums)