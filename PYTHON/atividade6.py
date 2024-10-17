# Solicita ao usuário que insira dois valores distintos
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

# Verifica qual valor é maior e exibe a mensagem correspondente
if valor1 > valor2 and valor1 > valor3:
    print(f"O maior entre {valor1} e {valor2} e {valor3} é {valor1}")
elif valor2 > valor1 and valor2 > valor3:
    print(f"O maior entre {valor1} e {valor2} e {valor3} é {valor2}")
elif valor3 > valor1 and valor3 >valor2:
    print(f"O maior entre {valor1} e {valor2} e {valor3} é {valor3}")
else:
    print("Os valores são iguais, insira valores distintos.")
