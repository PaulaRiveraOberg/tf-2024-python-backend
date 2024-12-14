##########################
#    Sintaxis básica
##########################

# Variables
a = 10
b = 20

# Operaciones y sentencias
print(a + b)

# Tipos de datos
entero = 10
flotante = 10.5
cadena = "Hola"
booleano = True
lista = [1, 2, 3]
diccionario = {"nombre": "Juan", "edad": 20}

# Condicionales
if a > b:
    print("a es mayor que b")
else:
    print("a es menor o igual que b")

# Bucles
for i in range(10):
    print(i)

##########################
#       Funciones
##########################

# definición de una función
def saludar(nombre="Desconocido"):
    print("Hola", nombre)

# invocación de una función
saludar("Juan")
saludar()

# Parametros por referencia
def modificar_lista(lista):
    lista.append(4)

lista = [1, 2, 3]
modificar_lista(lista)
print(lista)

# retorno de valores
def sumar(a, b):
    return a + b

resultado = sumar(1, 2)
print(resultado)

##########################
#       Manejo de excepciones
##########################

# captura de una excepción general
try:
    a = 10
    b = 0
    print(a / b)
except Exception as e:
    print("Error:", e)
    
# captura de una excepción específica
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Error: división por cero")

# uso de else
try:
    a = 10
    b = 1
    print(a / b)
except ZeroDivisionError:
    print("Error: división por cero")
else:
    print("No ocurrió ninguna excepción")

# uso de finally
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Error: división por cero")
finally:
    print("Fin del bloque try")


##########################
#       Modulos
##########################

# importación de un modulo con alias    
import modulo.funciones as funciones

print(funciones.raiz_cuadrada(16))

# importación de una función específica
from modulo.funciones import raiz_cuadrada

print(raiz_cuadrada(16))

# importación de todas las funciones
from modulo.funciones import *  

print(raiz_cuadrada(16))

##########################
# Clases y objetos
##########################

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola, me llamo", self.nombre)

# creación de un objeto
persona = Persona("Juan", 20)
persona.saludar()

# herencia
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def mostrar_sueldo(self):
        print("Mi sueldo es", self.sueldo)

# creación de un objeto
empleado = Empleado("Juan", 20, 1000)
# invocación de los métodos de la clase Persona
empleado.saludar()
# invocación de los métodos de la clase Empleado
empleado.mostrar_sueldo()

##########################
#    Estructuras de datos
##########################

lista = [1, 2, 3]
tupla = (1, 2, 3)
diccionario = {"nombre": "Juan", "edad": 20}
conjunto = {1, 2, 3}

# operaciones con listas
lista.append(4)
lista.remove(2)
lista.insert(0, 0)
lista.sort()
lista.reverse()

# operaciones con diccionarios
diccionario["nombre"] = "Pedro"
diccionario.pop("edad")
diccionario.update({"edad": 21})

# operaciones con conjuntos
conjunto.add(4)
conjunto.remove(2)
conjunto.update({4, 5, 6})

