<<<<<<< HEAD
from django import forms
from ejemplo.models import Familiar


class Buscar (forms.Form):
    nombre = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']
=======
forom django import forms

class Buscar (forms.Form):
    nombre = forms.CharField(max_length=100)
>>>>>>> e248c65561f475e710ff55a0e7bbac5e39c4f7ee
