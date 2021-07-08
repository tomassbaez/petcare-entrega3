from django import forms
from django.forms import ModelForm
from .models import Alimento, Accesorio, Producto_limpieza, Producto_peluqueria

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Alimento

        fields = [
            'idAlimento',
            'descripcion',
            'precio',
            'cantidad',
            'imagen',
            'marca'
        ]        
        
        labels = {
            'idAlimento':'Código Producto',
            'descripcion':'Descripción',
            'precio':'Precio Unitario $',
            'cantidad':'Stock',
            'imagen':"Imagen",
            'marca':'Marca'
        }
        widgets = {
            'idAlimento':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'precio':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'cantidad':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'imagen':forms.FileInput(attrs={'class':'form-control'}),
            'marca':forms.Select(attrs={'class':'form-control'})
        }

class ProductoFormAccesorios(forms.ModelForm):
    class Meta:
        model = Accesorio

        fields = [
            'idAccesorio',
            'descripcion',
            'precio',
            'cantidad',
            'imagen',
            'marca'
        ]        
        
        labels = {
            'idAccesorio':'Código Producto',
            'descripcion':'Descripción',
            'precio':'Precio Unitario $',
            'cantidad':'Stock',
            'imagen':"Imagen",
            'marca':'Marca'
        }
        widgets = {
            'idAccesorio':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'precio':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'cantidad':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'imagen':forms.FileInput(attrs={'class':'form-control'}),
            'marca':forms.Select(attrs={'class':'form-control'})
        }

##formulario limpieza
class ProductoFormLimpieza(forms.ModelForm):
    class Meta:
        model = Producto_limpieza

        fields = [
            'idProducto_limpieza',
            'descripcion',
            'precio',
            'cantidad',
            'imagen',
            'marca'
        ]        
        
        labels = {
            'idProducto_limpieza':'Código Producto',
            'descripcion':'Descripción',
            'precio':'Precio Unitario $',
            'cantidad':'Stock',
            'imagen':"Imagen",
            'marca':'Marca'
        }
        widgets = {
            'idProducto_limpieza':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'precio':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'cantidad':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'imagen':forms.FileInput(attrs={'class':'form-control'}),
            'marca':forms.Select(attrs={'class':'form-control'})
        }


##formulario limpieza
class ProductoFormPeluqueria(forms.ModelForm):
    class Meta:
        model = Producto_peluqueria

        fields = [
            'idProducto_peluqueria',
            'descripcion',
            'precio',
            'cantidad',
            'imagen',
            'marca'
        ]        
        
        labels = {
            'idProducto_peluqueria':'Código Producto',
            'descripcion':'Descripción',
            'precio':'Precio Unitario $',
            'cantidad':'Stock',
            'imagen':"Imagen",
            'marca':'Marca'
        }
        widgets = {
            'idProducto_peluqueria':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'precio':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'cantidad':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'imagen':forms.FileInput(attrs={'class':'form-control'}),
            'marca':forms.Select(attrs={'class':'form-control'})
        }








