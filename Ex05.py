print('Números')

numeros = []
PAR = []
impar = []

for i in range(20):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)

    if numero % 2 == 0:
        PAR.append(numero)
    else:
        impar.append(numero)

print("Números digitados:", numeros)
print("Números pares:", PAR)
print("Números ímpares:", impar)
