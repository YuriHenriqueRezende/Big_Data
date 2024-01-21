import numpy as np
hrsSemDormir = [8,8,12,12,16,16,20,20,24,24]
erros = [6,8,6,12,8,14,12,14,12,16]
m = [hrsSemDormir,erros]
poh = np.corrcoef(m)
print(poh)
#Existe uma correlação forte entre os erros e horas sem dormir, sendo maior os erros conforme mais horas sem dormir forem acumuladas!