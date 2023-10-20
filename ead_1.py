import numpy as np
from scipy import stats

# Dados de peso
peso = np.array([55, 58, 60, 62, 64, 57, 59, 63, 65, 61, 62, 64, 55, 58, 60, 62, 64, 57, 59, 63, 65, 61, 62, 64, 55, 58, 60, 62, 64, 57, 59, 63, 65, 61, 62, 64, 55, 58, 60, 62, 64, 57, 59, 63, 65, 61, 62, 64])

# Hipótese nula (H0) - média do peso é menor ou igual a 63 gramas
mu0 = 63

# Realizar o teste t de uma amostra
t_statistic, p_value = stats.ttest_1samp(peso, mu0)

# Definir o nível de significância (alfa)
alpha = 0.05

# Imprimir os resultados
print(f"Media do peso: {np.mean(peso):.2f} gramas")
print(f"Desvio padrao do peso: {np.std(peso):.2f} gramas")
print(f"Variancia do peso: {np.var(peso):.2f} gramas^2")
print(f"Estatistica de teste t: {t_statistic:.2f}")
print(f"Valor-p: {p_value:.4f}")

# Teste de hipóteses com base no valor-p
if p_value < alpha:
    print("Rejeitamos a hipotese nula (H0). O lote de pecas deve ser reprovado.")
else:
    print("Não rejeitamos a hipótese nula (H0). O lote de peças é aprovado.")
