from django.shortcuts import render, redirect, reverse
from .models import Alimento, Accesorio, Producto_limpieza, Producto_peluqueria
from .forms import ProductoForm, ProductoFormAccesorios, ProductoFormLimpieza, ProductoFormPeluqueria

# Create your views here.
alimentos = Alimento.objects.all()
accesorios = Accesorio.objects.all()
productos_limpieza = Producto_limpieza.objects.all()
productos_peluqueria = Producto_peluqueria.objects.all()


def index(request):
    return render(request, "core/index.html")
#base para probar
def base(request):
    return render(request, "core/base.html")

def acerca_de(request):
    return render(request, "core/acerca_de.html")

def contacto(request):
    return render(request, "core/contacto.html")

def veterinarios(request):
    return render(request, "core/veterinarios.html")

def gatos(request):
    return render(request, "core/gatos.html")

def perros(request):
    return render(request, "core/perros.html")

###
#Formularios para agregar productos
###
def add_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            idAlimento = form.cleaned_data.get("idAlimento")
            descripcion = form.cleaned_data.get("descripcion")
            precio = form.cleaned_data.get("precio")
            cantidad = form.cleaned_data.get("cantidad")
            imagen = form.cleaned_data.get("imagen")
            marca = form.cleaned_data.get("marca")
            obj = Alimento.objects.create(
                idAlimento=idAlimento,
                descripcion=descripcion,
                precio=precio,
                cantidad=cantidad,
                imagen=imagen,
                marca=marca
            )
            obj.save()         
            return redirect(reverse('add_producto')+ "?ok")
        else:
            return redirect(reverse('add_producto')+ "?fail")
    else:
        form = ProductoForm()

    return render(request,'core/add_producto.html',{'form':form})


##Formulario accesorios
def add_producto_accesorio(request):
    if request.method == 'POST':
        form = ProductoFormAccesorios(request.POST or None,request.FILES or None)
        if form.is_valid():
            idAccesorio = form.cleaned_data.get("idAccesorio")
            descripcion = form.cleaned_data.get("descripcion")
            precio = form.cleaned_data.get("precio")
            cantidad = form.cleaned_data.get("cantidad")
            imagen = form.cleaned_data.get("imagen")
            marca = form.cleaned_data.get("marca")
            obj = Accesorio.objects.create(
                idAccesorio=idAccesorio,
                descripcion=descripcion,
                precio=precio,
                cantidad=cantidad,
                imagen=imagen,
                marca=marca
            )
            obj.save()          
            return redirect(reverse('add_producto_accesorio')+ "?ok")
        else:
            return redirect(reverse('add_producto_accesorio')+ "?fail")
    else:
        form = ProductoFormAccesorios()

    return render(request,'core/add_producto_accesorios.html',{'form':form})


##Formulario limpieza
def add_producto_limpieza(request):
    if request.method == 'POST':
        form = ProductoFormLimpieza(request.POST or None,request.FILES or None)
        if form.is_valid():
            idProducto_limpieza = form.cleaned_data.get("idProducto_limpieza")
            descripcion = form.cleaned_data.get("descripcion")
            precio = form.cleaned_data.get("precio")
            cantidad = form.cleaned_data.get("cantidad")
            imagen = form.cleaned_data.get("imagen")
            marca = form.cleaned_data.get("marca")
            obj = Producto_limpieza.objects.create(
                idProducto_limpieza=idProducto_limpieza,
                descripcion=descripcion,
                precio=precio,
                cantidad=cantidad,
                imagen=imagen,
                marca=marca
            )
            obj.save()          
            return redirect(reverse('add_producto_limpieza')+ "?ok")
        else:
            return redirect(reverse('add_producto_limpieza')+ "?fail")
    else:
        form = ProductoFormLimpieza()

    return render(request,'core/add_producto_limpieza.html',{'form':form}) 

##Formulario peluqueria
def add_producto_peluqueria(request):
    if request.method == 'POST':
        form = ProductoFormPeluqueria(request.POST or None,request.FILES or None)
        if form.is_valid():
            idProducto_peluqueria = form.cleaned_data.get("idProducto_peluqueria")
            descripcion = form.cleaned_data.get("descripcion")
            precio = form.cleaned_data.get("precio")
            cantidad = form.cleaned_data.get("cantidad")
            imagen = form.cleaned_data.get("imagen")
            marca = form.cleaned_data.get("marca")
            obj = Producto_peluqueria.objects.create(
                idProducto_peluqueria=idProducto_peluqueria,
                descripcion=descripcion,
                precio=precio,
                cantidad=cantidad,
                imagen=imagen,
                marca=marca
            )
            obj.save()          
            return redirect(reverse('add_producto_peluqueria')+ "?ok")
        else:
            return redirect(reverse('add_producto_peluqueria')+ "?fail")
    else:
        form = ProductoFormPeluqueria()

    return render(request,'core/add_producto_peluqueria.html',{'form':form}) 


#RETURN TABLAS BDD
def tienda(request):
    alimentos = Alimento.objects.all()
    accesorios = Accesorio.objects.all()
    return render(request, "core/tienda.html",{'alimentos':alimentos,'accesorios':accesorios,'productos_limpieza':productos_limpieza,'productos_peluqueria':productos_peluqueria})

#Funciones modificar y eliminar 
#funcion de modificar

#Funciona de modificar alimento
def product_update_alimentos(request, idAlimento):
    alimento = Alimento.objects.get(idAlimento = idAlimento)
    form = ProductoForm(instance = alimento)

    if request.method == 'POST':
        form = ProductoForm(request.POST,request.FILES,instance=alimento)
        if form.is_valid():
            form.save()                
            return redirect(reverse('tienda')+ "?ok")
        else:
            return redirect(reverse('update_producto_alimento')+ idAlimento)

    return render(request,'core/update_producto_alimento.html',{'form':form})

#Funcion de modificar Accesorios
def product_update_accesorios(request, idAccesorio):
    accesorio = Accesorio.objects.get(idAccesorio = idAccesorio)
    form = ProductoFormAccesorios(instance = accesorio)

    if request.method == 'POST':
        form = ProductoFormAccesorios(request.POST,request.FILES,instance=accesorio)
        if form.is_valid():
            form.save()                
            return redirect(reverse('tienda')+ "?ok")
        else:
            return redirect(reverse('update_producto_accesorio')+ idAccesorio)

    return render(request,'core/update_producto_accesorio.html',{'form':form})


#Funcion de modificar Prodctos de limpieza
def product_update_limpieza(request, idProducto_limpieza):
    limpieza = Producto_limpieza.objects.get(idProducto_limpieza = idProducto_limpieza)
    form = ProductoFormLimpieza(instance = limpieza)

    if request.method == 'POST':
        form = ProductoFormLimpieza(request.POST,request.FILES,instance=limpieza)
        if form.is_valid():
            form.save()                
            return redirect(reverse('tienda')+ "?ok")
        else:
            return redirect(reverse('update_producto_limpieza')+ idProducto_limpieza)

    return render(request,'core/update_producto_limpieza.html',{'form':form})

#Funcion de modificar Prodctos de limpieza
def product_update_peluqueria(request, idProducto_peluqueria):
    peluqueria = Producto_peluqueria.objects.get(idProducto_peluqueria = idProducto_peluqueria)
    form = ProductoFormPeluqueria(instance = peluqueria)

    if request.method == 'POST':
        form = ProductoFormPeluqueria(request.POST,request.FILES,instance=peluqueria)
        if form.is_valid():
            form.save()                
            return redirect(reverse('tienda')+ "?ok")
        else:
            return redirect(reverse('update_producto_peluqueria')+ idProducto_peluqueria)

    return render(request,'core/update_producto_peluqueria.html',{'form':form})

#Funcion para eliminar
#Funcion para eliminar alimentos
def product_delete_alimento(request, idAlimento):
    alimento = Alimento.objects.get(idAlimento = idAlimento)
    alimento.delete()
    return redirect(to="tienda")

#Funcion para eliminar alimentos
def product_delete_accesorio(request, idAccesorio):
    accesorio = Accesorio.objects.get(idAccesorio = idAccesorio)
    accesorio.delete()
    return redirect(to="tienda")

#Funcion para eliminar productos de limpieza
def product_delete_limpieza(request, idProducto_limpieza):
    limpieza = Producto_limpieza.objects.get(idProducto_limpieza = idProducto_limpieza)
    limpieza.delete()
    return redirect(to="tienda")


#Funcion para eliminar productos de peluqueria
def product_delete_peluqueria(request, idProducto_peluqueria):
    peluqueria = Producto_peluqueria.objects.get(idProducto_peluqueria = idProducto_peluqueria)
    peluqueria.delete()
    return redirect(to="tienda")
 