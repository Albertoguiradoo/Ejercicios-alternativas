#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);

num1 = 0
num2 = 0
num3 = 0

num1= int(input("Dime el primer  número: \n"))
num2= int(input("Dime el segundo número: \n"))
num3= int(input("Dime el tercero número: \n")) 
 
if (num1>num2 and num2>num3):
    print("El orden sería:", num1, "-", num2, "-", num3 )
if (num1>num3 and num3>num2):
    print("El orden sería:", num1, "-", num3, "-", num2 )
if (num2>num1 and num1>num3):
    print("El orden sería:", num2, "-", num1, "-", num3 )
if (num2>num3 and num3>num1):
    print("El orden sería:", num2, "-", num3, "-", num1 )
if (num3>num2 and num2>num1):
    print("El orden sería:", num3, "-", num2, "-", num1 )
if (num3>num2 and num1>num2):
    print("El orden sería:", num3, "-", num1, "-", num2 )
