# Inicializa as variáveis
soma = 0
quantidade = 0
numero_anterior = float('-inf')  # Começa com um valor muito pequeno para garantir que o primeiro número será aceito

# Loop para ler números crescentes
while True:
    numero_atual = float(input("Digite um número (ou um número menor que o anterior para sair): "))
    
    if numero_atual < numero_anterior:
        break  # Sai do laço se o número atual for menor que o anterior
    
    soma += numero_atual
    quantidade += 1
    numero_anterior = numero_atual

# Verifica se algum número foi inserido
if quantidade > 0:
    media = soma / quantidade
    print(f"Soma: {soma}")
    print(f"Quantidade: {quantidade}")
    print(f"Média: {media}")
else:
    print("Nenhum número válido foi inserido.")
