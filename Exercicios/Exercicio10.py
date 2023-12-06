'''
A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros. Faça um algoritmo que 
receba um valor de uma compra e mostre o valor das prestações '''

valorTotal = int(input("Digite o valor total de sua compra: "))
valorParcelado = valorTotal / 5
print("A sua prestação ficou em 5x sem juros de:",valorParcelado,"R$")
