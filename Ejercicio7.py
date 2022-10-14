#Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:
# El exponente sea positivo, sólo tienes que imprimir la potencia.
# El exponente sea 0, el resultado es 1.
# El exponente sea negativo, el resultado es 1/potencia con el exponente



base1 = 0
exponente = 0

base1 = int(input("Dime el número: \n"))
exponente = int(input("Dime el exponente: \n"))

if(exponente>0):
    print(base1,"^",exponente,"=", base1**exponente)
if(exponente==0):
    print(base1,"^",exponente,"=1")
if(exponente<0):
    print(base1,"^",exponente,"=", 1/(base1**-exponente))

