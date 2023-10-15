from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Dados de entrada (características)
ph = [3.0, 5.5, 2.5, 7.0, 4.0, 6.5, 3.5, 6.0, 2.0, 7.5, 4.5, 5.0, 2.8, 8.0]
concentracao = ['Concentrada', 'Diluida', 'Concentrada', 'Diluida', 'Concentrada', 'Diluida', 'Concentrada', 'Diluida', 'Concentrada', 'Diluida', 'Concentrada', 'Diluida', 'Concentrada', 'Diluida']
cheiro = ['Com Cheiro', 'Sem Cheiro', 'Com Cheiro', 'Sem Cheiro', 'Com Cheiro', 'Sem Cheiro', 'Com Cheiro', 'Sem Cheiro', 'Com Cheiro', 'Sem Cheiro', 'Com Cheiro', 'Sem Cheiro', 'Com Cheiro', 'Sem Cheiro']

# Classificações
classificacao = ['Ácida', 'Básica', 'Ácida', 'Básica', 'Ácida', 'Básica', 'Ácida', 'Básica', 'Ácida', 'Básica', 'Ácida', 'Básica', 'Ácida', 'Básica']

le_concentracao = LabelEncoder()
concentracao_encoded = le_concentracao.fit_transform(concentracao)

le_cheiro = LabelEncoder()
cheiro_encoded = le_cheiro.fit_transform(cheiro)

caracteristicas = list(zip(ph, concentracao_encoded, cheiro_encoded))

modelo_arvore = DecisionTreeClassifier()
modelo_arvore.fit(caracteristicas, classificacao)


nova_substancia = [6.2, 'Diluida', 'Com Cheiro']
nova_substancia_encoded = [nova_substancia[0], le_concentracao.transform([nova_substancia[1]])[0], le_cheiro.transform([nova_substancia[2]])[0]]
previsao = modelo_arvore.predict([nova_substancia_encoded])

print("Classificação da substância:", previsao[0])
