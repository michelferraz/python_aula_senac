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
"""
lista = ["a", "b", "c", "d", "e","f"]
i=0
while i < len(lista):
    print(i,"-",lista[i])
    i+=1
