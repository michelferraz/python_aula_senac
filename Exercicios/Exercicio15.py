# . Faça um algoritmo que receba um número e diga se este número está no intervalo entre 100 e 200.


numero = int(input("Digite um número: "))

if numero > 100 and numero < 200: #aqui se usa o and para comparar os valores
    print("Este número está entre os valores de 100 a 200.")
else:
    print("Este número não está entre os valores de 100 a 200.")
