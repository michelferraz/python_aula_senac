#escopo (tudo criado dentro do Mostrar) / variavel global (tudo criado fora do escopo Mostrar)

x = "Senac"
def Mostrar():
    print(x)
Mostrar()

x = "Jose"
def MostrarNome():
    x = "SENAC"
    print(x)

MostrarNome()
print(x)
