class Empleado:
    def __init__ (self):
        self.codigo = ""
        self.nombre = ""
        self.apellido = ""
        self.salario_base = 0

    def calcular_retencion(self):
        return print("La retencion es de ",self.salario_base * 0.1)
    def mostrar_nombre_completo(self):
        return print("nombre completo ",self.nombre+" "+self.apellido)
    def calcular_salario_neto(self):
        if(self.salario_base <= 828116):
            A = " SALARIO NETO ",(self.salario_base + 97032)-(self.salario_base*0.1)
        else:
            A = " SALARIO NETO ",self.salario_base-(self.salario_base*0.1)
        return print(A)

a = Empleado()

a.codigo = input("ingrese el codigo ")
a.nombre = input("ingrese el nombre ")
a.apellido = input("ingrese el apellido ")
a.salario_base = int(input("ingrese su salario "))

a.calcular_retencion()
a.mostrar_nombre_completo()
a.calcular_salario_neto()
