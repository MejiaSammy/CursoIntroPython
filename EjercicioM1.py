# program.py
from turtle import left


sum = 1 + 2
print('La suma es: ')
print(sum)

## Producto
sum = 1 + 2 # 3
product = sum * 2
print('El producto es: ')
print(product)

## Tipos de Datos
planetas_en_el_sistema_solar = 8 # int, plutón era considerado un planeta pero ya es muy pequeño
distancia_a_alfa_centauri = 4.367 # float, años luz
type(distancia_a_alfa_centauri)
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11" #string

## Operadores
left_side = 10
right_side = 5
left_side / right_side # 2

## Fecha
#Importar la biblioteca
from datetime import date
#Obtenemos la fecha de hoy
date.today()
#Imprimimos la fecha en consola
print('La fecha de hoy es: ')
print(date.today())

## Conversion de Tipo de Datos
print("Today's date is: " + str(date.today()))

## Entrada del usuario
print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Hola " + name)

## Calculadora
print("Bienvenido a Calculadora")
first_number = input("Ingrese el Primer número: ")
second_number = input("Ingrese el Segundo número: ")
suma=(int(first_number) + int(second_number))
print("La suma de los dos numeros es: "+str(suma))