# IMPORTAÇÃO DAS BIBLIOTECAS #
import numpy as np
import matplotlib.pyplot as plt

# CARREGAMENTO DOS DADOS #
dados = {"peso":[30,32,24,28,26,34,25,23,35,31],
         "altura":[145,150,125,140,127,145,132,112,155,145]}

# PROCESSAMENTO DOS DADOS #
media_peso = np.mean(dados['peso'])
media_altura = np.mean(dados['altura'])

# IMPLEMENTAÇÃO DA TABELA DO MMQO #
alfa = []
beta = []

tamanho = len(dados['peso'])
contador = range(tamanho)
for i in contador:
    valor = dados['peso'][i] - media_peso
    alfa.append(valor)

    valor = dados['altura'][i] - media_altura
    beta.append(valor)

soma_numerador = 0.0
soma_denominador = 0.0
for i in contador:
    valor = alfa[i]*beta[i]
    soma_numerador = soma_numerador + valor

    valor = alfa[i]*alfa[i]
    soma_denominador = soma_denominador +valor

a = soma_numerador/soma_denominador
b = media_altura - a * media_peso


# VERIFICAÇÃO DO MODELO #
pesos_escolhidos = [5,10,15,20,25,30,35,40,45,50]
tamanho = len(pesos_escolhidos)
contador = range(tamanho)
altura_prevista = []
for i in contador:
    valor = a * pesos_escolhidos[i] + b
    altura_prevista.append(valor)

# CALCULO DO R^2 #
soma_residuos = 0.0
denominador_residuo = 0.0
tamanho = len(dados['peso'])
contador = range(tamanho)
for i in contador:
    y_previsto = a * dados["peso"][i] + b
    valor = dados['altura'][i] - y_previsto
    soma_residuos = soma_residuos + valor*valor

    valor = beta[i] * beta[i]
    denominador_residuo = denominador_residuo + valor

R2 = 1 - soma_residuos/denominador_residuo

# APRESENTAÇÃO DOS DADOS #
print(dados)
print(media_peso)
print(media_altura)
print(soma_numerador)
print(soma_denominador)
print(a)
print(b)
print(R2)

graf1 = plt.scatter(dados['peso'],dados['altura'])
graf2 = plt.plot(pesos_escolhidos, altura_prevista)
plt.title('ALTURA EM FUNÇÃO DOS PESO')
plt.xlabel('peso')
plt.ylabel('altura')
plt.show()