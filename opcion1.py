# #1)Escribir un programa que permita validar el ingreso a un sistema. Se deberá solicitar el ingreso 
#por teclado de nombre de usuario y contraseña. Será valido como nombre de usuario “admin” y 
#como contraseña “1234”. Si el ingreso es correcto deberá mostrar por pantalla el mensaje “Ingreso exitoso”.

#Opcional 1: permitir como usuario valido también su propio nombre y su propia contraseña.



# Opcional 3: Puede incluir parte de la lógica del programa en una o más funciones.
#IMPORTANTE:  Aquellos que deseen publicar una solución propuesta para no dispersarnos pueden hacerlo
# en este hilo así es más fácil de aunar en un solo hilo todas las soluciones propuestas.

#OPCION 1#
registroUsuario = ""
registroContraseña = ""
usuario = ""
contraseña = ""
contador = 0
registroUsuario = input("Ingrese un nombre de Usuario: ")
registroContraseña = input("Ingrese una contraseña : ")
while contador <3:
    usuario = input("Ingrese nombre de Usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if usuario != registroUsuario or contraseña != registroContraseña:
        print("Usuario o Clave Incorrecta")
        contador = contador + 1
        if contador == 3:
            print("Usuario Bloqueado")
        
    if(usuario == registroUsuario and contraseña == registroContraseña): 
        print("Ingreso Exitoso")
        break



