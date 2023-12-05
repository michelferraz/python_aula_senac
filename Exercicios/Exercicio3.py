#Escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida a distância total percorrida pelo automóvel e o total de combustível gasto.

km = int(input ("Qual a quilometragem percorrida? "))
gas = int(input ("Quanto foi o total de combustível gasto? "))
gasprice = int(input ("Qual o valor pago no combustível? "))
#gastype = input("Qual o tipo de combustível usado? ")


kmlitro = (km/gas)
media = (gasprice/kmlitro)

print("Este veículo faz",kmlitro,"km por litro de combustível")
print("Sendo assim, este veículo gasta",media,"$ por quilometro percorrido.")