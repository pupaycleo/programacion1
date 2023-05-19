#OPCION 2 #
# Opcional 2: solamente permitir el ingreso incorrecto de los datos 3 veces, luego de ello,
# no permitir más ingresos y mostrar por pantalla “Cuenta bloqueada”.

usuario= ""
contraseña = ""
contador = 0
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
        
    

