# Solicita ao usuário que insira dois valores distintos
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Verifica qual valor é maior e exibe a mensagem correspondente
if valor1 > valor2:
    print(f"O maior entre {valor1} e {valor2} é {valor1}")
elif valor2 > valor1:
    print(f"O maior entre {valor1} e {valor2} é {valor2}")
else:
    print("Os valores são iguais, insira valores distintos.")
