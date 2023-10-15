from sklearn import svm
from sklearn.preprocessing import LabelEncoder

# Dados de entrada (características)
potencia = [120, 80, 100, 110, 90, 130, 70, 105, 115, 85]
eficiencia = [92, 65, 75, 85, 68, 95, 60, 80, 88, 70]
idade = [50, 45, 55, 60, 48, 62, 40, 58, 56, 45]
tamanho = ['Eficiente', 'Ineficiente', 'Ineficiente', 'Eficiente', 'Ineficiente', 'Eficiente', 'Ineficiente', 'Eficiente', 'Eficiente', 'Ineficiente']

# Classificações
classificacao = ['Eficiente' if t == 'Eficiente' else 'Ineficiente' for t in tamanho]

le_tamanho = LabelEncoder()
tamanho_encoded = le_tamanho.fit_transform(tamanho)

caracteristicas = list(zip(potencia, eficiencia, idade, tamanho_encoded))

modelo_svm = svm.SVC(kernel='linear')
modelo_svm.fit(caracteristicas, classificacao)

nova_maquina = [95, 78, 53, 'Eficiente']
nova_maquina_encoded = [nova_maquina[0], nova_maquina[1], nova_maquina[2], le_tamanho.transform([nova_maquina[3]])[0]]
previsao = modelo_svm.predict([nova_maquina_encoded])

print("Classificação da máquina:", previsao[0])
