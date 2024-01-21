"""IMPLANTAÇÃO DO EXERCICIO 1 PARA A LISTA 1"""

#ATIVIDADE 1: #

'BLOCO 1: BIBLIOTECAS'
import numpy as np
import statistics as st


"BLOCO 2: DADOS"
matematica = [45, 56, -89.0, 23.4, 1.5, 2.5, 5.5, 10.0, -50.0, 1.0]

'BLOCO 3: PROCESSAMENTO DOS DADOS'
media = np.mean(matematica)
mediana = np.median(matematica)
desviopadrao = np.std(matematica)
moda = st.mode(matematica)

"BLOCO 4: APRESENTAÇÃO DOS RESULTADOS"
print("ATIVIDADE 1: A MEDIA E IGUAL A %.2f" %(media))
print("ATIVIDADE 1: A MEDIANA E IGUAL A %.2f" %(mediana))
print("ATIVIDADE 1: O DESVIO-PADRÃO E IGUAL A %.2f" %(desviopadrao))
print("ATIVIDADE 1: A MODA E IGUAL A %.2f" %(moda))

#print("A MEDIA É %.1f É A MEDIANA É %d" %(media, mediana))#

#ATIVIDADE 2: #

matematica2 = [83.3,80.7,86.4,88.3,84.7,85.2,82.8,87.7,86.9,86.2,83.5,84.4,87.2,85.5,86.3]

media2 = np.mean(matematica2)
mediana2 = np.median(matematica2)
desviopadrao2 = np.std(matematica2)
moda2 = st.mode(matematica2)

print("ATIVIDADE 2: A MEDIA E IGUAL A %.2f" %(media2))
print("ATIVIDADE 2: A MEDIANA E IGUAL A %.2f" %(mediana2))
print("ATIVIDADE 2: O DESVIO-PADRÃO E IGUAL A %.2f" %(desviopadrao2))
print("ATIVIDADE 2: A MODA E IGUAL A %.2f" %(moda2))

#ATIVIDADE 3: #

bateriaA = [153,173,136,134,157,149,171,162]
bateriaB = [172,163,151,146,146]

media3 = np.mean(bateriaA)
desviopadrao3 = np.std(bateriaA)
media4 = np.mean(bateriaB)
desviopadrao4 = np.std(bateriaB)
soma1 = np.subtract(media3,desviopadrao3)
subtracao1 = np.add(media3,desviopadrao3)
soma2 = np.subtract(media4,desviopadrao4)
subtracao2 = np.add(media4,desviopadrao4)

print("ATIVIDADE 3: A MEDIA DA BATERIA A É: %.d É DESVEIO-PADRAO É %d" %(media3, desviopadrao3))
print("ATIVIDADE 3: A MEDIA DA BATERIA B É: %.d É DESVEIO-PADRAO É %d" %(media4, desviopadrao4))
print("ATIVIDADE 3: O LIMITE INFERIOR DA BATERIA A E: %.d"%(subtracao1))
print("ATIVIDADE 3: O LIMITE SUPERIOR DA BATERIA A E: %.d"%(soma1))
print("ATIVIDADE 3: O LIMITE INFERIOR DA BATERIA B E: %.d"%(subtracao2))
print("ATIVIDADE 3: O LIMITE SUPERIOR DA BATERIA B E: %.d"%(soma2))