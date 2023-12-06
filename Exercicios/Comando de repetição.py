# comandos de repetição
"""
for x in range(1,10): #para mostrar uma lista de 1 a 10 (nao mostra o ultimo, pois começa no 0)
    print(x)

listanomes = ["Maria","Ana","Pedro","João"] #o mesmo de cima só que com nomes)
for x in listanomes:
    print(x)

numeros = (3,6,4,9)
soma = 0 #soma foi usado para formar a formula junto com o 0, assim vai somar apenas os numeros em cima, se mudar o 0 da soma ele vai somar junto aos de cima)
for x in numeros:
    soma += x #o comando += é a mesma coisa que usar a função soma, ex: soma = soma + x
    print(soma) #aqui ele soma dentro do "for", mostrando as somas separadas
print(soma) #aqui ele soma fora do "for", mostrando todas as somas juntas

i=0
while i<10: #formula para mostrar em sequencia
    print(i)
    i+=1

lista = ["a", "b", "c", "d", "e","f"]
i=0
while i < len(lista):
    print(i,"-",lista[i])
    i+=1
"""

# brake (parar uma linha de comando, por exemplo: parar uma busca em algum lugar especifico) e continue (para continuar uma operação/comando)

listacarros = ["Opala", "Chevette", "Zafira", "Mustang", "Omega", "Astra", "Fusca", "Uno", "kadet"]
line = "______________________________________"
print(line)
for x in listacarros:
    print(x)


print(line)
i = 0
while i <len(listacarros):
    if listacarros[i] == "Omega":
        print(i, "-", listacarros[i])
        break
    i+=1


print(line)
i = 0
while i <len(listacarros):
    print(i,"-",listacarros[i])
    if listacarros[i] == "Omega":
        break
    i+=1


print(line)
for x in listacarros:
    if x == "Omega":
        continue
    print(x)


print(line)
i=0
while i <len(listacarros): #aqui ele faz a lista até chegar no Omega
    print(i,"-",listacarros[i])
    if listacarros[i] == "Omega":
        break
    i+=1
while i <len(listacarros): #aqui ele inicia a lista a partir do omega
    print(listacarros[i])
    i+=1


print(line) #ordenar lista, se usa sort (variavel.sort) para ordenar em ordem alfabetica
print(listacarros)
listacarros.sort() 
print(listacarros)
listacarros.sort(reverse = True) #(reverse) ordenação inversa da anterior
print(listacarros)


print(line)
#exercicio: encontrar a posição do Mustang e montar uma lista nova a partir dele
print(listacarros)
#posicao = 0 #usado apenas para mostrar a posição do Mustang, mas poderia usar a variante global "i"
i = 0
while i < len(listacarros):
    if listacarros[i] == "Mustang":
        posicao = i
    i += 1

print(posicao) #encontrou a posição do Mustang

listanova = [] #agora é criar uma lista nova a partir da posição do Mustang
while posicao < len(listacarros):
    listanova.append(listacarros[posicao])
    posicao += 1

print(listanova)

   
    

    



print(line)
newlist = ["Monza"] #parenteses com virgula = tuple (vc não consegue modificar, usar append ou adicionar outras informações posteriores, se for lista, usar conchetes, pois consegue adicionar informações dentro dela)
print(type(newlist))


print(line) #ensinando a transformar uma tupla (tuple) em [list], caso queira alterar algo (lembrando que tuple serve para proteger dados que voce não quer alterar)
# então voce altera a tuple para lista e depois altera para tuple novamente
tuplaFrutas = ("Maça", "Pera", "Banana", "Morango") #criado uma variavel tipo tuple ()
print(type(tuplaFrutas)) #descobrindo o tipo (type)
x = list(tuplaFrutas) #cria uma variavel lista ao converter x = lista(+variavel antiga em tuple)
print(type(x))
x.append("Melancia") #adiciona com append, um valor (melancia) na lista tuplaFrutas(que agora é x)
print(x)
tuplaFrutas = tuple(x) #volta a variavel que virou lista em tupla
print(type(tuplaFrutas)) 
print(tuplaFrutas) #mostra o resultado


