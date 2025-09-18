# Estrutura e Tipos de Dados

# Pacotes
import pandas as pd
# pip install palmerpenguins
from palmerpenguins import load_penguins

# --------------------------------------------
# Carregando os dados
penguins = load_penguins()

# Visualizações iniciais
penguins.shape
penguins.head()
penguins.dtypes

# --------------------------------------------
# Selecionando linhas e colunas em um DataFrame

# Selecionar colunas
penguins['species']
penguins[['species', 'island', 'body_mass_g']]

# Selecionar linhas
penguins.iloc[0]    # primeira linha
penguins.iloc[10]   # 11ª linha

# Selecionar linhas específicas e colunas específicas
penguins.iloc[0:5, 0:3]   # linhas 0 a 4, colunas 0 a 2

# Selecionar linhas por condição
filtro = penguins['species'] == 'Adelie'
penguins[filtro]

# Selecionar linhas com múltiplas condições
filtro2 = (penguins['species'] == 'Adelie') &  (penguins['island'] == 'Torgersen')
filtro2
penguins[filtro2]

penguins[filtro2].shape

# --------------------------------------------
# Dados Ausentes
penguins.isnull().sum(axis = 1)

# Removendo valores ausentes
penguins2 = penguins.dropna()
penguins2.isnull().sum(axis = 0)

