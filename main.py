"""importo la clase cliente, con todos sus metodos y atributos desde el modulo1 
mediante la siguiente sentencia"""
from modulo1 import * 
#Creo dos clientes
cliente1 = Cliente("Ezequiel", "Paz", 25, 1)
cliente2 = Cliente("Saul", "Goodman", 50, 2)
#Imprimp por pantalla mediante el magic method str a los dos clientes creados
print(cliente1.__str__())
print(cliente2.__str__())
#Llamo al metodo "agregar_direccion", pasandole el parametro correspondiente
cliente1.agregar_direccion("Calle falsa 123")
cliente2.agregar_direccion("Los pollos hermanos 321")
#Llamo al metodo comprar
cliente1.comprar()
cliente2.comprar()
