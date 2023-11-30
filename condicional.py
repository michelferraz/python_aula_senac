#condição de True ou False (sempre escritos com a primeira letra maiuscula)
# if(se) e ou else (senão), elif (pergunta dentro de outra pergunta)
"""
a = False
print(type(a))
if a:
    print("Verdadeiro")
else:
    print("Falso")


#a>b (a maior do que b), a<b (a menor do que b), a>=b (a maior ou igual que b), a<=b (a menor ou igual que b)
#a!=b (a diferente que b)
#a==b igual com dois sinais de igual se não atribui valor

n1 = 50
n2 = 120
if n1>n2:
    print("n1 é maior do que n2")
else:
    print("n1 é menor do que n2")
nome = input("Digite um nome : ")

if nome == "Jose":
    print("É igual")
else:
    print("É diferente")


nota1, nota2, nota3 = 10, 5, 1
media = (nota1 + nota2 + nota3) / 3
print(media)
if media >= 7:
    print("Aprovado")
elif media <5:
    print("Reprovado")
else:
    print("Apavorado")
"""


#exercicio, digite o nome do aluno e as notas

nome = input ("Ok, Digite seu nome : ")
nota1 = int(input ("Agora digite sua nota de Matemática : "))
nota2 = int(input ("Digite sua nota de Português : "))
nota3 = int(input ("E por fim, digite sua nota de História : "))

media = (nota1 + nota2 + nota3) / 3
print(media)

if media >= 7:
    print("Parabens, você foi Aprovado!")
elif media >=3:
    print("Você vai precisar frequentar uma Recuperação")
elif media >=1:
    print("Infelizmente você foi Reprovado")
else:
    print("MEEEEU DEEEEUS, entregou em branco!")
