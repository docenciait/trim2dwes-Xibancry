from django import forms
from .models import Denuncia

class DenunciaForm(forms.Form):
    class Meta():
        model = Denuncia
        fields = ('titulo', 'descripcion', 'imagen', 'categoria', 'estado')