preco = float(input("Digite o preço: "))
desconto = float(input("Digite o desconto: "))

desconto_porcentagem = desconto / 100

resultado = desconto_porcentagem * preco

descontoo = preco - resultado
print(descontoo)