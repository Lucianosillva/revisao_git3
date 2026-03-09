# def calcular_imposto2(preco, ir= 0.275,csll= 0.35, iss= 0.05):
#     imposto_ir = preco * ir
#     imposto_csll = preco * csll
#     imposto_iss = preco * iss
#     return imposto_ir, imposto_csll, imposto_iss
# ir, csll, iss = calcular_imposto2(1000)
# print(ir, csll, iss,sep='\n')

# tamanho_tela = (1920, 1080)

# exercício

vendas = {
    "André": [1000, 500, 300, 5000, 1500, 80, 3000],
    "Andressa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
    "Alan": [800, 100],
    "Ana": [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65, 60, 70, 70, 70, 200, 180, 100, 120, 110, 130, 140]}
# cada venda o vendedor ganha R$ 2 e 1% do valor de venda
# calcular o valor total de bonus pago e o bonus de cada vendedor

def calcular_bonus(lista_vendas):
    quantidade = len(lista_vendas)
    bonus1 = quantidade * 2
    valor_total = sum(lista_vendas)
    bonus2 = 0.01 * valor_total
    bonus_final = bonus1 + bonus2
    return bonus_final

bonus_total = 0
for vendedor in vendas:
    # retorna a lista de vendas de cada vendedor
    # alternativamente pode-se usar uma estrutura tipo: vendas.items
    # for vendedor, lista_vendas_vendedor in vendas.items():
    # print(vendedor)
    # print(lista_vendas_vendedor)
    # explicando as linhas acima: a primeira variável pega a chave do dicionário e a segunda pega o valor.
    lista_vendas_vendedor = vendas[vendedor]
    bonus_final = calcular_bonus(lista_vendas_vendedor)
    print(f'Vendedor: {vendedor}, bonus: {bonus_final}')
    bonus_total = bonus_total + bonus_final
print(f'Bonus total: {bonus_total}')
    
 
