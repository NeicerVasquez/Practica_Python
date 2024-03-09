'''
Ejercicio 1: Conversión de temperaturas
Crea un programa que pida al usuario ingresar una temperatura en grados Celsius y conviértela a grados Fahrenheit utilizando la fórmula: Fahrenheit = (Celsius * 9/5) + 32. Imprime el resultado en la consola.
'''
temp = int(input('Ingresa grados C°: '))
conv = (temp * (9/5)) + 32
print(f'Los grados {temp} Celsius a Fahrenheit son: {conv}')