#realizar un programa que calcule el IMC de una persona
peso = float(input("ingrese el peso"))
altura = float(input("ingrese la altura"))
IMC = peso/(altura*altura)

if IMC < 18.5:
    print("bajo peso")
elif IMC >= 18.5 and IMC < 25:
    print("normal")
elif IMC >= 25 and IMC < 30:
    print("Sobrepeso")
elif IMC >= 30 and IMC < 35:
    print("Obesidad I")
elif IMC >= 35 and IMC < 40:
    print("Obesidad II")
elif IMC >= 40 and IMC < 50:
    print("Obesidad III")
else: 
    print("Obesidad IV")
    
