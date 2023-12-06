'''
O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos 
impostos (aplicados, primeiro os impostos sobre o custo de fábrica, e depois a percentagem do distribuidor sobre o 
resultado). Supondo que a percentagem do distribuidor seja de 28% e os impostos 45%. Escrever um algoritmo que 
leia o custo de fábrica de um carro e informe o custo ao consumidor do mesmo.
'''

custoFab = int(input("Digite o valor do custo deste veículo (custo de fabrica): "))
impostos = (custoFab + (custoFab * 0.45))
#print(impostos)
custoDist = (impostos + (impostos * 0.28))
#print(custoDist)

print("O valor final deste veículo, com todos os impostos, taxas e encargos é de:",custoDist,"R$")