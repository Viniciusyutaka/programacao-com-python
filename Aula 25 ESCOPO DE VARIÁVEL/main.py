'''
def cadastrar_usuario(nome, idade, cidade='Nao informado'):
    print(f"Cadrastro: {nome}, {idade}, {cidade}")
    
cadastrar_usuario("Calos", 30, "SJS")
'''
numero = 20 # Variavel global
def calcular():
    numero = 10 # Variavel local
    return numero
print(calcular())
print(numero)

saldo = 5000
def deposito():
    global saldo
    saldo = saldo + 100
    return saldo
print(deposito())