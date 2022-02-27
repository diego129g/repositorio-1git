
#Desarrollar una calculadora con las siguientes características:
#La calculadora deberá ser capaz de calcular las operaciones de suma, resta, multiplicación, división entera, exponente y modulo o resto.
#La calculadora deberá tener un menú de opciones donde el usuario pueda elegir cual es la operación que desea ejecutar.
#La calculadora deberá solicitar únicamente dos valores por cada operación.
#Requerimientos indispensables:
#El código de este programa deberá de funcionar con una única variable que se llamara numero, es decir, no se permite la implementación de otra variable.

print("dijete el numero de la operacion que desearealizar 1: suma 2:resta 3:multiplicacion 4:dividion 5:potencia 6:modulo ")
opcion=int(input("elija una opcion para realizar la operacion "))
numero1=0
numero2=0

if opcion==1:
 numero1=int(input("dijite el primer numero "))
 numero2=int(input("dijite el segundo numero "))
 resultado=numero1+numero2
 print("el resultado de la suma es",resultado)


if opcion==2:
 numero1=int(input("dijite el primer numero "))
 numero2=int(input("dijite el segundo numero "))
 resultado=numero1-numero2
 print("el resultado de la resta es",resultado)


if opcion==3:
 numero1=int(input("dijite el primer numero "))
 numero2=int(input("dijite el segundo numero "))
 resultado=numero1*numero2
 print("el resultado de la multiplicacion es",resultado)


if opcion==4:
 numero1=int(input("dijite el primer numero "))
 numero2=int(input("dijite el segundo numero "))
 resultado=numero1/numero2
 print("el resultado de la division es",resultado)


if opcion==5:
 numero1=int(input("dijite un numero numero "))
 resultado=numero1*numero1
 print("el resultado de la potencia es",resultado)


if opcion==6:
 numero1=int(input("dijite el primer numero "))
 numero2=int(input("dijite el segundo numero "))
 resultado=numero1%numero2
 print("el residuo de la operacion es",resultado)
