#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

letra = ""

letra= input("Dime la letra: \n")

if (letra.isupper()):
    print("La letra es mayúscula")
else:
    print("La letra es minúscula")

