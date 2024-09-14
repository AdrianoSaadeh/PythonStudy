print("1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.")
dicionario_pessoas = {'nome': 'Adriano', 'idade': 38, 'cidade': 'Canoas', }
print(dicionario_pessoas['nome'])

print('''\n2 - Utilizando o dicionário criado no item 1:
    Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
    Adicione um campo de profissão para essa pessoa;
    Remova um item do dicionário.''')

# Atualização de Idade
dicionario_pessoas['idade'] = 39
print(dicionario_pessoas['idade'])

# Adicionando Profissão
dicionario_pessoas['profissao'] = 'QA'
print(dicionario_pessoas)

# Remoção de Elemento
del dicionario_pessoas['idade']
print(dicionario_pessoas)

("\n3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.")
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    dic_numeros_quadrado = {numero: numero * numero}
print(dic_numeros_quadrado)


print("\n3 - Crie um dicionário para representar números e seus quadrados de 1 a 5.")
numeros = [1, 2, 3, 4, 5]
dic_numeros_quadrado = {}  # Inicializa o dicionário vazio
for numero in numeros:
    # Adiciona cada número e seu quadrado ao dicionário
    dic_numeros_quadrado[numero] = numero * numero
print(dic_numeros_quadrado)

# ou solução mais simples da ALura
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

print("\n4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.")
print(dicionario_pessoas)
if 'cpf' in dicionario_pessoas:
    print("Existe a chave")
else:
    print("Não existe")

print("\n5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.")
frase = "Python se tornou uma das linguagens de programação mais populares pois Python é mais otimizado."
contagem_palavras = {}
palavras = frase.split()
print(frase)
print(palavras)
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)
