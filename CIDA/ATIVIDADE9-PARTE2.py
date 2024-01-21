# IMPORTAÇÃO DAS BIBLIOTECAS #
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as snb

# IMPORTAÇÃO DOS ARQUIVOS
arquivo = 'C:\\Users\\yurih\\Documents\\Programações\\CIDA\\dados_corr.csv'
dados_originais = pd.read_csv(arquivo, header=0)
dados_dict = dados_originais.to_dict("list")

# PROCESSAMENTO DOS DADOS #
matriz_corr = [dados_dict['altura'], dados_dict['lado'], dados_dict['processo'],dados_dict['massa']]
rho = np.corrcoef(matriz_corr)

altura_log = []
lado_log = []
processo_log = []
massa_log = []
tamanho = len(dados_dict['massa'])
contador = range(tamanho)
for i in contador:
    valor = np.log(dados_dict['altura'][i])
    altura_log.append(valor)

    valor = np.log(dados_dict['lado'][i])
    lado_log.append(valor)

    valor = np.log(dados_dict['processo'][i])
    processo_log.append(valor)

    valor = np.log(dados_dict['massa'][i])
    massa_log.append(valor)

matriz_corr_linear = [altura_log, lado_log,processo_log,massa_log]
rho_lineralizado = np.corrcoef(matriz_corr_linear)

# APRESENTAÇÃO DOS DADOS #
print(rho)
print("=========================================================================================================================================================================================================================================================")
print(rho_lineralizado)
mapa_calor = snb.heatmap(rho, annot=True)
plt.grid()
plt.show()