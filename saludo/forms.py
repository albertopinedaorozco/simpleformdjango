from django import forms
from .models import Mesero

class MeseroForm(forms.ModelForm):
    nombre = forms.CharField(max_length=40)
    apellidos = forms.CharField(max_length=40)
    edad = forms.IntegerField()

    class Meta:
        model = Mesero
        fields = '__all__'
    
 