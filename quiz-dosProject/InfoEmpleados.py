#Datos Empleado
nombre = "Luis Vejarano"
input("Ingrese su nombre:")
print("Nombre :" + nombre)

def calcularSalario(nombre, dias, salario):
prima = salario * dias / 360
cesantias = salario * dias_laborados/ 360
intereses_cesantias = cesantias * 0.12 dias_laborados
vacaciones = salario * dias labarados / 720
liquidacion_total = prima + cesantias + intereses_cesantias + vacaciones

return prima, cesantias, intereces_cesantias, vacaciones, liquidacion_total

if __name__== "__main__":
nombre = ("Luis Vejarano")
dias = int(7)
salaraio = float("785000")

prima, cesantias, intereces_cesantias, vacaciones, liquidacion_total = calcularSalario(nombre,dias,salario)
print(f"Señor {nombre} para los {dias} dias laborados y salario ${salario:.2f}, su liquidacion se compone asi:")
print(f"Prima: ${prima:.2f}")
print(f"cesantias: {cesantias:.2f}")
print(f"intereses_cesantias:${intereces_cesantias:.2f}")
print(f"vacaciones: {vacaciones:.2f}")
print(f"Liquidacion_total: {liquidacion_total:.2f}")