class ProductoBase:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.precio = precio

    def precio_final(self):
        return self.precio


class ProductoOferta(ProductoBase):
    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio)
        if not (0 <= descuento <= 100):
            raise ValueError("El descuento debe estar entre 0 y 100.")
        self.descuento = descuento

    def precio_final(self):
        # Aplica el porcentaje de descuento sobre el precio original
        return self.precio * (1 - self.descuento / 100)