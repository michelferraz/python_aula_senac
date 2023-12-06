# Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento após um mês.
#  Considere fixo o juro da poupança em 0,70% a. m

deposito = int(input("Digite o valor a ser depositado: "))
soma = deposito * 0.007 #1.0 = 100%, 0.5 = 50%, 0.1 = 10%, 0.01 = 1%, 0.001 = 0.1%
somaDiaria = soma / 30

print("O rendimento diário deste valor é de:",somaDiaria,"R$")
print("O rendimento deste valor após um mês é de:",soma,"R$")
