print('''1 - Crie uma lista para cada informação a seguir:
    . Lista de números de 1 a 10;
    . Lista com quatro nomes;
    . Lista com o ano que você nasceu e o ano atual.
''')

lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)

lista_nomes = ["Adriano", "Aline", "Bruno", "Andre"]
print(lista_nomes)

lista_ano = ["1986", "2024"]
print(lista_ano, "\n")
      
print("2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.")
for nome in lista_nomes:
    print(nome)

print("\n3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.")
soma_impares  = 0
for numero in lista:
    if(numero % 2 !=0):
        soma_impares += numero
        print(soma_impares)

# ou da para fazer assim:
soma_impares2 = 0
for i in range(1, 11, 2):
    soma_impares2 += i
    print(soma_impares2)


print("\n4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.")
for i in range(10, 0, -1):
    print(i)

print("\n5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10")
numero = int(input("Digite um número: "))
for i in range(1, 11):
    resultado = i * numero
    print(f"{numero} X {i} = {resultado}")

print("\n6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.")
total_atual = 0
try:
    for numero in lista:
        total_atual += numero
        print(f"Soma dos elementos: {total_atual}") 
except Exception as e:
    print(f"Ocorreu um erro: {e}")     

print("7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.")
lista_valores = [9, 18 ,22]
total = 0
try:
    for numero in lista_valores:
        total += numero
    media = total / len(lista_valores)
    print(f"A média é de {total} divido por {i} é igual a : {media}")
except Exception as e:
   print(f"Ocorreu um erro: {e}")     
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
   
