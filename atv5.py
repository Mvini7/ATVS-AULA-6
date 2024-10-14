nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))
nota4 = float(input("Digite a quarta nota do aluno: "))

soma_notas = nota1 + nota2 + nota3 + nota3

resultado = soma_notas / 4

print(resultado)

if resultado >= 6:
    print("Aprovado")
else:
    print("Reprovado")