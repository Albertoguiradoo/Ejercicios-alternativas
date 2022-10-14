#Escribe un programa que pida un nombre de usuario y una contraseña y si se ha
#introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.

usuarioSecreto = "Pepe"
contraSecreta = "asdasd"

usuario=input("Dime el usuario: \n")
contraseña= input("Ahora, dime la contraseña: \n")

print (usuario!=usuarioSecreto)

while (usuario!=usuarioSecreto or contraseña!=contraSecreta):
    
    if(usuario!=usuarioSecreto):
        print("Usuario erróneo, intentelo de nuevo.")
        usuario= str(input("Dime el usuario: \n"))
    if(contraseña!=contraSecreta):
        print("Contraseña errónea, intentelo de nuevo.")
        contraseña= str(input("Dime la contraseña: \n"))

print("Felicidades, has entrado en el sistema.")
