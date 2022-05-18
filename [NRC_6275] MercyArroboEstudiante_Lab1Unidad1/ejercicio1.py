

#Ingresar el radio de un círculo del usuario y calcule el área.

radio = int(input("Ingrese el radio del círculo para calcular el area: "))
pi=3.1416
area = pi*(radio*radio)
print("El área del circulo es: ",area)

#Calcular el teorema de Pitágoras
catetopuesto = int(input("Ingrese un valor: "))
catetoadyacente = int(input("Ingrese un valor: "))
hipotenusa = catetopuesto*catetopuesto+catetoadyacente*catetoadyacente
print("La hipotenusa es: ", hipotenusa)

#Ingresar dos números y realizar todas las operaciones aritméticas.
dato1= int(input("Ingrese primer número: "))
dato2= int(input("Ingrese segundo número: "))
#Operación sumar
suma = dato1 + dato2
#Operación restar
resta = dato1 - dato2
#Operación multplicar
multiplicar = dato1 * dato2
#Operación dividir
dividir = dato1 / dato2

#Salida
print("La suma es: ",suma)
print("La resta es: ",resta)
print("La multiplicación es: ",multiplicar)
print("La división es: ",dividir)

#Preguntar al usuario su nombre y lo salude con su nombre.
nombre = input("Ingrese tu primer nombre: ")
print("Hola como estás",nombre)

#Ingresar dos ángulos de un triángulo y encontrar el tercer ángulo.
angulo1 = int(input("Ingrese el primer ángulo: "))
angulo2 = int(input("Ingrese el segundo ángulo: "))
triangulo = 180
suma = triangulo - (angulo1+angulo2)
print("El tercer ángulo es: ", suma)

