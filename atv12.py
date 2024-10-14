usuario = input("Digite o seu usuario: ")
senha = input("Digite sua senha: ")

if usuario == "admin" and senha == "1234":
    print("Login bem sucedido")
else:
    print("Senha ou usuario incorreto")