import matplotlib.pyplot as plt
import numpy as np


lista_dados = [-0.5, 1.8, 43.8, 52, 2.6, 7.8, 9.8, -2.5]

n = len(lista_dados)
print("tamanha e", n)

lista_dados.sort()
print("ordenada", lista_dados)

print("menor valor", lista_dados[0])

valores = range(n)
oi = valores
for contador in valores:
    print(contador)

print("==================================================")
valores = range(n)
for contador in valores:
    print(contador, lista_dados[contador])

print("==================================================")

for contador in valores:
    if (lista_dados[contador] > 0):
        print(lista_dados[contador])

print("==================================================")

oi = range(n-1,0,-1)
print(oi)
for contador in oi:
    if (lista_dados[contador] > 0):
        print(lista_dados[contador])

print("==================================================")

lista_dados.append(4.5)
lista_dados.sort()
print(lista_dados)

print("==================================================")

dados = [45, 56, -89.0, 23.4, 1.5, 2.5, 5.5, 10.0, -50.0, 1.0]

dados.append(-12.5) #adicionar
dados.sort()
print(dados)
print("==================================================")
Q1 = np.percentile(dados,25, method="averaged_inverted_cdf")
Q3 = np.percentile(dados,75, method="averaged_inverted_cdf")
dq = Q3 - Q1

lim_inf = np.fmax(dados[0], Q1 - 1.5*dq)
lim_sup = np.fmin(dados[-1], Q3 + 1.5*dq)

print("inferior",lim_inf)
print("superior",lim_sup)

dados_sem = []
valores = range(len(dados))
for contador in valores:
    if (dados[contador] >= lim_inf) and (dados[contador] <= lim_sup):
        dados_sem.append(dados[contador])

diagrama = plt.boxplot([dados, dados_sem])
plt.show()