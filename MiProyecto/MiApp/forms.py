from django import forms


class CrearPostForm(forms.Form):
  titulo = forms.CharField(max_length=90)
  fecha = forms.DateField()
  texto = forms.CharField(max_length=450)


class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length= 100)
    email = forms.EmailField()
    consulta = forms.CharField(max_length=450)
