#AULA 01#
#Carragamento das bibliotecas
import matplotlib.pyplot
import numpy as np
import statistics as st
import matplotlib.pyplot as plot

#carregamento dos dados
dados_seguros = [0.9, 1.0, 1.7, 1.9, 3.1, 5.3, 5.5, 6.9, 12.2, 12.9, 14.0, 33.6]

#Processamento
Q1 = np.percentile(dados_seguros,25, method="averaged_inverted_cdf")
Q2 = np.percentile(dados_seguros,50, method="averaged_inverted_cdf")
Q3 = np.percentile(dados_seguros,75, method="averaged_inverted_cdf")

dq = Q3 - Q1

limite_inferior = np.fmax(0.9, Q1 - 1.5*dq)
limite_superior = np.fmin(33.6, Q3 + 1.5*dq)

#Criação BoxPlot
diagrama = plot.boxplot(dados_seguros)

#Apresentação dos Dados
print ("Q1 =", Q1)
print ("Q2 =", Q2)
print("Q3", Q3)
print("Limite_Inferior=", limite_inferior)
print("Limite_Inferior=", limite_superior)

plot.title("BoxPlot Atividade")
plot.xlabel("Seguradoras")
plot.ylabel("Fatia de Mercado das seguradoras (%)")
plot.show()
