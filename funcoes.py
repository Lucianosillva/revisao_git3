lista_precos = [1500, 1000, 800, 2000]
total_imposto = 0 # acumulado (sempre que tiver acumulado, criar fora do for)
# def calcular_imposto(preco):
#         if preco > 2000:
#             imposto = preco * 0.2
#         elif preco > 1000:
#             imposto = preco * 0.15
#         else:
#             imposto = preco * 0.1
#         print(f'Preço: {preco}, Imposto: {imposto}')
#         return imposto
# for preco in lista_precos:
#     imposto = calcular_imposto(preco)
#     total_imposto = total_imposto + imposto
# print(f'Imposto acumulado: {total_imposto}')

def calcular_imposto2(preco, ir= 0.275,csll= 0.35, iss= 0.05):
    imposto_ir = preco * ir
    imposto_csll = preco * csll
    imposto_iss = preco * iss
    return imposto_ir, imposto_csll, imposto_iss
resposta = calcular_imposto2(1000)
print(resposta)
