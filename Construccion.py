from constructor import Automovil, Particular, Carga, Bicicleta, Motocicleta, Vehiculo, guardar_datos_csv

contador = 0
nro_vehiculos_ingres = input("Ingrese el numero de vehiculos a registrar:")
nro_vehiculos_ingres = int(nro_vehiculos_ingres)
autos = []

while contador < nro_vehiculos_ingres:
    print(f"Datos del automovil {contador +1}")
    marca = input("Inserte la marca del automovil:")
    modelo = input("Inserte el modelo del automovil:")
    nro_ruedas = input("Inserte el numero de ruedad del automovil:")
    velocidad = input("Inserte la velocidad del automovil en km/h:")
    cilindrada = input("Inserte el cilindraje del automovil en cc:")
    nuevo_vehiculo = Automovil(
        marca, modelo, nro_ruedas, velocidad, cilindrada)
    autos.append(nuevo_vehiculo)
    guardar_datos_csv("vehiculos.csv", nuevo_vehiculo)
    contador += 1
else:
    print("Imprimiendo por pantalla los vehiculos ingresados:")
    for x in autos:
        print(
            f"Datos del automovil: Marca {x.marca}, Modelo {x.modelo}, {x.nro_ruedas} ruedas, {x.velocidad} Km/h, {x.cilindrada} cc")


# particular = Particular("Toyota", "Prius", "4", "200", "400", 2)
# carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
# bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
# motocicleta = Motocicleta(
#     "BMW", "F800s", 2, "Deportiva", "2T", "DobleViga", 21)

# print(particular)
# print("*"*30)
# print(carga)
# print("*"*30)
# print(bicicleta)
# print("*"*30)
# print(motocicleta)

# print(isinstance(motocicleta, Vehiculo))
# print(isinstance(motocicleta, Automovil))
# print(isinstance(motocicleta, Particular))
# print(isinstance(motocicleta, Carga))
# print(isinstance(motocicleta, Bicicleta))
# print(isinstance(motocicleta, Motocicleta))
