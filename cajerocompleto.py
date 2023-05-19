# 4)Deberá en un solo programa unir el logueo del sistema con los ejercicios 2 y 3. Esto quiere decir que,
# si el ingreso al sistema es exitoso, se mostrará el menú del cajero automático y el usuario podrá comenzar 
# a operar.

usuario= ""
contraseña = ""
contador = 0
saldo = 10000
opcion = ""
deposito = 0
extraccion = 0
#ingreso
print("CAJERO AUTOMATICO")
print("ISPC")
while contador <3:
    usuario = input("Ingrese nombre de Usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if usuario != "admin" or contraseña != "1234":
        print("Usuario o Clave Incorrecta")
        contador = contador + 1
        if contador == 3:
            print("Usuario Bloqueado")
        
    if(usuario == "admin" and contraseña == "1234"): 
        print("Ingreso Exitoso")
        break

#opciones
print("LISTADO DE OPCIONES")
print(" 1 --> Ingreso Dinero \n 2 --> Extraccion de Dinero \n 3 --> Consulta de Saldo \n 4 --> Salir")
while opcion != "4":
    opcion = input("Ingrese la Opcion Deseada ")
    if opcion > "4":
        print("Usted ha elegido una opción incorrecta")
    if opcion == "1":
        print("Usted ha elegido la Opcion 1")
        deposito = int(input("Ingrese el Monto a Depositar :"))
        saldo = saldo + deposito
    if opcion == "2":
        print("Usted ha elegido la Opcion 2")
        extraccion =int( input("Ingrese el Monto a Extraer :"))
        if extraccion <= saldo:
            saldo = saldo - extraccion
        else:
            print("Su Saldo es Insuficiente para realizar esa Extraccion")
    if opcion == "3":
        print("Usted ha elegido la Opcion 3")
        print("Su Saldo es:  ", saldo)
if opcion == "4":
    print("Usted ha elegido la Opcion 4")
    print("Usted ha elegido Salir del Sistema")
    

