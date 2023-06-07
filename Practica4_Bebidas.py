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

    def quitar_bebida(self, id):
        bebida = self.buscar_bebida(id)
        if bebida:
            self.bebidas.remove(bebida)

    def actualizar_bebida(self, id, nombre, clasificacion, marca, precio):
        bebida = self.buscar_bebida(id)
        if bebida:
            bebida.nombre = nombre
            bebida.clasificacion = clasificacion
            bebida.marca = marca
            bebida.precio = precio

    def mostrar_bebidas(self):
        for bebida in self.bebidas:
            print(f"ID: {bebida.id}, Nombre: {bebida.nombre}, Clasificación: {bebida.clasificacion}, Marca: {bebida.marca}, Precio: {bebida.precio}")

    def buscar_bebida(self, id):
        for bebida in self.bebidas:
            if bebida.id == id:
                return bebida
        return None

    def calcular_precio_promedio(self):
        total = sum(bebida.precio for bebida in self.bebidas)
        promedio = total / len(self.bebidas) if len(self.bebidas) > 0 else 0
        return promedio

    def cantidad_por_marca(self, marca):
        cantidad = sum(1 for bebida in self.bebidas if bebida.marca == marca)
        return cantidad

    def cantidad_por_clasificacion(self, clasificacion):
        cantidad = sum(1 for bebida in self.bebidas if bebida.clasificacion == clasificacion)
        return cantidad


def mostrar_menu():
    print("---- Menú ----")
    print("1. Agregar bebida")
    print("2. Quitar bebida")
    print("3. Actualizar bebida")
    print("4. Mostrar bebidas")
    print("5. Calcular precio promedio de bebidas")
    print("6. Cantidad de bebidas de una marca")
    print("7. Cantidad de bebidas por clasificación")
    print("0. Salir")


def obtener_datos_bebida():
    id = int(input("Ingrese el ID de la bebida: "))
    nombre = input("Ingrese el nombre de la bebida: ")
    clasificacion = input("Ingrese la clasificación de la bebida: ")
    marca = input("Ingrese la marca de la bebida: ")
    precio = float(input("Ingrese el precio de la bebida: "))
    return Bebida(id, nombre, clasificacion, marca, precio)


almacen = AlmacenBebidas()

while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        bebida = obtener_datos_bebida()
        almacen.agregar_bebida(bebida)
        print("Bebida agregada correctamente.")
    elif opcion == "2":
        id = int(input("Ingrese el ID de la bebida a quitar: "))
        almacen.quitar_bebida(id)
        print("Bebida quitada correctamente.")
    elif opcion == "3":
        id = int(input("Ingrese el ID de la bebida a actualizar: "))
        bebida = obtener_datos_bebida()
        almacen.actualizar_bebida(bebida)
        print("Bebida actualizada correctamente.")
    elif opcion == "4":
        almacen.mostrar_bebidas()
    elif opcion == "5":
        promedio = almacen.calcular_precio_promedio()
        print(f"Precio promedio de bebidas: {promedio}")
    elif opcion == "6":
        marca = input("Ingrese la marca de bebidas: ")
        cantidad = almacen.cantidad_por_marca(marca)
        print(f"Cantidad de bebidas de la marca {marca}: {cantidad}")
    elif opcion == "7":
        clasificacion = input("Ingrese la clasificación de bebidas: ")
        cantidad = almacen.cantidad_por_clasificacion(clasificacion)
        print(f"Cantidad de bebidas de la clasificación {clasificacion}: {cantidad}")
    elif opcion == "0":
        break
    else:
        print("Opción inválida. Intente nuevamente.")
