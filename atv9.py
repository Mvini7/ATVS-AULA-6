idade = int(input("Digite sua idade: "))

if idade >= 15 and idade < 18:
    print("Você é adolescente")
elif idade >= 18:
    print("Voê é adulto")
else:
    print("Voê é criança")