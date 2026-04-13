
cp1 = 8.0
cp2 = 6.5
cp3 = 9.0
sp1 = 7.0
sp2 = 8.5
gs = 9.0

menor = cp1
if cp2 < menor:
    menor = cp2
if cp3 < menor:
    menor = cp3

media = ((cp1 + cp2 + cp3 - menor + sp1 + sp2) / 4) * 0.4 + gs * 0.6
media_peso = media * 0.4

print("Média:", round(media, 1))
print("Média com peso:", round(media_peso, 1))