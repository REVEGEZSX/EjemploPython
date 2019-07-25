edad = int(input("ingrese su edad "))
genero = input("ingrese su genero ")

if edad >= 18:
    if genero in 'Hh':
        print("Señor Usted es Mayor de edad ")
    elif genero == 'Mm':
        print("Señora Usted es Mayor de edad ")
    else:
        print("DATO ERRONEO ")
else:
    if genero in 'Hh':
        print("Joven Usted es Menor de edad ")
    elif genero in 'Mm':
        print("Señorita Usted es Menor de edad ")
    else:
        print("DATO ERRONEO ")
        
