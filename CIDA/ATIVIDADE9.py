import numpy as np
import matplotlib.pyplot as plt


# CARREGAMENTO DAS BIBLIOTECAS #
x = [1,2,3,4,5,6,7,8,9,10]

#LAÇO QUE PRODUZ AS FUNÇOES DESEJADAS
ya = []
yb = []
yc = []
tamanho = len(x)
contador = range(tamanho)
for i in contador:
    valor = x[i] * x[i]     #FUNÇÃO QYE FAZ Y = x^2#
    ya.append(valor)

    valor2 = x[i] * x[i] * x[i]
    yb.append(valor2)

    valor3 = 1.0/(x[i] * x[i])
    yc.append(valor3)


# PROCESSAMENTO DOS DADOS #
matriz_corr = [x,ya,yb,yc]
rho = np.corrcoef(matriz_corr)

# APRESENTAÇÃO DOS RESULTADOS #
print(ya)
print(yb)
print(yc)
graf_a = plt.scatter(x,ya)
plt.show()

graf_b = plt.scatter(x,yb)
plt.show()

graf_c = plt.scatter(x,yc)
plt.show()
print("=========================================================================================================================================================================================================================================================")
print(rho)
print("=========================================================================================================================================================================================================================================================")

# LINEARIZAÇÃO DOS PROBLEMAS #
x_log = []
ya_log = []
yb_log = []
yc_log = []
tamanho = len(x)
contador = range(tamanho)
for i in contador:
    valor = np.log(x[i])
    x_log.append(valor)

    valor2 = np.log(ya[i])
    ya_log.append(valor2)

    valor3 = np.log(yb[i])
    yb_log.append(valor3)

    valor4 = np.log(yc[i])
    yc_log.append(valor4)

matriz_corr_log = [x_log, ya_log,yb_log,yc_log]
rho_log = np.corrcoef(matriz_corr_log)

graf_a = plt.scatter(x_log,ya_log)
plt.show()

graf_b = plt.scatter(x_log,yb_log)
plt.show()

graf_c = plt.scatter(x_log,yc_log)
plt.show()

print(rho_log)
print("=========================================================================================================================================================================================================================================================")
