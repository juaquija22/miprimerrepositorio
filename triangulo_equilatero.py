""""
Nombre: Juan Pablo Quijano Martinez
Fecha: 11/08/2025Descripcion: Este programa permite al usuario calcular el area de un triangulo equilatero"""


print ('vamos a calcular el area de un triangulo equilatero')
lado1= float(input('Ingresa la medida de uno de los lados en cm de tu triangulo equilatero : '))
area = (1.73 / 4 ) * lado1 * lado1
print (f'el area de tu triangulo equilatero es {area}')
if area >= 1000:
    print (' El area de su triangulo es mayor a 1000 ')
