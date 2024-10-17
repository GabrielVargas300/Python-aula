# Solicita ao usuário que insira três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Determina o maior e o menor número
maior = max(num1, num2, num3)
menor = min(num1, num2, num3)

# Calcula a maior diferença entre eles
maior_diferenca = maior - menor

# Exibe o resultado
print(f"A maior diferença entre {num1}, {num2} e {num3} é {maior_diferenca}")
