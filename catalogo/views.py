from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
from .dominio import ProductoBase, ProductoOferta

def lista_productos(view_request):
    productos_db = Producto.objects.all()
    productos_con_precio_final = []
    
    for p in productos_db:
        # Usamos las clases de dominio de la UF2404 para calcular el precio final
        if p.descuento > 0:
            prod_dominio = ProductoOferta(p.nombre, float(p.precio), p.descuento)
        else:
            prod_dominio = ProductoBase(p.nombre, float(p.precio))
            
        productos_con_precio_final.append({
            'nombre': p.nombre,
            'precio_original': p.precio,
            'descuento': p.descuento,
            'precio_final': prod_dominio.precio_final()
        })
        
    return render(view_request, 'catalogo/lista_productos.html', {'productos': productos_con_precio_final})


def nuevo_producto(view_request):
    if view_request.method == 'POST':
        form = ProductoForm(view_request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
        
    return render(view_request, 'catalogo/nuevo_producto.html', {'form': form})