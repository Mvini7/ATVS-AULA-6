capital = float(input("Digite o capital inicial: "))
juros = float(input("Digite o valor dop juros: "))
tempo = float(input("Digite o tempo: "))

juros_porcentagem = juros / 100

calculo = capital * juros_porcentagem * tempo

print(calculo)