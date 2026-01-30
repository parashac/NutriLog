from django import forms
from .models import FoodLog

class FoodLogForm(forms.ModelForm):
    class Meta:
        model = FoodLog
        fields = ['date', 'meal', 'food_item', 'quantity_grams']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'meal': forms.Select(attrs={
                'class': 'form-select'
            }),
            'food_item': forms.Select(attrs={
                'class': 'form-select',
            }),
            'quantity_grams': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'In grams'
            }),

        }
