# dicionário: é um conjunto chave-valor, o valor também pode ser texto ou uma lista, e a chave também pode ser número.
# os valores do dicionário são acessados usando índices. (passa-se a chave e retorna valor)

produtos = ['celular', 'camera', 'fone de ouvido', 'monitor']
precos = [1500, 1000, 800, 2000]

dic_precos = {'celular': 1500,
              'camera': 1000,
              'fone de ouvido': 800,
              'monitor': 2000}
# se passar a chave (passar como índice[]) retorna o valor de um item
# se fizer um for num dicionário retorna só as chaves
preco_celular = dic_precos['celular']
print(preco_celular)
# altera valor de uma chave
dic_precos['celular'] = 2000
print(dic_precos)
# para adicionar um item:
# basta editar um item, se o item não existir ele vai ser adicionado, caso contrário ele vai ser editado. No dicionário não existem itens duplicados.
dic_precos['iphone' ] = 4500
print(dic_precos) 
# deleta item
dic_precos.pop('iphone')
print(dic_precos)
# tamanho
print(len(dic_precos))
# procura um item (procura por chave, não valor)
print('tv' in dic_precos) # retorna false
#  retorna só as chaves
print(dic_precos.keys())
# retorna só os valores
print(dic_precos.values())

####################################################
# exercício:
# crie um sistema de consulta de preços
# dic_precos está no início da pág.
produto_procurado = input('Digite um produto: ')
produto_procurado = produto_procurado.lower()
if produto_procurado not in dic_precos:
    print('Produto não cadastrado!')
else:
     preco = dic_precos[produto_procurado]
     #passei chave, vai retornar valor
     print(f'Produto:{produto_procurado}\nPreço:{preco}')


