
numeros = []
pares = []
impares = []


while True:
    numero = int(input("Digite um número (ou 0 para encerrar): "))

    if numero == 0:
        break

    numeros.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

numeros.sort()
pares.sort()
impares.sort()

print("Números em ordem crescente:", numeros)
print("Números pares em ordem crescente:", pares)
print("Números ímpares em ordem crescente:", impares)

soma = sum(numeros)
print("Soma dos valores:", soma)
