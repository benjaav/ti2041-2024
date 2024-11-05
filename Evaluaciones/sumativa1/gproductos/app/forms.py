from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'marca', 'categoria', 'tamaño', 'precio']

    # Validación personalizada para el campo "precio"
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor que 0.")
        return precio
