
def calcular_horas_extras(salario, horas):
    return salario * 0.015 * horas

def calcular_descontos_faltas(salario, faltas):
    return salario * 0.02 * faltas

def calcular_bonus(cargo, recebe):
    if recebe == 's':
        if cargo == 1:
            return 1000
        elif cargo == 2:
            return 500
        elif cargo == 3:
            return 300
        else:
            return 100
    return 0

nome = "João"
cargo = 2
salario = 3000
horas = 10
faltas = 2
bonus_resp = 's'

extra = calcular_horas_extras(salario, horas)
desconto = calcular_descontos_faltas(salario, faltas)
bonus = calcular_bonus(cargo, bonus_resp)

bruto = salario + extra + bonus
final = bruto - desconto

print("Salário bruto:", bruto)
print("Acréscimos:", extra + bonus)
print("Descontos:", desconto)
print("Salário final:", final)