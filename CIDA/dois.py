# CARREGAMENTO DAS BIBLIOTECAS #
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# 2 #
print("2")
# CARREGAMENTO DOS DADOS #
hrsSemDormir = [8,8,12,12,16,16,20,20,24,24]
erros = [6,8,6,12,8,14,12,14,12,16]
m = [hrsSemDormir,erros]
poh = np.corrcoef(m)
print(poh)