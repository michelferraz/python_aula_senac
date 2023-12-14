'''
Escrever um algoritmo que leia o nome e as três notas obtidas por um aluno durante o semestre. Calcular a sua 
média (aritmética), informar o nome e sua menção aprovado (media >= 7), Reprovado (media <= 5) e Recuperação 
(media entre 5.1 a 6.9).'''

name = (input("Digite seu nome:"))
nHis = int(input("Digite sua nota de História:"))
nGeo = int(input("Digite sua nota de Geografia:"))
nIng = int(input("Digite sua nota de Inglês:"))

media = (nHis + nGeo + nIng) / 3
print(media)

if media >= 7:
    print("Parabéns",name,"você foi Aprovado!")
elif media <= 5:
    print("Que pena",name,"você foi reprovado.")
elif media >= 5.1 and media <= 6.9:
    print(name,"Você está de recuperação.")

