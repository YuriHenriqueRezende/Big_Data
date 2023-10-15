from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Dados de entrada (características)
idade = [2, 6, 1, 4, 3, 5]
horas_desde_manutencao = [50, 200, 20, 150, 100, 180]
historico_falhas = ['Nenhuma', 2, 'Nenhuma', 1, 3, 2]

# Classificações
classificacao = ['Necessita', 'Necessita', 'Necessita', 'Não Necessita', 'Necessita', 'Não Necessita']

le_historico_falhas = LabelEncoder()
historico_falhas_encoded = le_historico_falhas.fit_transform(historico_falhas)

caracteristicas = list(zip(idade, horas_desde_manutencao, historico_falhas_encoded))

modelo_arvore = DecisionTreeClassifier()
modelo_arvore.fit(caracteristicas, classificacao)


nova_maquina = [3, 120, 'Nenhuma']
nova_maquina_encoded = [nova_maquina[0], nova_maquina[1], le_historico_falhas.transform([nova_maquina[2]])[0]]
previsao = modelo_arvore.predict([nova_maquina_encoded])

print("Classificação da máquina:", previsao[0])
