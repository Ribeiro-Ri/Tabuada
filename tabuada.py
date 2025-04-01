num = int(input("Digite um número para ver a tabuada: "))  # Solicita um número ao usuário

print(f"\nTabuada do {num}:")
for i in range(1, 11):  # Loop de 1 a 10
    print(f"{num} × {i} = {num * i}")

