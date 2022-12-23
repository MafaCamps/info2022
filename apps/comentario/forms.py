from django import forms
from .models import Comentarios

class ComentarioForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['texto'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Comentarios
        fields = ['texto']
        exclude = ['noticia']
