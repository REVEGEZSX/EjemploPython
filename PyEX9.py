class Empleado:
    def __init__ (self):
        self.codigo = ""
        self.nombre = ""
        self.apellido = ""
        self.salario_base = 0

    def calcular_retencion():
        return self.salario_base * 0.1

    def mostrar_nombre_completo():
        return self.nombre+""+self.apellido

    def calcular_salario_neto():
        if(self.salario_base <= 828116):
            aux = 97132
        else:
            aux = 0
        return self.salario_base + aux

Empleado.codigo = input("ingrese el codigo")
Empleado.nombre = input("ingrese el nombre")
Empleado.apellido = input("ingrese el apellido")
Empleado.salario_base = int(input("ingrese su salario"))

print("la retencion ", calcular_retencion())
print("nombre completo ", mostrar_nombre_completo())
print("salario neto ", calcular_salario_neto())
