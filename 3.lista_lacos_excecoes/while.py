#  com for
numero = -1
for _ in range(3):  # Supondo um número máximo de tentativas (3) arbitrário
    numero = int(input("Digite um número positivo: "))
    if numero > 0:
        break

print("Você digitou:", numero)


# com while
numero = -1
while numero <= 0:
    numero = int(input("Digite um número positivo: "))

print("Você digitou:", numero)