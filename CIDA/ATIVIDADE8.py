# CARREGAMENTOS DAS BIBLIOTECAS
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# IMPORTAÇÃO DOS DADOS #
arquivo = 'C:\\Users\\yurih\\Documents\\Programações\\CIDA\\dados_criancas.csv'
dados_originais = pd.read_csv(arquivo, header=0)
dados_dict = dados_originais.to_dict("list")

# PROCESSAMENTO DOS DADOS #
# COVARIANCIA #
media_peso = np.mean(dados_dict['Peso(kg)'])
media_altura = np.mean(dados_dict['Altura(cm)'])
dp_peso = np.std(dados_dict['Peso(kg)'])
dp_altura = np.std(dados_dict['Altura(cm)'])
matriz = [dados_dict['Peso(kg)'], dados_dict['Altura(cm)']]
rho = np.corrcoef(matriz)
# APRESENTAÇÃO DOS RESULTADOS
print(dados_dict)
print(media_peso)
print(media_altura)
print("DISVIO PADRAO",dp_peso)
print("DISVIO PADRAO",dp_altura)
print(rho)
dispersao = plt.scatter(dados_dict["Peso(kg)"], dados_dict["Altura(cm)"],c='#00FF00', marker='o')
plt.title("Estuda da correlação entre peso x altura")
plt.xlabel("Peso(kg)")
plt.ylabel("Altura(cm)")
plt.show()