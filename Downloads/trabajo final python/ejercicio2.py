# La compañía multinacional Las Palmeras, solicita un sistema que determine los días de vacaciones a los que tiene derecho un trabajador, tomando en cuenta las siguientes características:
# Departamento de atención al cliente. (clave 1)
# Departamento de logística. (clave 2)
# Gerencia. (clave 3)

# Trabajadores con clave 1 (Atención al cliente):
# Con 1 año de servicio, reciben 6 días de vacaciones.
# Con 2 a 6 años de servicio, reciben 14 días de vacaciones.
# A partir de 7 años, reciben 20 días de vacaciones

# Trabajadores con clave 2 (Logística):
# Con 1 año de servicio, reciben 7 días de vacaciones.
# Con 2 a 6 años de servicio, reciben 15 días de vacaciones.
# A partir de 7 años, reciben 22 días de vacaciones.

# Trabajadores con clave 3 (Gerencia):
# Con 1 año de servicio, reciben 10 días de vacaciones.
# Con 2 a 6 años de servicio, reciben 20 días de vacaciones.
# A partir de 7 años, reciben 30 días de vacaciones
# requerimientos indispensables:
# El sistema debe de solicitar el “Nombre”, “Clave del departamento”, y “antigüedad “del trabajador desde teclado.
# Posteriormente el programa debe mostrar un mensaje en pantalla, que contenga el nombre del trabajador y los días de vacaciones a los que tiene derecho.
numerodeclave1 = 0
numerodeclave2 = 0
numerodeclave = int(input("elija el numero de la clave debe de ser un numero entre el 1 y el 3 "))

añostrabajados = int(input(" digite los años trabajados "))

if numerodeclave == '1':
    añostrabajados
elif añostrabajados == 1:
    trabajador = (input(" digite el nombre del trabjador "))
    print("los dias de vacaciones de ", trabajador, " son 6 ")

elif añostrabajados >= 2 and añostrabajados <= 6:
    trabajador = (input(" digite el nombre del trabjador "))
    print("los dias de vacaciones de ", trabajador, " son 14 ")

elif añostrabajados > 7:
    trabajador = (input(" digite el nombre del trabjador "))
    print("los dias de vacaciones de ", trabajador, " son 20 ")

if numerodeclave1 == '2':
    añostrabajados
elif añostrabajados == 1:
    trabajador = (input(" digite el nombre del trabjador "))
    print("los dias de vacaciones de ", trabajador, " son 7 ")

elif añostrabajados >= 2 and añostrabajados <= 6:
    trabajador = (input(" digite el nombre del trabjador "))
    print("los dias de vacaciones de ", trabajador, " son 15 ")

elif añostrabajados > 7:
    trabajador = (input(" digite el nombre del trabjador "))
    print("los dias de vacaciones de ", trabajador, " son 22 ")

if numerodeclave2 == '3':
    añostrabajados
elif añostrabajados == 1:
    trabajador = (input(" digite el nombre del trabjador "))
    print("los dias de vacaciones de ", trabajador, " son 10 ")

elif añostrabajados >= 2 and añostrabajados <= 6:
    trabajador = (input(" digite el nombre del trabjador "))
    print("los dias de vacaciones de ", trabajador, " son 20 ")

elif añostrabajados > 7:
    trabajador = (input(" digite el nombre del trabjador "))
    print("los dias de vacaciones de ", trabajador, " son 30 ")
