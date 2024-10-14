dia = int(input("Digite o dia que você nasceu: "))
mes = input("Digite o mês que você nasceu: ")

if dia >= 21 and mes == "março" and dia <= 20 and mes == "abril":
    print("Seu signo é Áries")
elif dia >= 21 and mes == "abril" and dia <= 20 and mes == "maio":
    print("Seu signo é Touro")
elif dia >= 21 and mes == "maio" and dia <= 20 and mes == "junho":
    print("Seu signo é Gêmeos")