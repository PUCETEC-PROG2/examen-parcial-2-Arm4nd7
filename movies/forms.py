from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        labels = {
            'title': 'Titulo',
            'genere': 'Genero',
            'director_name': 'Nombre del Director',
            'year': 'Año',
            'synopsis': 'Sipnosis',            
        }