
def pode_aprovar(idade, renda, valor):
    return idade > 18 and valor <= renda * 20

def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    else:
        return 0.10

def calcular_parcela(valor, taxa, n):
    return valor * (taxa * (1 + taxa)**n) / ((1 + taxa)**n - 1)

def calcular_total(parcela, n):
    return parcela * n

def calcular_juros(total, valor):
    return total - valor

nome = "Maria"
idade = 25
renda = 3000
valor = 20000
parcelas = 12

if pode_aprovar(idade, renda, valor):
    taxa = definir_taxa(parcelas)
    parcela = calcular_parcela(valor, taxa, parcelas)
    total = calcular_total(parcela, parcelas)
    juros = calcular_juros(total, valor)

    print("APROVADO")
    print("Cliente:", nome)
    print("Valor financiado:", valor)
    print("Taxa:", taxa)
    print("Parcela:", round(parcela, 2))
    print("Total pago:", round(total, 2))
    print("Juros:", round(juros, 2))
else:
    print("EMPRÉSTIMO NEGADO")