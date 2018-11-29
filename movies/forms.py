from django import forms

from .models import  Mascotas, Interesados,Estados


class MascotaListForm(forms.ModelForm):

    class Meta:
        model = Mascotas
        fields = '__all__'

class InteresadosForm(forms.ModelForm):

    class Meta:
        model = Interesados
        fields = '__all__'

class EstadosForm(forms.ModelForm):

    class Meta:
        model = Estados
        fields = '__all__'
		
class MascotasForm(forms.ModelForm):

    class Meta:
        model = Mascotas
        fields = '__all__'