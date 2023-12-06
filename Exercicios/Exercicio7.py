# Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão é: 
# F=(9*C+160) / 5, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

tempC = int(input("Digite a temperatura em graus Celsius atual: "))

F=(9*tempC+160) / 5

print("A temperatura convertida de Celsius para Fahrenheit é:",F,"°F")
