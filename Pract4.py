class Bebida:
    def __init__(self, id, nombre, clasificacion, marca, precio):
        self.id = id
        self.nombre = nombre
        self.clasificacion = clasificacion
        self.marca = marca
        self.precio = precio

class AlmacenBebidas:
    def __init__(self):
        self.bebidas = []

    def agregar_bebida(self, bebida):
        self.bebidas.append(bebida)

    def eliminar_bebida(self, id):
        for bebida in self.bebidas:
            if bebida.id == id:
                self.bebidas.remove(bebida)
                break

    def actualizar_bebida(self, id, nombre, clasificacion, marca, precio):
        for bebida in self.bebidas:
            if bebida.id == id:
                bebida.nombre = nombre
                bebida.clasificacion = clasificacion
                bebida.marca = marca
                bebida.precio = precio
                break

    def mostrar_todas_bebidas(self):
        for bebida in self.bebidas:
            print("ID:", bebida.id)
            print("Nombre:", bebida.nombre)
            print("Clasificación:", bebida.clasificacion)
            print("Marca:", bebida.marca)
            print("Precio:", bebida.precio)
            print()

    def calcular_precio_promedio(self):
        total_precios = sum(bebida.precio for bebida in self.bebidas)
        promedio = total_precios / len(self.bebidas)
        return promedio

    def cantidad_bebidas_marca(self, marca):
        cantidad = sum(1 for bebida in self.bebidas if bebida.marca == marca)
        return cantidad

    def cantidad_bebidas_clasificacion(self, clasificacion):
        cantidad = sum(1 for bebida in self.bebidas if bebida.clasificacion == clasificacion)
        return cantidad



almacen = AlmacenBebidas()


bebida1 = Bebida(1, "Agua", "Bebida sin azúcar", "Marca1", 1.5)
almacen.agregar_bebida(bebida1)

bebida2 = Bebida(2, "Refresco", "Bebida azucarada", "Marca2", 2.0)
almacen.agregar_bebida(bebida2)

bebida3 = Bebida(3, "Energética", "Bebida energética", "Marca1", 3.5)
almacen.agregar_bebida(bebida3)

print("Todas las bebidas en el almacén:")
almacen.mostrar_todas_bebidas()

precio_promedio = almacen.calcular_precio_promedio()
print("Precio promedio de las bebidas:", precio_promedio)

marca = "Marca1"
cantidad_marca = almacen.cantidad_bebidas_marca(marca)
print("Cantidad de bebidas de la marca", marca + ":", cantidad_marca)

clasificacion = "Bebida sin azúcar"
cantidad_clasificacion = almacen.cantidad_bebidas_clasificacion(clasificacion)
print("Cantidad de bebidas de la clasificación", clasificacion + ":", cantidad_clasificacion)
