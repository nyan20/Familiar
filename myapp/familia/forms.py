from django import forms 

from myapp.familia.models import Familia

class FamiliaForm(forms.ModelForm):

    class Meta:
        model = Familia
        
        fields = [
        	'parentesco',
        	'nombre',
        	'fecha_nac',
        	'escolaridad',
        ]
        labels = {
        	'parentesco': 'Parentesco',
        	'nombre': 'Nombre',
        	'fecha_nac': 'Fecha de Nacimiento',
        	'escolaridad': 'Escolaridad',
        }
        widgets = {
        	'parentesco': forms.Select(attrs={'class': 'form-control'}),
        	'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        	'fecha_nac': forms.TextInput(attrs={'class': 'form-control'}),
        	'escolaridad': forms.TextInput(attrs={'class': 'form-control'}),
        }
