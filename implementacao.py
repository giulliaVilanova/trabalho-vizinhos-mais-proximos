import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

data = pd.read_csv('dados_lanches.csv')

data_clean = data[data['Tipo de proteína'] != '?']

X = data_clean.iloc[:, :-1]
y = data_clean.iloc[:, -1]

encoder = OneHotEncoder(sparse_output=False)
X_encoded = encoder.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size = 0.2, random_state = 42)

linha_para_prever = data[data['Tipo de proteína'] == '?'].iloc[:, :-1]
linha_encoded = encoder.transform(linha_para_prever)

for k in [1, 3, 5]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    predicao = knn.predict(linha_encoded)
    print(f"A proteína prevista para K={k} é: {predicao[0]}")