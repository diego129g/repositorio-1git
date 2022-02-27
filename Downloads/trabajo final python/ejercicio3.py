#Desarrollar un programa que solicite tres números enteros desde teclado al usuario, posteriormente, el programa deberá determinar e indicar a través de un mensaje en pantalla, cuál de los tres números es el más grande.
#Requerimientos indispensables:
 #El mensaje en pantalla deberá mostrar el número que resultó ser el más grande de los tres, por ejemplo:

numero1=int(input("dijete el primer numero "))
numero2=int(input("dijite el segundo numero "))
numero3=int(input("dijte el tercer numero "))
if numero2<numero1>numero3:
  print("el numero mayor es ",numero1)
elif numero1<numero2>numero3:
  print("el numero mayor es ",numero2)
elif numero1<numero3>numero2:
   print("el numero mayor es ",numero3)