import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dados = pd.read_csv("F:\\eu\\datacience\\lista04\\dados_imposto_empresa.csv",header=2)
lista = dados.to_dict('list')
print(lista)
classe = round(1+3.32*np.log10(len(lista['Imposto (%)'])))
plt.hist(lista['Imposto (%)'], bins=classe, ec='white')
plt.show()