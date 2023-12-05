''' Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no 
mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o 
seu nome, o salário fixo e salário no final do mês.
'''

name = input("Digite o seu nome: ")
salario = int(input ("Qual o valor do seu salário? "))
vendas = int(input ("Qual o valor das suas vendas este mês?(em R$) "))
comissao = (vendas * 0.15)
salariototal = salario+comissao
salarioliquido = salariototal - (salariototal * 0.25)

print("Vendedor:",name)
print("Salário fixo mensal:",salario,"R$")
print("Salário Total comissionado:",salariototal,"R$")
print("Total liquído após os descontos:",salarioliquido, "R$")

