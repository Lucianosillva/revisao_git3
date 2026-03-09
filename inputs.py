# sempre que for receber dados númericos tem que colocar int ou float dentro do input: (número = int(input('Digite um número: )))




# Entrada de dados
nome2 = input('Digite seu nome e sobrenome:')
nome2 = nome2.lower()

email2 = input('Digite seu e-mail: ')
email2 = email2.lower()

# 1) descubra o servidor do e-mail
pos = email2.find('@')
print(f'Nome do servidor: {email2[pos:].replace('@', '')}')

# 2) pegar primeiro nome do usuário (tipo olá (nome))
pos2 = nome2.find(' ')
print(f'Olá {nome2.title()[:pos2]}')

# 3) construa uma mensagem: usuário (nome) cadastrado com sucesso com e-mail tal
print(f'Usuário {nome2.title()[:pos2]} cadastrado com sucesso com o e-mail: {email2}')

# 4) construa uma mensgagem: enviamos um link de confirmação para o e-mail, como por exemplo: l*******@gmail.com
primeira_letra = email2[0]
print(f'Enviamos um link de confirmação para o e-mail: {primeira_letra}***{email2[pos:]}')
#pos3 = email2.replace(email2[:pos], '***')
#comprimento = len(email2[:pos])
#for item in email2[:pos - comprimento +1]:
    #print(f'Enviamos um link de confirmação para o e-mail: {email2[0]}{pos3}')
#email3 = list(email2)
#pos3 = email3.find(email2[0])
#print(pos3)

print('alterando este código...')









