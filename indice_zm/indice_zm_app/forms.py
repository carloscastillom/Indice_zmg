from django import forms    
from .models import indiceDB

class indiceform(forms.ModelForm):
    class Meta:
        model = indiceDB
        fields = ['titulo','serie','autor','editor','idioma','pag','tipo','formato','genero' ]
