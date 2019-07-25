num1 = int(input("Dijite primer numero "))
num2 = int(input("Dijite segundo numero "))
operacion = int(input("1=suma, 2=resta, 3=multiplicacion, 4=division "))
if operacion == 1:
    print(num1+num2)
elif operacion == 2:
    print(num1-num2)
elif operacion == 3:
    print(num1*num2)
elif operacion == 4:
    print(num1/num2)
else:
    print("ingreso un valor erroneo")
