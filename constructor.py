import csv


def guardar_datos_csv(nombre_archivo, Automovil):
    archivo = open(nombre_archivo, "a")
    datos = [(Automovil.__class__, Automovil.__dict__)]
    archivo_csv = csv.writer(archivo)
    archivo_csv.writerows(datos)
    archivo.close()


def recuperar(nombre_archivo):
    vehiculos = []
    archivo = open(nombre_archivo, "r")
    archivo_csv = csv.reader(archivo)
    for vehiculo in archivo_csv:
        vehiculos.append(vehiculo)
    archivo.close()
    return vehiculos


class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

    def __str__(self):
        "Devuelve una cadena representativa del vehiculo"
        return f"Marca: {self.marca} \nModelo: {self.modelo} \nNumero de ruedas: {self.nro_ruedas}"


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        "Devuelve una cadena representativa del automovil"
        return f"Marca: {self.marca} \nModelo: {self.modelo} \nNumero de ruedas: {self.nro_ruedas} \nVelocidad: {self.velocidad} \nCilindrada: {self.cilindrada}"


class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, carga):
        Automovil.__init__(self, marca, modelo, nro_ruedas,
                           velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        "Devuelve una cadena representativa del automovil de carga"
        return f"Marca: {self.marca} \nModelo: {self.modelo} \nNumero de ruedas: {self.nro_ruedas} \nVelocidad: {self.velocidad} \nCilindrada: {self.cilindrada} \nCarga: {self.carga}"


class Particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos):
        Automovil.__init__(self, marca, modelo, nro_ruedas,
                           velocidad, cilindrada)
        self.nro_puestos = nro_puestos

    def __str__(self):
        "Devuelve una cadena representativa del automovil"
        return f"Marca: {self.marca} \nModelo: {self.modelo} \nNumero de ruedas: {self.nro_ruedas} \nVelocidad: {self.velocidad} \nCilindrada: {self.cilindrada} \nNumero de puestos: {self.nro_puestos}"


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo):
        Vehiculo.__init__(self, marca, modelo, nro_ruedas)
        self.tipo = tipo

    def __str__(self):
        "Devuelve una cadena representativa del automovil"
        return f"Marca: {self.marca} \nModelo: {self.modelo} \nNumero de ruedas: {self.nro_ruedas} \nTipo: {self.tipo}"


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo, nro_radios, cuadro, motor):
        Bicicleta.__init__(self, marca, modelo, nro_ruedas, tipo)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor

    def __str__(self):
        "Devuelve una cadena representativa del automovil"
        return f"Marca: {self.marca} \nModelo: {self.modelo} \nNumero de ruedas: {self.nro_ruedas} \nTipo: {self.tipo} \nNumero de radios: {self.nro_radios} \nCuadro: {self.cuadro} \nMotor: {self.motor}"
