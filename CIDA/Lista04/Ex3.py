import numpy as np
import matplotlib.pyplot as plt
unidades = [40,60,80,100,120,140,160]
rendimento = [15.9,18.8,21.6,25.2,28.7,30.4,30.7]
m = [unidades,rendimento]
roh = np.corrcoef(m)
print(roh)
plt.scatter(unidades,rendimento)
plt.show()
#Coeficiente = 0.98 Muito forte!!