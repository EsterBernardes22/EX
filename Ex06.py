print('Média')

medias = []

for i in range(6):
    notas = []
    for j in range(4):
        nota = float(input(f"Digite a {j + 1}ª nota do {i + 1}º aluno: "))
        notas.append(nota)

    media = sum(notas) / len(notas)
    medias.append(media)

alunos_aprovados = sum(1 for media in medias if media >= 7.0)

print("Número de alunos com média maior ou igual a 7.0:", alunos_aprovados)
