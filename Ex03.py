print('Nota')

notas = []
for i in range(4):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("Notas digitadas:", notas)
print("Média das notas:", media)
