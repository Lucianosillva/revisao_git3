email = 'EMAIL_falso@gmail.com'
print(email.lower())# transforma o texto em mínuscula
print(email.find('@'))# se encontrar o elemento retorna a sua posição, se não encontrar retorna -1
print(email[12]) # mostra o que tem em determinada posição.
posicao = email.find('@')
print(posicao) # retorna o índice da posição

# exemplo prático
# sabendo a posição de cada elemento de um texto podemos pegar pedaços de um texto, como por exemplo descobrir qual os servidores que as pessoas mais usam em uma determinada base de dados, e com isso personalizar o envio de e-mails de acordo com cada servidor.
servidor = email[posicao:]
# servidor = email[posicao+1:] retorna tudo o que tiver depois da posição
# servidor = email[:posicao] # retorna tudo o que tiver antes da posição
print(servidor) # retorna tudo a partir da posição, no caso o nome do servidor.
# se quiser saber o nome do e-mail?
nome_email = email[:posicao]
print(nome_email)

# tamanho de um texto
tamanho = len(email)
print(tamanho)

# trocar um pedaço de texto
email_trocado = email.replace('gmail.com', 'hotmail.com')
print(email_trocado)

# primeiras letras maiúsculas
nome2 = 'luciano silva'
print(nome2.capitalize()) # Luciano silva
print(nome2.title()) # Luciano Silva


# delimitação para melhor visualização
print('####################################')

# formatações numéricas (devem ser feitas no final, nos prints, pois a formatação transforma a variável em texto str(nome_da_variavel) e com texto não é possível fazer contas.)
# Exemplo
faturamento = 1000
custo = 700
novas_vendas = 300
faturamento = faturamento + novas_vendas
imposto = faturamento * 0.1
lucro = faturamento - custo
restituicao = imposto * 0.1
print(faturamento)
print(lucro)
margem_lucro = lucro / faturamento
print(f'margem_lucro: {margem_lucro:.1%}')
print(restituicao)
# (:) formatação, (,) separador de milhar, (.) casa decimal, (2) quantidade de casas decimais, (f) float
print(f'o faturamento foi de R$ {faturamento:,.2f}')

################################################
# exercícios

# Entrada de dados
nome2 = 'Luciano Silva'
email2 = 'email_falso@gmail.com'

# 1) descubra o servidor do e-mail
pos = email2.find('@')
print(f'Nome do servidor: {email2[pos:]}')

# 2) pegar primeiro nome do usuário (tipo olá (nome))
pos2 = nome2.find(' ')
print(f'Olá {nome2[:pos2]}')

# 3) construa uma mensagem: usuário (nome) cadastrado com sucesso com e-mail tal
print(f'Usuário {nome2[:pos2]} cadastrado com sucesso com o e-mail: {email2}')

# 4) construa uma mensagem: enviamos um link de confirmação para o e-mail, como por exemplo: l*******@gmail.com
primeira_letra = email2[0]
print(f'Enviamos um link de confirmação para o e-mail: {primeira_letra}***{email2[pos:]}')
#pos3 = email2.replace(email2[:pos], '***')
#comprimento = len(email2[:pos])
#for item in email2[:pos - comprimento +1]:
    #print(f'Enviamos um link de confirmação para o e-mail: {email2[0]}{pos3}')









