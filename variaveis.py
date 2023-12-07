line = "_____________________________"
line2 = "                            "
"""
str = "textos"
int = 10
float = 10.5
boolean = true

# nome das variaveis
# não pode começar com numeros, e diversos tipos de caracteres, tb nao pode iniciar com letra maiuscula (geralmente é usada para funções)

# nomeando uma variavel
nome = "Michel Ferraz"
print(nome)

#mostrando o tipo = type
print(type(nome))

#funções, length (len) é tamanho, Uper case (upper) é caixa alta,
#na função for tem que seguir o espaço de tab para continuar seguindo o codigo do for
print(len(nome))

print(nome.upper)

#for x in nome:
#    print(x)

# [] conchetes usa para especificar algum lugar/espaço, por exemplo [5] vai mostrar a 5ª letra do nome ou [5:12] vai mostrar da 5ª a 12ª letra do nome, ou 2x :: (2 pontos) para mostrar até o final
print(nome[5::])
"""
a,b,c = 10,3,5
print(type(a))
print(a,b,c)
a="michel"
print(type(a))
print(a,b,c)
a=100
print(type(a))
print(a,b,c)



print(line)
nomeCompleto = "Michel Ferraz"
print(nomeCompleto[0:10]) #conchetes com essa numeração, busca os valores conforme a ordem que vc escolheu, ex: de 0 a 10 (0 = M e 10 = r, sendo Michel feRraz), lembrando que começa sempre no 0 e conta cada espaço e nunca mostra o ultimo valor/espaço
print(nomeCompleto[-1]) #mostra apenas o ultimo caracter)
print(nomeCompleto[3:10]) #mostra do 3º ao 10º caracter, lembrando que começa no zero e não mostra o ultimo real
print(nomeCompleto[5::]) #mostra a partir do 5º caracter até o ultimo real
print(nomeCompleto[-6:-1]) #mostra de tras pra frente
print(nomeCompleto[-6::]) #mostra de tras pra frente, os :: é usado para fazer ler até o ultimo caracter real


print(line)
print(line2)
#exercicio: digitar o cpf sem os pontos e printar com os pontos e separado...

# 38602487827
# 01234567891
cpf = "38602487827" #(input("Digite o CPF: "))

print(cpf[0:3]+"."+cpf[3:6]+"."+cpf[6:9]+"-"+cpf[-2::]) #lembrando que a ultima não mostra, por isso repete o 3 nos dois primeiros conchetes e nos demais



print(line)
print(line2)
produto = {
    "nome" : "camiseta",
    "cores" : ["branca", "azul", "verde"], #para adicionar varias opções na lsita
    "tamanho" : ["P", "M", "G"]
}

print(produto) #mostra todo o produto e as variaveis
print(produto["cores"][1].capitalize()) #mostra a variavel cores e a posição da cor escolhida, no caso a 1 = azul
print(produto["tamanho"][2]) #mostra a variavel tamanho na posição 2 = G


