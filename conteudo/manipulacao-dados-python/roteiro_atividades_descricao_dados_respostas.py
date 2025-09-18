# Soluções - Roteiro de Atividades - Ciências de Dados com Python

# Preparação
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando os conjuntos de dados
iris = sns.load_dataset('iris')
tips = sns.load_dataset('tips')


# ============================================================================
# Parte 1: Operações Básicas e Estruturas de Dados
# ============================================================================

print("\n=== PARTE 1: OPERAÇÕES BÁSICAS ===")

# Exercício 1.1 - Operações Aritméticas
print("\n--- Exercício 1.1 - Operações Aritméticas ---")

# 1. Operações básicas
print("15 + 8 =", 15 + 8)
print("25 * 3 =", 25 * 3)
print("100 / 7 =", 100 / 7)
print("100 // 7 =", 100 // 7)
print("100 % 7 =", 100 % 7)
print("2**8 =", 2**8)

# 2. Funções matemáticas
print("\nFunções matemáticas:")
print("Logaritmo natural de 50:", math.log(50))
print("Logaritmo base 10 de 1000:", math.log10(1000))
print("Raiz quadrada de 64:", math.sqrt(64))
print("Seno de π/4:", math.sin(math.pi/4))

# Exercício 1.2 - Variáveis e Atribuições
print("\n--- Exercício 1.2 - Variáveis e Atribuições ---")

altura = 1.75
peso = 70
imc = peso / (altura ** 2)
print(f"Altura: {altura}m")
print(f"Peso: {peso}kg")
print(f"IMC: {imc:.2f}")

# Exercício 1.3 - Listas e Arrays
print("\n--- Exercício 1.3 - Listas e Arrays ---")

# Criando lista
idades_lista = [23, 34, 45, 28, 31, 29]
print("Lista original:", idades_lista)

# Convertendo para array NumPy
idades_array = np.array(idades_lista)
print("Array NumPy:", idades_array)

# Multiplicando por 2
print("Lista * 2:", [i * 2 for i in idades_lista])
print("Array * 2:", idades_array * 2)

# Exercício 1.4 - Sequências
print("\n--- Exercício 1.4 - Sequências ---")

# Sequência com range
seq_range = list(range(1, 21))
print("Sequência 1-20:", seq_range)

# Valores igualmente espaçados
seq_linspace = np.linspace(0, 100, 7)
print("7 valores entre 0 e 100:", seq_linspace)

# Repetindo número
seq_repeat = np.repeat(5, 10)
print("Número 5 repetido 10 vezes:", seq_repeat)

# ============================================================================
# Parte 2: Explorando os Dados - Dataset Iris
# ============================================================================

print("\n=== PARTE 2: EXPLORANDO DADOS - IRIS ===")

# Exercício 2.1 - Primeiras Explorações
print("\n--- Exercício 2.1 - Primeiras Explorações ---")

print("Primeiras 10 linhas:")
print(iris.head(10))

print(f"\nDimensões do dataset: {iris.shape}")

print("\nTipos de dados:")
print(iris.dtypes)

print("\nValores ausentes:")
print(iris.isnull().sum())

# Exercício 2.2 - Seleção e Filtragem
print("\n--- Exercício 2.2 - Seleção e Filtragem ---")

# Selecionando uma coluna
print("Coluna 'sepal_length' (primeiras 5 valores):")
print(iris['sepal_length'].head())

# Selecionando múltiplas colunas
print("\nColunas 'petal_length' e 'petal_width' (primeiras 5 linhas):")
print(iris[['petal_length', 'petal_width']].head())

# Selecionando linhas específicas
print("\nLinhas 20 a 30:")
print(iris.iloc[20:31])

# Filtrando por espécie
print("\nObservações da espécie 'setosa' (primeiras 5):")
setosa = iris[iris['species'] == 'setosa']
print(setosa.head())
print(f"Total de observações setosa: {len(setosa)}")

# Filtrando por condição numérica
print("\nObservações onde petal_length > 4.0:")
filtro_petal = iris[iris['petal_length'] > 4.0]
print(f"Total de observações com petal_length > 4.0: {len(filtro_petal)}")

# ============================================================================
# Parte 3: Estatística Descritiva - Dataset Tips
# ============================================================================

print("\n=== PARTE 3: ESTATÍSTICA DESCRITIVA - TIPS ===")

# Exercício 3.1 - Variáveis Qualitativas
print("\n--- Exercício 3.1 - Variáveis Qualitativas ---")

# Frequência absoluta de 'day'
print("Frequência absoluta de 'day':")
print(tips['day'].value_counts())

# Frequência relativa de 'time'
print("\nFrequência relativa de 'time':")
print(tips['time'].value_counts(normalize=True))

# Gráfico de barras para 'smoker'
plt.figure(figsize=(8, 5))
tips['smoker'].value_counts().plot(kind='bar')
plt.title("Distribuição de Fumantes")
plt.xlabel("Fumante")
plt.ylabel("Frequência")
plt.xticks(rotation=0)
plt.show()
plt.close('all')

# Exercício 3.2 - Variáveis Quantitativas
print("\n--- Exercício 3.2 - Variáveis Quantitativas ---")

# Resumo descritivo de 'total_bill'
print("Resumo descritivo de 'total_bill':")
print(tips['total_bill'].describe())

# Medidas separadas de 'tip'
print(f"\nMédia de 'tip': {tips['tip'].mean():.2f}")
print(f"Mediana de 'tip': {tips['tip'].median():.2f}")
print(f"Desvio padrão de 'tip': {tips['tip'].std():.2f}")

# Histograma de 'total_bill'
plt.figure(figsize=(8, 5))
tips['total_bill'].hist(bins=8, edgecolor='black')
plt.title("Histograma de Total da Conta")
plt.xlabel("Total da Conta ($)")
plt.ylabel("Frequência")
plt.show()
plt.close('all')

# Boxplot de 'tip'
plt.figure(figsize=(6, 8))
tips['tip'].plot(kind='box')
plt.title("Boxplot de Gorjetas")
plt.ylabel("Gorjeta ($)")
plt.show()
plt.close('all')

# Exercício 3.3 - Quartis e Medidas de Posição
print("\n--- Exercício 3.3 - Quartis e Medidas de Posição ---")

# Quartis de 'total_bill'
quartis = tips['total_bill'].quantile([0.25, 0.5, 0.75])
print("Quartis de 'total_bill':")
print(quartis)

# Percentil 90 de 'tip'
percentil_90 = tips['tip'].quantile(0.9)
print(f"\nPercentil 90 de 'tip': {percentil_90:.2f}")

# Comparando média e mediana de 'size'
media_size = tips['size'].mean()
mediana_size = tips['size'].median()
print(f"\nMédia de 'size': {media_size:.2f}")
print(f"Mediana de 'size': {mediana_size:.2f}")
print("Interpretação: Como média > mediana, a distribuição tem assimetria positiva (cauda à direita)")

# Exercício 3.4 - Padronização (Z-score)
print("\n--- Exercício 3.4 - Padronização ---")

# Calculando Z-score
media_bill = tips['total_bill'].mean()
desvio_bill = tips['total_bill'].std()
tips['zscore_bill'] = (tips['total_bill'] - media_bill) / desvio_bill

print(f"Média do Z-score: {tips['zscore_bill'].mean():.10f}")
print(f"Desvio padrão do Z-score: {tips['zscore_bill'].std():.2f}")

# Histogramas comparativos
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Variável original
axes[0].hist(tips['total_bill'], bins=15, edgecolor='black', alpha=0.7)
axes[0].set_title("Total da Conta - Original")
axes[0].set_xlabel("Total da Conta ($)")
axes[0].set_ylabel("Frequência")

# Z-score
axes[1].hist(tips['zscore_bill'], bins=15, edgecolor='black', alpha=0.7, color='orange')
axes[1].set_title("Total da Conta - Z-Score")
axes[1].set_xlabel("Z-Score")
axes[1].set_ylabel("Frequência")

plt.tight_layout()
plt.show()
plt.close('all')
# ============================================================================
# Parte 4: Medidas de Associação
# ============================================================================

# Exercício 4.1 - Associação entre Variáveis Qualitativas

# Tabela de contingência
contingencia = pd.crosstab(tips['day'], tips['time'])
contingencia

# Frequências relativas por linha
freq_linha = contingencia.div(contingencia.sum(axis=1), axis=0)
freq_linha

# Frequências relativas por coluna
freq_coluna = contingencia.div(contingencia.sum(axis=0), axis=1)
freq_coluna

# Gráfico de barras agrupadas
contingencia_smoker = pd.crosstab(tips['day'], tips['smoker'])
plt.figure(figsize=(10, 6))
contingencia_smoker.plot(kind='bar', stacked=False)
plt.title("Associação entre Dia da Semana e Fumantes")
plt.xlabel("Dia da Semana")
plt.ylabel("Frequência")
plt.legend(title="Fumante")
plt.xticks(rotation=45)
plt.show()
plt.close('all')

# Exercício 4.2 - Associação entre Variáveis Quantitativas (Iris)

# Gráfico de dispersão
plt.figure(figsize=(8, 6))
plt.scatter(iris['sepal_length'], iris['petal_length'], alpha=0.7)
plt.title("Associação entre Comprimento da Sépala e Pétala")
plt.xlabel("Comprimento da Sépala (cm)")
plt.ylabel("Comprimento da Pétala (cm)")
plt.show()
plt.close('all')

# Covariância
cov_matrix = iris[['sepal_length', 'petal_length']].cov()
cov_matrix

# Correlação
corr_matrix = iris[['sepal_length', 'petal_length']].corr()
corr_matrix

# Correlação específica
correlacao = iris['sepal_length'].corr(iris['petal_length'])
correlacao
# Interpretação: Correlação forte positiva (> 0.8)

# Exercício 4.3 - Associação Quantitativa vs Qualitativa

# Tips: média de tip por time
tips.groupby('time')['tip'].mean()

# Boxplot total_bill por day
plt.figure(figsize=(10, 6))
sns.boxplot(data=tips, x='day', y='total_bill')
plt.title("Distribuição da Conta Total por Dia da Semana")
plt.xlabel("Dia da Semana")
plt.ylabel("Conta Total ($)")
plt.show()
plt.close('all')

# Pointplot tip por smoker
plt.figure(figsize=(8, 6))
sns.pointplot(data=tips, x='smoker', y='tip', capsize=0.1, color='black', errorbar='sd')
plt.title("Média de Gorjeta por Fumante (com desvio padrão)")
plt.xlabel("Fumante")
plt.ylabel("Gorjeta ($)")
plt.show()
plt.close('all')

# Iris: resumo petal_width por species
iris.groupby('species')['petal_width'].describe()

# Boxplot sepal_width por species
plt.figure(figsize=(10, 6))
sns.boxplot(data=iris, x='species', y='sepal_width')
plt.title("Distribuição da Largura da Sépala por Espécie")
plt.xlabel("Espécie")
plt.ylabel("Largura da Sépala (cm)")
plt.show()
plt.close('all')

# Exercício 4.4 - Análises Multivariadas

# Tips: scatter plot com cores
plt.figure(figsize=(10, 6))
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='smoker')
plt.title("Relação Conta Total vs Gorjeta por Fumante")
plt.xlabel("Conta Total ($)")
plt.ylabel("Gorjeta ($)")
plt.show()
plt.close('all')

# Iris: pairplot
sns.pairplot(data=iris, hue='species', diag_kind='kde')
plt.suptitle("Matriz de Gráficos de Dispersão - Iris", y=1.02)
plt.show()
plt.close('all')

# Tips: lmplot com regressão
sns.lmplot(data=tips, x='total_bill', y='tip', hue='time', height=6, aspect=1.2, ci=None)
plt.title("Relação Conta Total vs Gorjeta por Período (com regressão)")
plt.show()
plt.close('all')

# ============================================================================
# Desafios Extras
# ============================================================================

# Desafio 1: Gorjeta fumantes vs não fumantes por dia
contingencia_desafio = pd.crosstab(tips['day'], tips['smoker'])
contingencia_desafio

plt.figure(figsize=(10, 6))
tips.groupby(['day', 'smoker'])['tip'].mean().unstack().plot(kind='bar')
plt.title("Gorjeta Média por Dia e Fumante")
plt.xlabel("Dia da Semana")
plt.ylabel("Gorjeta Média ($)")
plt.legend(title="Fumante")
plt.xticks(rotation=45)
plt.show()
plt.close('all')

# Desafio 2: Coeficiente de variação por espécie (Iris)
# Setosa
dados_setosa = iris[iris['species'] == 'setosa']
cv_setosa_sepal_length = dados_setosa['sepal_length'].std() / dados_setosa['sepal_length'].mean()
cv_setosa_sepal_width = dados_setosa['sepal_width'].std() / dados_setosa['sepal_width'].mean()
cv_setosa_petal_length = dados_setosa['petal_length'].std() / dados_setosa['petal_length'].mean()
cv_setosa_petal_width = dados_setosa['petal_width'].std() / dados_setosa['petal_width'].mean()

# Versicolor
dados_versicolor = iris[iris['species'] == 'versicolor']
cv_versicolor_sepal_length = dados_versicolor['sepal_length'].std() / dados_versicolor['sepal_length'].mean()
cv_versicolor_sepal_width = dados_versicolor['sepal_width'].std() / dados_versicolor['sepal_width'].mean()
cv_versicolor_petal_length = dados_versicolor['petal_length'].std() / dados_versicolor['petal_length'].mean()
cv_versicolor_petal_width = dados_versicolor['petal_width'].std() / dados_versicolor['petal_width'].mean()

# Virginica
dados_virginica = iris[iris['species'] == 'virginica']
cv_virginica_sepal_length = dados_virginica['sepal_length'].std() / dados_virginica['sepal_length'].mean()
cv_virginica_sepal_width = dados_virginica['sepal_width'].std() / dados_virginica['sepal_width'].mean()
cv_virginica_petal_length = dados_virginica['petal_length'].std() / dados_virginica['petal_length'].mean()
cv_virginica_petal_width = dados_virginica['petal_width'].std() / dados_virginica['petal_width'].mean()

# Desafio 3: Taxa de gorjeta
tips['tip_rate'] = (tips['tip'] / tips['total_bill']) * 100
tips['tip_rate'].describe()

plt.figure(figsize=(10, 6))
sns.boxplot(data=tips, x='day', y='tip_rate')
plt.title("Taxa de Gorjeta por Dia da Semana")
plt.xlabel("Dia da Semana")
plt.ylabel("Taxa de Gorjeta (%)")
plt.show()
plt.close('all')lmplot(data=tips, x='total_bill', y='tip', hue='time', height=6, aspect=1.2, ci=None)
plt.title("Relação Conta Total vs Gorjeta por Período (com regressão)")
plt.show()
plt.close('all')

# ============================================================================
# Desafios Extras
# ============================================================================

print("\n=== DESAFIOS EXTRAS ===")

# Desafio 1: Gorjeta fumantes vs não fumantes por dia
print("\n--- Desafio 1 ---")
contingencia_desafio = pd.crosstab(tips['day'], tips['smoker'])
print("Fumantes vs Não fumantes por dia:")
print(contingencia_desafio)

plt.figure(figsize=(10, 6))
tips.groupby(['day', 'smoker'])['tip'].mean().unstack().plot(kind='bar')
plt.title("Gorjeta Média por Dia e Fumante")
plt.xlabel("Dia da Semana")
plt.ylabel("Gorjeta Média ($)")
plt.legend(title="Fumante")
plt.xticks(rotation=45)
plt.show()
plt.close('all')

# Desafio 2: Coeficiente de variação por espécie (Iris)
print("\n--- Desafio 2 ---")
print("Coeficiente de variação por espécie:")
for especie in iris['species'].unique():
    dados_especie = iris[iris['species'] == especie]
    print(f"\n{especie.upper()}:")
    for col in ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']:
        cv = dados_especie[col].std() / dados_especie[col].mean()
        print(f"  {col}: {cv:.3f}")

# Desafio 3: Taxa de gorjeta
print("\n--- Desafio 3 ---")
tips['tip_rate'] = (tips['tip'] / tips['total_bill']) * 100
print("Estatísticas da taxa de gorjeta (%):")
print(tips['tip_rate'].describe())

plt.figure(figsize=(10, 6))
sns.boxplot(data=tips, x='day', y='tip_rate')
plt.title("Taxa de Gorjeta por Dia da Semana")
plt.xlabel("Dia da Semana")
plt.ylabel("Taxa de Gorjeta (%)")
plt.show()
plt.close('all')

print("\nTodas as atividades foram concluídas com sucesso!")
