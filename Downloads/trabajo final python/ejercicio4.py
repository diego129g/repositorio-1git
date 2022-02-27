#Desarrollar un programa que imprima en pantalla la sucesión de Fibonacci desde el numero 0 hasta el número 1597, de manera horizontal.
#Es decir, imprimir los siguientes números en pantalla:
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
#Requerimientos indispensables:
#El programa deberá tener un máximo de 7 líneas de código.

numero1,numero2=0,1
while numero2<=1597:
  print(numero1 , numero2 , end=" ")
  numero1 = numero1 + numero2
  numero2 = numero1 + numero2