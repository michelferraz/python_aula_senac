# Escrever um algoritmo que leia o nome de um aluno e as notas das três provas que ele obteve no semestre. No final informar o nome do aluno e a sua média (aritmética)


name = input("Digite o seu nome: ")
ingles = int(input("Digite sua nota de Inglês: "))
portugues = int(input("Digite sua nota de Português: "))
historia = int(input("Digite sua nota de História: "))

media = (ingles+portugues+historia) / 3

if media >= 7:
    print("Sua nota final foi de",media,"e você foi aprovado, Parabens",name,"!")
elif media >=3:
    print("Sua nota final foi de",media,"e você ficou de recuperação, procure seu docente.")
elif media >=1:
    print("Sua nota final foi de",media,"e infelizmente você foi reprovado, boa sorte na próxima.")