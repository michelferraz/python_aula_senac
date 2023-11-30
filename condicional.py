#condição de True ou False (sempre escritos com a primeira letra maiuscula)
# if(se) e ou else (senão)

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
