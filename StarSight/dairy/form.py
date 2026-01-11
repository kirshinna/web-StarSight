from django import forms
from .models import Observation

class ObservationForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = ['date', 'title', 'description', 'image', 'equipment', 'celestial_body']
        labels = {
            'date': 'Дата наблюдения',
            'title': 'Название',
            'description': 'Описание',
            'image': 'Фото (по желанию)',
            'equipment': 'Оборудование',
            'celestial_body': 'Наблюдаемый объект',
        }
