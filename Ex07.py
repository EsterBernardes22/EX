print('Calculo')

numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)

soma = sum(numeros)
multiplicacao = 1
for numero in numeros:
    multiplicacao *= numero

print("Soma dos números:", soma)
print("Multiplicação dos números:", multiplicacao)
print("Números digitados:", numeros)
