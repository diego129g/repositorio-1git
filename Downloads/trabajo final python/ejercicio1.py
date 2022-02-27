# Desarrollar un programa que solicite un numero entero desde el teclado al usuario, posteriormente, el programa deberá determinar e indicar a través de un mensaje si el número introducido es par o impar.

# Requerimientos indispensables:

# El mensaje en pantalla deberá mostrar la frase el número es par o impar, según sea el caso, junto con el número que el usuario introdujo desde teclado, por ejemplo:

# El numero 2 es par.”
# “El numero 3 es impar.”
print("introduzca un numero para determinar si es par o impar ")

numero = int(input())
if numero % 2 == 0:

    print("el numero ", numero, "es par ")

else:
    print("el numero ", numero, " es impar ")
