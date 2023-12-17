from django import forms
from .models import Contacto, Mecanico, Trabajo, Curriculum


class ContactoForm(forms.ModelForm):
    

    class Meta:
        model = Contacto
        fields = "__all__"



class MecanicoForm(forms.ModelForm):

    class Meta:
        model = Mecanico
        fields = "__all__"
        widgets = {"fecha_nacimiento" : forms.DateInput(attrs={'type': 'date'}, format=('%Y-%m-%d'))}


class AgregarTrabajoForm(forms.ModelForm):

    class Meta:
        model = Trabajo
        fields = "__all__"

class ModificarTrabajoForm(forms.ModelForm):
    autorizado = forms.BooleanField(required=False)

    class Meta:
        model = Trabajo
        fields = "__all__"


class CurriculumForm(forms.ModelForm):
    
    
    class Meta:
        model = Curriculum
        fields ="__all__"
        widgets = {"fecha_nacimiento" : forms.DateInput(attrs={'type': 'date'}, format=('%Y-%m-%d'))}


    
