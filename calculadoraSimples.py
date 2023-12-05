#pegar dois números e efetuar mostrando na tela a soma, divisão, multiplicação e subtração da seguinte maneira. ex:
# a soma dos dois números é: SOMA
# porcentagem %, é valor * 0.1 (para 10%), 0.5 (para 50%), sempre usar essa multiplicação de 0. alguma coisa referente ao porcentagem
# exemplo de subtração com porcentagem:
# salariototal = salariofixo + comissao
# salarioliquido = salariototal - (salariototal * 0.11) 
# no segundo subtrai o valor pela soma+11%.

#exercicio feito
#n1 = int(input ("Digite o primeiro número : "))
#n2 = int(input ("Digite o segundo número : "))
#print("A soma dos dois números é : " , n1+n2)
#n3 = int(input ("Digite o terceiro número : "))
#print("O resultado final é : ", n1+n2-n3)

#correção feita
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
soma = n1+n2
divisao = n1/n2
multiplicacao = n1*n2
subtracao = n1-n2
print("O resultado da Soma é : ", soma)
print("O resultado da Subtração é : ", subtracao)
#ou
print("O resultado da Soma é : ", n1+n2)
print("O resultado da Subtração é : ", n1-n2)
print("O resultado da Divisão é : ", n1/n2)
print("O resultado da Multiplicação é : ", n1*n2)


