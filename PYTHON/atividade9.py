# Solicita ao usuário o número de valores que serão lidos
n = int(input("Digite a quantidade de números (n): "))

# Verifica se n é válido
if n <= 0:
    print("A quantidade de números deve ser maior que 0.")
else:
    # Inicializa a variável para armazenar o maior número
    maior = float('-inf')  # Começa com um valor muito pequeno

    # Lê n números e encontra o maior
    for i in range(n):
        num = float(input(f"Digite o número {i + 1}: "))
        if num > maior:
            maior = num

    # Exibe o maior número
    print(f"O maior número entre os {n} valores fornecidos é: {maior}")
