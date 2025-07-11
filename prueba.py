""""
Nombre: Juan Pablo Quijano Martinez
Fecha: 11/08/2025
Descripcion: Este programa permite al usuario calcular el promedio de 5 voltajes
"""

print ('Vamos a calcular el promedio de 5 Voltajes')
voltaje1 =  float(input('Ingresa el primer Voltaje :'))
voltaje2 =  float(input('Ingresa el segundo Voltaje :'))
voltaje3 =  float(input('Ingresa el tercer  voltaje :'))
voltaje4 =  float(input('Ingresa el cuarto Voltaje :'))
voltaje5 =  float(input('Ingresa el quinto Voltaje :'))
voltaje_total = (voltaje1 + voltaje2 + voltaje3 + voltaje4 +voltaje5) / 5
if voltaje_total >= 220:
    print (f'El promedio de su voltaje total es mayor que 220 y es igual a {voltaje_total}')
else:
    print (f'El promedio de su voltaje total es menor a 220 es igual a {voltaje_total}')