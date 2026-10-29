from django.test import TestCase, Client
from django.urls import reverse
from .dominio import ProductoOferta

class CatalogoTests(TestCase):
    
    def test_precio_final_con_descuento(self):
        """1. Verificar que un producto de 100 € con un descuento del 20 % devuelve 80 €."""
        producto = ProductoOferta("Televisor", 100, 20)
        self.assertEqual(producto.precio_final(), 80.0)

    def test_url_productos_responde_200(self):
        """2. Verificar que la página /productos/ responde con el código HTTP 200."""
        cliente = Client()
        url = reverse('lista_productos')  # Busca la ruta automáticamente
        respuesta = cliente.get(url)
        self.assertEqual(respuesta.status_code, 200)