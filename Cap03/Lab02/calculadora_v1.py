# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

def soma(x,y):
    result = x + y
    print(result)

def subtracao(x,y):
    result = x - y
    print(result)

def multiplicacao(x,y):
    result = x * y
    print(result)

def divisao(x,y):
    result = x/y
    print(result)

x = float(input("Informe o Primeiro Valor:"))
y = float(input("Informe o Segundo Valor: "))
op = str(input("Informe a operação: Multiplicação(X), Divisão(/), Soma(+), Subtração(-)"))

if (op == "X"):
    multiplicacao(x,y)
elif(op == "/"):
    divisao(x,y)
elif(op == "+"):
    soma(x,y)
elif(op == "-"):
    subtracao(x,y)
