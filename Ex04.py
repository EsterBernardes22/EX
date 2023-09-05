print('Vetor')

vetor = []

for i in range(10):
    caractere = input(f"Digite o {i + 1}º caractere: ")
    vetor.append(caractere)

consoantes = [c for c in vetor if c.isalpha() and c.lower() not in 'aeiou']
quantidade_consoantes = len(consoantes)

print("Caracteres digitados:", vetor)
print("Consoantes:", consoantes)
print("Quantidade de consoantes:", quantidade_consoantes)
