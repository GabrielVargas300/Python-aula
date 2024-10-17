#atividade 1 
# Função para verificar se um número é par ou ímpar
def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "O número é par."
    else:
        return "O número é ímpar."

# Solicita ao usuário um número
try:
    numero = int(input("Digite um número: "))
    resultado = verificar_par_ou_impar(numero)
    print(resultado)
except ValueError:
    print("Por favor, digite um número válido.")
