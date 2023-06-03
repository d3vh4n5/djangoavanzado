from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label = "Nombre de contacto:", required=True)
    apellido = forms.CharField(label = "Apellido de contacto", required = True)
    email = forms.EmailField(required=True)