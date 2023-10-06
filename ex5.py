# Importe as bibliotecas necessárias
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Suponha que você tenha um DataFrame chamado 'data' com suas características e rótulos
# Certifique-se de preparar seus dados adequadamente

# Divida o conjunto de dados em treinamento e teste
X = data[['Idade', 'Manutencao', 'FalhasAnteriores', 'NivelAutomacao']]
y = data['Seguranca']  # 'Seguranca' é o rótulo que indica "Segura" ou "Não Segura"
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crie o modelo de árvore de decisão
model = DecisionTreeClassifier()

# Treine o modelo com os dados de treinamento
model.fit(X_train, y_train)

# Faça previsões usando o modelo
y_pred = model.predict(X_test)

# Calcule a precisão do modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisão do modelo: {accuracy * 100:.2f}%')

# Agora você pode usar o modelo para classificar novas máquinas com base em suas características