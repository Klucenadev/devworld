import time

nome = input("qual seu nome:")
peso = float(input("qual seu peso (kg):"))
altura = float(input("qual sua altura (m):"))
print("estamos calculando seu IMC, um segundo...")

time.sleep (1)

print("Calculando IMC,um segundo...")

if peso <= 0 or altura <= 0:
    print("Erro: peso e altura devem ser maiores que zero.")
else:
    imc = int(peso / (altura ** 2))
    print("Seu IMC é:", imc)

    if imc < 18:
        print("Abaixo do peso")
    elif imc < 25:
        print("Peso normal")
    elif imc < 30:
        print("Sobrepeso")
    elif imc < 35:
        print("Obesidade grau 1")
    elif imc < 40:
        print("Obesidade grau 2")
    else:
        print("Obesidade grau 3")
