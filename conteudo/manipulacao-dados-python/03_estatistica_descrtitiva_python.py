# Estatística Descritiva e Visualização com Penguins
import pandas as pd
import numpy as np
from palmerpenguins import load_penguins
import matplotlib.pyplot as plt


# --------------------------------------------
# Carregando os dados
penguins = load_penguins().dropna()

# --------------------------------------------
# 1. Variáveis Qualitativas/Categóricas
penguins.dtypes
# Frequência absoluta
penguins['species'].value_counts()

# Frequência relativa
penguins['species'].value_counts(normalize=True)

# Gráfico de barras
penguins['species'].value_counts().plot(kind='bar')
plt.title("Número de Pinguins por Espécie")
plt.xlabel("Espécie")
plt.ylabel("Frequência")
plt.show()
plt.close('all')

penguins['island'].value_counts().plot(kind='bar')
# --------------------------------------------
# 2. Variáveis Quantitativas
penguins.dtypes
# Resumo descritivo
penguins['body_mass_g'].describe()
penguins.describe()


# Histograma
penguins['body_mass_g'].plot(kind='hist', 
                    bins=5, edgecolor = "white")
plt.title("Histograma da Massa Corporal")
plt.xlabel("Massa (g)")
plt.ylabel("Frequência")
plt.show()
plt.close('all')

# --------------------------------------------
# 3. Quartis
penguins['body_mass_g'].quantile(0.25)
penguins['body_mass_g'].quantile(0.50)  # mediana
penguins['body_mass_g'].quantile(0.75)

penguins['body_mass_g'].quantile([0.25, 0.5, 0.75])

# Boxplot
penguins['body_mass_g'].plot(kind='box')
plt.title("Boxplot da Massa Corporal")
plt.ylabel("Massa (g)")
plt.show()
plt.close('all')

# --------------------------------------------
# 4. Medidas de Tendência Central
penguins['body_mass_g'].mean()
penguins['body_mass_g'].median()

# --------------------------------------------
# 5. Medidas de Variação
penguins['body_mass_g'].std()
penguins['body_mass_g'].var()

x = penguins['body_mass_g']

np.sum((x - x.mean())**2) / (len(x) - 1))

# --------------------------------------------
# 6. Escore-Z - padronização
media = penguins['body_mass_g'].mean()
desvio_padrao = penguins['body_mass_g'].std()

penguins['zscore_massa'] = (penguins['body_mass_g'] - media) / desvio_padrao
penguins[['body_mass_g', 'zscore_massa']].head()

penguins[['body_mass_g', 'zscore_massa']].describe()

# --------------------------------------------
# Gráficos comparativos
fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=False)

# Histograma da variável original
axes[0].hist(penguins['body_mass_g'], bins=20, color='skyblue', edgecolor='black')
axes[0].set_title("Massa Corporal (g) - Original")
axes[0].set_xlabel("Massa (g)")
axes[0].set_ylabel("Frequência")

# Histograma da variável padronizada
axes[1].hist(penguins['zscore_massa'], bins=20, color='lightgreen', edgecolor='black')
axes[1].set_title("Massa Corporal - Z-Score")
axes[1].set_xlabel("Escore-Z")
axes[1].set_ylabel("Frequência")

plt.tight_layout()
plt.show()
plt.close('all')
