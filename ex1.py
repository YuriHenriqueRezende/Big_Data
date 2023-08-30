import pandas as pd

data = {
    'Nomes': ['Alice', 'Julia', 'Viviane', 'Roberto', 'Filipe', 'Silvio'],
    'Idade': [19, 22, 28, 34, 28, 48],
    'Profissões': ['Direito', 'Engenharia', 'Enfermagem', 'Engenheiro Civil', 'Cientista da Computação', 'Engenheiro Eletrônico'],
    'ID': [1, 2, 3, 4, 5, 6]
}

df = pd.DataFrame(data)

print(df)
