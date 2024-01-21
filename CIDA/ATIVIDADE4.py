import numpy as np
import statistics as st
import matplotlib.pyplot as plot

#dados
n = 2

dados = [988.8, 556.9, 224.6, 210.9, 201.5, 187.7, 151.6, 135.8, 129.8, 119.4, 116.0, 102.3, 101.8, 92.4,
         84.7, 83.9, 80.2, 74.7, 72.7, 68.8, 66.8, 66.8, 63.7, 62.8, 61.9, 56.2, 54.1, 50.3, 49.7, 46.3]
dadosSud = [988.8, 556.9, 210.9, 101.8, 92.4, 84.7, 83.9, 72.7, 68.4, 63.7, 62.8, 50.3, 49.7, 46.3]
#processamento de dados

q1 = np.percentile(dados, 25, method="averaged_inverted_cdf")
q2 = np.percentile(dados, 50, method="averaged_inverted_cdf")
q3 = np.percentile(dados, 75, method="averaged_inverted_cdf")

q1S = np.percentile(dadosSud, 25, method="averaged_inverted_cdf")
q2S = np.percentile(dadosSud, 50, method="averaged_inverted_cdf")
q3S = np.percentile(dadosSud, 75, method="averaged_inverted_cdf")

dq = q3 - q1
dqS = q3S - q1S

limiteInferior = np.fmax(46.3, q1 - 1.5*dq)
limiteSuperior = np.fmin(988.8, q3 + 1.5*dq)
LISud = np.fmax(46.3, q1S - 1.5*dqS)
LSSud = np.fmin(988.8, q3S + 1.5*dqS)

#criação do boxplot

diagrama = plot.boxplot(dados, labels= ["brasil"], positions= [1] )
diagramaI = plot.boxplot(dadosSud, labels= ["região sudeste"], positions= [2] )

#apresentação dos dados

print("q1 é = ", q1)
print("q2 é = ", q2)
print("q3 é = ", q3)

print("q1S é = ", q1S)
print("q2S é = ", q2S)
print("q3S é = ", q3S)


print("limite inferior é = ", limiteInferior)
print("limite superior é = ", limiteSuperior)

print("limite inferior sudeste é = ", LISud)
print("limite superior sudeste é = ", LSSud)


plot.title("boxplot da população dos municipios brasileiros em 10000")
plot.xlabel("municipios")
plot.ylabel("população (10000)")
plot.show()