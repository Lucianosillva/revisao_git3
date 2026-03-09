import statistics

# # Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
# lista_notas = []
# for item in range(2):
#     notas = float(input('Digite a nota: '))
#     lista_notas.append(notas)
# media = statistics.mean(lista_notas)
# if media >= 7 and media != 10:
#     print(f'Média {media}\nAprovado!')
# elif media == 10:
#     print(f'Média {media}\nAprovado com distinção!')
# else:
#     print(f'Média {media}\nReprovado!')
  
lista_notas = []
for item in range(3):
    notas = float(input('digite a nota: '))
    lista_notas.append(notas)
media = statistics.mean(lista_notas)
if media >= 7 and media != 10:
    print(f'média {media}\nAprovado!')
elif media == 10:
    print(f'media {media}\nAprovado com distinção!')
else:
    print(f'média {media}\nReprovado!')
    # esta linha foi modificada no ramo novabranch
    
    #testando push da master
    #esta linha foi modificada no ramo master.
    
    # esta linha foi modificada no ramo novabranch
    
    #testando atualização.
