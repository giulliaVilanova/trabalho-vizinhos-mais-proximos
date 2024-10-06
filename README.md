# Explicação de como o algoritmo KNN chegou ao resultado

## 1. Pré-processamento dos dados:
- O primeiro passo foi carregar o conjunto de dados contendo informações sobre tipos de pão, queijo, vegetais, molho e a proteína correspondente.
- Em seguida, foi feita uma limpeza nos dados, removendo as linhas onde o valor da coluna "Tipo de proteína" era desconhecido (representado por `'?'`). Essas linhas não são úteis para o treinamento, já que queremos treinar o modelo com exemplos onde a proteína é conhecida.

**Exemplo:**
- Foram usadas colunas como "Tipo de pão", "Tipo de queijo", "Vegetais" e "Tipo de molho" como **features**.
- A coluna "Tipo de proteína" foi usada como a **classe alvo** que o modelo deve prever.

## 2. Codificação das variáveis categóricas:
- Como o KNN não consegue trabalhar diretamente com dados categóricos, como "Italiano", "Cheddar" ou "Frango", foi necessário transformar essas categorias em **números**.
- Isso foi feito usando o **OneHotEncoder**, que converte as variáveis categóricas em representações binárias (vetores de 0s e 1s). Cada categoria foi convertida em uma nova coluna no conjunto de dados.

**Exemplo de transformação:**
- Se "Tipo de pão" tiver 3 categorias: "Italiano", "Simples", "Granola", o OneHotEncoder criará três colunas, uma para cada tipo de pão. Assim, se a linha tiver "Italiano", a codificação será algo como `[1, 0, 0]`.

## 3. Divisão em conjunto de treino e teste:
- O conjunto de dados codificados foi dividido em dois subconjuntos: **treinamento** e **teste**, usando a função `train_test_split()`.
- A maior parte dos dados (80%) foi usada para **treinar** o modelo, enquanto os 20% restantes foram reservados para **teste**, garantindo que a avaliação do modelo seja feita em dados que ele nunca viu antes.

## 4. Preparação da linha a ser prevista:
- Para prever o tipo de proteína de uma linha específica (onde o valor estava como `'?'`), essa linha foi selecionada e suas características também foram codificadas da mesma forma que os dados de treino (usando o mesmo OneHotEncoder).

**Por que isso é importante?**
- Para garantir que a estrutura dos dados de entrada para a previsão seja **compatível** com os dados de treinamento (ou seja, que tenham o mesmo número de colunas e a mesma codificação).

## 5. Execução do algoritmo KNN:
- Para cada valor de `k` (número de vizinhos), o modelo KNN foi treinado usando os dados de treino. O KNN funciona procurando os `k` vizinhos mais próximos da nova instância (a linha com `'?'`) com base em uma medida de distância (normalmente a distância Euclidiana).

**Como o KNN faz a previsão:**
- O KNN observa os **k vizinhos mais próximos** e retorna a classe (proteína) mais comum entre esses vizinhos.
- Por exemplo, se `k=3` e entre os 3 vizinhos mais próximos houver 2 instâncias de "Frango" e 1 de "Peru", o KNN preverá "Frango", já que é a classe mais frequente.

## 6. Resultados para diferentes valores de K:
- No meu código, o processo foi repetido para `k=1`, `k=3` e `k=5`. Cada vez que o valor de `k` muda, o número de vizinhos considerados pelo algoritmo aumenta, o que pode influenciar o resultado da previsão.

- **k=1**: O algoritmo leva em consideração apenas o vizinho mais próximo. A previsão é baseada no único dado mais semelhante ao exemplo com `'?'`.

- **k=3**: O KNN observa os três vizinhos mais próximos e escolhe a classe predominante.

- **k=5**: O algoritmo considera cinco vizinhos, e a previsão será a classe com a maioria entre esses cinco vizinhos.

## 7. Considerações finais:
- A previsão final varia com o valor de `k`, já que com mais vizinhos sendo considerados, há uma maior diversidade de instâncias influenciando a decisão.
- Para `k=1`, o modelo pode ser muito sensível a outliers (instâncias fora do padrão), enquanto valores maiores de `k` tendem a suavizar a previsão, considerando um grupo maior de vizinhos.
- O retorno do algoritmo de forma transcrita foi:

    A proteína prevista para `K=1` é: Frango

    A proteína prevista para `K=3` é: Frango

    A proteína prevista para `K=5` é: Frango
