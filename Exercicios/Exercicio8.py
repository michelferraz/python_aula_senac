'''
Elaborar um algoritmo que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar 
(US$). O algoritmo deverá solicitar o valor da cotação do dólar e também a quantidade de dólares disponíveis com o 
usuário.
'''

cotacao = float(input("Digite o valor da cotação atual (em Dólar):"))
saldo = float(input("Digite o valor de saldo atual (em Dólar):"))

real = (saldo*cotacao)

print("Saldo em Dólar:",saldo,"U$D")
print("Saldo em Real Brasileiro:",real,"R$")
