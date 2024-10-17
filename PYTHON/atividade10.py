# Inicializa as populações e as taxas de crescimento
populacao_A = 90000000  # População inicial do país A
populacao_B = 200000000  # População inicial do país B
taxa_crescimento_A = 0.03  # 3% de crescimento anual para o país A
taxa_crescimento_B = 0.015  # 1,5% de crescimento anual para o país B

# Inicializa o contador de anos
anos = 0

# Loop para calcular o número de anos necessários
while populacao_A < populacao_B:
    populacao_A += populacao_A * taxa_crescimento_A  # Atualiza a população de A
    populacao_B += populacao_B * taxa_crescimento_B  # Atualiza a população de B
    anos += 1  # Incrementa o número de anos

# Exibe o resultado
print(f"Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")
