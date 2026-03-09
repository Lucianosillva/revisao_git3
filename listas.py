vendas = [100, 50, 130, 80, 120, 200]
# índices negativos começam da direita para esquerda, é útil para pegar o último item da lista por exemplo.
#print(vendas[-1]) retorna 200
#print(vendas[-2]) retorna 120
total_vendas = sum(vendas)
print(total_vendas)
quantidade = len(vendas)
print(quantidade)
valor_min = min(vendas)
print(valor_min)
valor_max = max(vendas)
print(valor_max)
posicao = vendas.index(130)
print(posicao)
print(vendas[:2]) # não pega o último índice (2)
print(vendas[3:]) # do índice escolhido até final

# Exemplo prático -> usar a lista para saber se um produto já está cadastrado no sistema:
produtos = ['iphone', 'ipad', 'airpod']
#produto_usuario = input('Digite o nome do produto: ')
print('iphone' in produtos) # retorna True

# Alterar valores de uma lista:
precos = [4000, 8000, 200]
precos[0] = 4500 # altera o preço do índice 0 para 4500
print(precos)
precos[0] = precos[0] * 1.1 # aumenta o preço do índice 0 em 10%
print(precos)

# Adiciona um novo item no final da lista:
produtos.append('macbook')
precos.append(11000)
print(produtos)
print(precos)
# 
# remove item
produtos.remove('macbook') # remove de acordo com o valor do item
precos.pop() # remove o último índice da lista
precos.pop(-1) # remove de acordo com o índice da lista, pode usar índice positivo também.
print(produtos)
print(precos)

# insere um item na posição desejada
produtos.insert(1, 'airpod')
print(produtos)

# contar valores
print(produtos.count('airpod')) # conta os airpod da lista

# ordenar
precos.sort() # ordena em ordem crescente
# neste caso não é preciso criar uma variável para receber a função, basta atribuir à variável já existente.
#precos.sort(reverse=True) ordena em ordem decrescente.
print(precos)
