import pandas as pd
import matplotlib.pyplot as plt
from palmerpenguins import load_penguins
import seaborn as sns


# --------------------------------------------
# Carregando os dados
penguins = load_penguins().dropna()

# --------------------------------------------
# 1. Associação entre Duas Variáveis Qualitativas (Categóricas)
# Exemplo: Associação entre 'species' (espécie) e 'island' (ilha)

# Tabela de contingência (frequências observadas)
contingency_table = pd.crosstab(penguins['species'], 
                                penguins['island'])
contingency_table

# Frequências relativas marginais (por linha)
total_row = contingency_table.sum(axis=1)
total_row
relative_row = contingency_table.div(total_row, axis=0)
relative_row

# Frequências relativas marginais (por coluna)
total_col = contingency_table.sum(axis=0)
total_col
relative_col = contingency_table.div(total_col, axis=1)
relative_col

# Frequências relativas conjuntas
relative_joint = contingency_table / contingency_table.sum().sum()
relative_joint.sum(axis = 0).sum()

# Gráfico de barras agrupadas
contingency_table.plot(kind='bar', stacked=False) # stacked=True
plt.title("Associação entre Espécie e Ilha")
plt.xlabel("Espécie")
plt.ylabel("Frequência")
plt.legend(title="Ilha")
plt.show()
plt.close('all')

# Gráfico com seaborn
sns.countplot(data=penguins, x='island', hue='species')
plt.title("Associação entre Espécie e Ilha")
plt.xlabel("Espécie")
plt.ylabel("Frequência")
plt.legend(title="Ilha")
plt.show()
plt.close('all')

# --------------------------------------------
# 2. Associação entre Duas Variáveis Quantitativas
# Exemplo: Associação entre 'bill_length_mm' (comprimento do bico) e 'body_mass_g' (massa corporal)

# Gráfico de dispersão
sns.scatterplot(
    data=penguins,
    x='bill_length_mm',
    y='body_mass_g',
    hue='species'
)
plt.title("Associação entre Comprimento do Bico e Massa Corporal")
plt.xlabel("Comprimento do Bico (mm)")
plt.ylabel("Massa Corporal (g)")
plt.show()
plt.close('all')

# Covariância e Correlação
covariance = penguins[['bill_length_mm', 'body_mass_g']].cov()
covariance
correlation = penguins[['bill_length_mm', 'body_mass_g']].corr()
correlation

# Correlação como uma medida de covariâncioa das variáveis padronizadas
penguins_padr = penguins[['bill_length_mm', 'body_mass_g']].copy()
penguins_padr = (penguins_padr - penguins_padr.mean()) / penguins_padr.std()
penguins_padr.mean()
penguins_padr.std()
penguins_padr.cov()
penguins_padr.corr()

# --------------------------------------------
# 3. Associação entre Variável Quantitativa e Qualitativa
# Exemplo: Associação entre 'body_mass_g' (massa corporal - quantitativa) e 'species' (espécie - qualitativa)

# Resumo descritivo por grupo
grouped = penguins.groupby('species')['body_mass_g'].describe()
grouped

penguins.groupby('species')['bill_length_mm'].describe()

# Boxplot por grupos
sns.boxplot(x='species', y='bill_length_mm', data=penguins)
plt.title("Distribuição da Massa Corporal por Espécie")
plt.xlabel("Espécie")
plt.ylabel("Massa Corporal (g)")
plt.show()
plt.close('all')

# Gráfico de erros (média e desvio padrão)
means = penguins.groupby('species')['body_mass_g'].mean()
stds = penguins.groupby('species')['body_mass_g'].std()

sns.pointplot(
    data=penguins,
    x='species',
    y='body_mass_g',
    capsize=0.1,      # tamanho das barras de erro
    color='black',    # cor dos pontos e das barras de erro
    errorbar='sd'           # ci='sd' usa o desvio padrão ao invés do intervalo de confiança
)
plt.title("Média e Desvio Padrão da Massa Corporal por Espécie")
plt.xlabel("Espécie")
plt.ylabel("Massa Corporal (g)")
plt.show()
plt.close('all')

# --------------------------------------------
# 4. Variável Quantitativa como função de variável Quantitativa e Qualitativa
# Scatter plot com cores por espécie
sns.scatterplot(
    data=penguins,
    x='bill_length_mm',
    y='body_mass_g',
    # hue='species',
)
plt.title("Massa Corporal em função do Comprimento do Bico por Espécie")
plt.xlabel("Comprimento do Bico (mm)")
plt.ylabel("Massa Corporal (g)")
plt.show()
plt.close('all')

# Scatter plot com regressão separada por espécie
sns.lmplot(
    data=penguins,
    x='bill_length_mm',
    y='body_mass_g',
    hue='species',
    height=5,
    aspect=1.2,
    markers=['o','s','D'],
    ci=None
)
plt.title("Massa Corporal em função do Comprimento do Bico por Espécie (Regressão)")
plt.xlabel("Comprimento do Bico (mm)")
plt.ylabel("Massa Corporal (g)")
plt.show()
plt.close('all')

# Pairplot para variáveis quantitativas, colorindo por espécie
sns.pairplot(
    data=penguins,
    vars=['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'],
    hue='species',
    diag_kind='kde'   # 'kde'
)
plt.show()
plt.close('all')

sns.lmplot(
    data=penguins,
    x='flipper_length_mm',
    y='body_mass_g',
    hue='species',
    height=5,
    aspect=1.2,
    markers=['o','s','D'],
    ci=None
)
plt.show()
plt.close('all')

sns.lmplot(
    data=penguins,
    x='bill_depth_mm',
    y='bill_length_mm',
    hue='species',
    height=5,
    aspect=1.2,
    markers=['o','s','D'],
    ci=None
)
plt.show()
plt.close('all')

