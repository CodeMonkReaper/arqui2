from django import forms
from registro_pago.models import Pago

class añadirPago(forms.ModelForm):
    class Meta:
        model = Pago
        fields = [
            'cliente',
            'cantidad',
            'rutCliente',
            'fecha',
            'descripcion'
        ]
        labels = {
            'cliente': 'Cliente',
            'cantidad': 'Cantidad',
            'rutCliente': 'Rut Cliente',
            'fecha': 'Fecha',
            'descripcion': 'Descripcion'
        }
        widgets = {
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
            'rutCliente': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'})
        }
