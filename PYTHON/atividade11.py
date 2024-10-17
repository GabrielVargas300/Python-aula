# Solicita ao usuário um número inteiro qualquer
numero = input("Digite um número inteiro: ")

# Solicita ao usuário um número inteiro de 1 algarismo
algarismo = input("Digite um número de apenas 1 algarismo: ")

# Verifica se o número fornecido tem apenas 1 dígito
if len(algarismo) == 1 and algarismo.isdigit():
    # Verifica se o algarismo aparece no número
    if algarismo in numero:
        print(f"O algarismo {algarismo} aparece no número {numero}.")
    else:
        print(f"O algarismo {algarismo} não aparece no número {numero}.")
else:
    print("Por favor, insira um número válido de apenas 1 algarismo.")
