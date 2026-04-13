
estado = 1
peso_ton = 10
codigo = 15

peso_kg = peso_ton * 1000

if 10 <= codigo <= 20:
    preco_kg = 100
elif 21 <= codigo <= 30:
    preco_kg = 250
else:
    preco_kg = 340

preco_carga = peso_kg * preco_kg

if estado == 1:
    imposto = preco_carga * 0.35
elif estado == 2:
    imposto = preco_carga * 0.25
elif estado == 3:
    imposto = preco_carga * 0.15
elif estado == 4:
    imposto = preco_carga * 0.05
else:
    imposto = 0

total = preco_carga + imposto

print("Peso em kg:", peso_kg)
print("Preço da carga:", preco_carga)
print("Imposto:", imposto)
print("Total:", total)