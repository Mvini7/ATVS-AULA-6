nota = float(input("Digite sua nota de 0 a 100: "))

if nota <= 20:
    print("Você tirou F")
elif nota > 21 and nota <= 40:
    print("Você tirou D")
elif nota > 41 and nota <= 60:
    print("Você tirou C")
elif nota > 61 and nota <= 80:
    print("Você tirou B")
elif nota > 81 and nota <= 100:
    print("Você tirou A")