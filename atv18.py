usuario= "admin"
senha = "senha123"

tentativas = 3

for tentativa in range(tentativas):

    user = input("Digite o nome de usuário: ")
    sen = input("Digite a senha: ")

    if user == usuario and sen == senha:
        print("Login feito com sucesso")
        break
    elif tentativa == tentativas - 1:
        for _ in range(3):
            print("Acesso negado")
    else:
        tentativas_restantes = tentativas - tentativa - 1
        print(f"Você tem {tentativas_restantes} tentativas")
