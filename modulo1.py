#Cree la clase "cliente" que contiene 4 metodos y 4 atributos de instancia
class Cliente():
    def __init__(self, nombre, apellido, edad, nro_cliente):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nro_cliente = nro_cliente
        self.direcciones = []
#Este metodo es un magic method que permite obtener una representación en forma de cadena de un objeto cliente
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}, Edad: {self.edad}, Número de Cliente: {self.nro_cliente}"
# Este metodo permite a un cliente agregar una dirección a su lista de direcciones. 
# Las direcciones se almacenan en la lista direcciones del objeto cliente
    def agregar_direccion(self, direccion):
        self.direcciones.append(direccion)
        print(f"Nueva dirección agregada: {direccion}")
#Imprime un mensaje indicando que el cliente ha realizado una compra
    def comprar(self):
        print(f"El cliente {self.nombre} {self.apellido} ha realizado una compra")


