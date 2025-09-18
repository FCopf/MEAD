# ================================================================================
# ANÁLISE DE COMPONENTES PRINCIPAIS (PCA)
# Material didático para aula de Ciências de Dados
# ================================================================================

# ============================================================================
# PARTE 1: IMPORTAÇÃO DE BIBLIOTECAS
# ============================================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from statsmodels.nonparametric.smoothers_lowess import lowess
from scipy.stats import pearsonr

# Configurações visuais
plt.style.use('default')
sns.set_palette("husl")

# ============================================================================
# PARTE 2: INTRODUÇÃO AO PCA COM DADOS BIDIMENSIONAIS
# ============================================================================

# Carregando os dados
Y = pd.read_csv('https://raw.githubusercontent.com/FCopf/datasets/refs/heads/main/Notas.csv')

# Visualizando estrutura dos dados
Y

# Selecionando apenas duas variáveis para análise inicial
Y_2d = Y[['Estudo_horas', 'Frequencia']]

# ----------------------------------------------------------------------------
# Visualização dos dados originais
# ----------------------------------------------------------------------------
plt.figure(figsize=(10, 8))
sns.scatterplot(data=Y_2d, x='Estudo_horas', y='Frequencia', 
                alpha=0.7, s=100)

# Adicionando rótulos dos alunos
for i, nome in enumerate(Y['Nome']):
    plt.text(x=Y_2d['Estudo_horas'][i] + 0.1,
             y=Y_2d['Frequencia'][i] + 0.1,
             s=nome, fontsize=9)

plt.title('Tempo de Estudo vs. Frequência nas Aulas', fontsize=14)
plt.xlabel('Tempo de Estudo (horas)', fontsize=12)
plt.ylabel('Frequência (%)', fontsize=12)
plt.ylim(30.5, 40.5)
plt.xlim(4, 15.5)
plt.grid(True, alpha=0.3)
plt.show()

# ----------------------------------------------------------------------------
# Aplicando PCA aos dados bidimensionais
# ----------------------------------------------------------------------------
# Criando e ajustando o modelo PCA
pca_2d = PCA()
pca_2d.fit(Y_2d)

# Transformando os dados para o novo espaço de componentes principais
F_2d = pd.DataFrame(pca_2d.transform(Y_2d), columns=['PCA1', 'PCA2'])

# Adicionando os componentes principais ao dataframe original
Y[['PCA1', 'PCA2']] = F_2d

# Visualizando a variância explicada
variancia_explicada = pca_2d.explained_variance_
variancia_explicada

# Variância total
np.sum(variancia_explicada)

# Matriz de covariância original
Y_2d.cov(ddof=1)

# ----------------------------------------------------------------------------
# Visualização dos componentes principais no espaço original
# ----------------------------------------------------------------------------
plt.figure(figsize=(8, 8))
sns.scatterplot(data=Y, x='Estudo_horas', y='Frequencia', 
                alpha=0.7, s=100)
plt.ylim(29.5, 41.5)
plt.xlim(3, 17)
# Adicionando rótulos
for i, nome in enumerate(Y['Nome']):
    plt.text(x=Y['Estudo_horas'][i] + 0.1,
             y=Y['Frequencia'][i] + 0.1,
             s=nome, fontsize=9)

# Calculando o centro dos dados
centro = Y_2d.mean().to_numpy()
plt.scatter(centro[0], centro[1], color='black', s=100, marker='x', 
            linewidth=2, label='Centro dos dados')

# Desenhando as direções dos componentes principais (autovetores)
U = pca_2d.components_  # Matriz de autovetores
escala = 10  # Fator de escala para visualização
rotacao = np.degrees(np.arctan2(U[:, 1], U[:, 0]))

# --- Componente Principal 1 ---
plt.arrow(centro[0], centro[1], 
          U[0, 0] * escala * 0.6, U[0, 1] * escala * 0.6,
          head_width=0.3, head_length=0.2, fc='red', ec='red', 
          linewidth=2, alpha=0.7)

# Segmento de reta PC1 (pontilhado)
x1, y1 = centro[0] - U[0, 0] * escala, centro[1] - U[0, 1] * escala
x2, y2 = centro[0] + U[0, 0] * escala, centro[1] + U[0, 1] * escala
plt.plot([x1, x2], [y1, y2], color='red', linestyle='--', linewidth=1.0)

# Adicionando rótulos do componente 1
plt.text(x=centro[0] + U[0, 0] * escala * 0.3, 
         y=centro[1] + U[0, 1] * escala * 0.3 + 0.5,
         s="Componente Principal 1", rotation=rotacao[0], fontsize=12, 
         color='red', fontweight='bold')

# --- Componente Principal 2 ---
plt.arrow(centro[0], centro[1], 
          U[1, 0] * escala * 0.6, U[1, 1] * escala * 0.6,
          head_width=0.3, head_length=0.2, fc='red', ec='red', 
          linewidth=2, alpha=0.7)

# Segmento de reta PC2 (pontilhado)
x1, y1 = centro[0] - U[1, 0] * escala, centro[1] - U[1, 1] * escala
x2, y2 = centro[0] + U[1, 0] * escala, centro[1] + U[1, 1] * escala
plt.plot([x1, x2], [y1, y2], color='red', linestyle='--', linewidth=1.0)

# Adicionando rótulos do componente 2
plt.text(x=centro[0] + U[1, 0] * escala * 0.5, 
         y=centro[1] + U[1, 1] * escala * 0.22,
         s="Componente Principal 2", rotation=rotacao[1]+180, fontsize=12, 
         color='red', fontweight='bold')

# Função auxiliar para projeção de pontos
def projetar_ponto(p, v, centro):
    """Projeta o ponto p sobre o vetor v a partir do centro"""
    p_rel = p - centro
    escalar = np.dot(p_rel, v) / np.dot(v, v)
    return centro + escalar * v

# Desenhando as projeções dos pontos no PC1
for i in range(len(Y_2d)):
    ponto = Y_2d.iloc[i].to_numpy()
    ponto_projetado = projetar_ponto(ponto, U[0, :], centro)
    plt.plot([ponto[0], ponto_projetado[0]], 
             [ponto[1], ponto_projetado[1]], 
             color='gray', linestyle=':', linewidth=1)

plt.ylim(30,41)
plt.xlim(2.5,16)

plt.title('Componentes Principais no Espaço Original', fontsize=14)
plt.xlabel('Tempo de Estudo (horas)', fontsize=12)
plt.ylabel('Frequência (%)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

# ----------------------------------------------------------------------------
# Visualização no espaço transformado (PCA)
# ----------------------------------------------------------------------------
plt.figure(figsize=(10, 8))
sns.scatterplot(data=Y, x='PCA1', y='PCA2', alpha=0.7, s=100)

# Linhas de referência nos eixos
plt.axhline(0, color='red', linestyle='--', alpha=0.5)
plt.axvline(0, color='red', linestyle='--', alpha=0.5)

# Adicionando nomes dos alunos
for i, nome in enumerate(Y['Nome']):
    plt.text(x=F_2d['PCA1'][i] + 0.1,
             y=F_2d['PCA2'][i] + 0.1,
             s=nome, fontsize=9)

plt.title('Dados Transformados: Espaço dos Componentes Principais', fontsize=14)
plt.xlabel(f'PC1 ({variancia_explicada[0]*100:.1f}% da variância)', fontsize=12)
plt.ylabel(f'PC2 ({variancia_explicada[1]*100:.1f}% da variância)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

# ----------------------------------------------------------------------------
# Comparação lado a lado: Espaço Original vs Espaço PCA
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# Gráfico 1: Dados Originais
ax1 = axes[0]
sns.scatterplot(data=Y, x='Estudo_horas', y='Frequencia', 
                alpha=0.7, s=100, ax=ax1)
for i, nome in enumerate(Y['Nome']):
    ax1.text(x=Y['Estudo_horas'][i] + 0.1,
             y=Y['Frequencia'][i] + 0.1,
             s=nome, fontsize=9)
ax1.set_title('Espaço Original', fontsize=14)
ax1.set_xlabel('Tempo de Estudo (horas)', fontsize=12)
ax1.set_ylabel('Frequência (%)', fontsize=12)
ax1.set_ylim(30.5, 40.5)
ax1.set_xlim(4, 15.5)
ax1.grid(True, alpha=0.3)

# Gráfico 2: Espaço PCA
ax2 = axes[1]
sns.scatterplot(data=Y, x='PCA1', y='PCA2', alpha=0.7, s=100, ax=ax2)
ax2.axhline(0, color='red', linestyle='--', alpha=0.5)
ax2.axvline(0, color='red', linestyle='--', alpha=0.5)

# Rótulos dos pontos
for i, nome in enumerate(Y['Nome']):
    ax2.text(x=F_2d['PCA1'][i] + 0.1, 
             y=F_2d['PCA2'][i] + 0.1, 
             s=nome, fontsize=9)

# --- Adicionando setas dos componentes principais ---
escala = 3  # fator de escala para visualização

# Rótulos das setas
ax2.text(escala + 0.2, 0.1, "PC1", fontsize=12, color='red', fontweight='bold')
ax2.text(0.1, escala + 0.2, "PC2", fontsize=12, color='red', fontweight='bold')

# Ajustes finais
ax2.set_title('Espaço dos Componentes Principais', fontsize=14)
ax2.set_xlabel(f'PC1 ({variancia_explicada[0]*100:.1f}% da variância)', fontsize=12)
ax2.set_ylabel(f'PC2 ({variancia_explicada[1]*100:.1f}% da variância)', fontsize=12)
ax2.grid(True, alpha=0.3)

plt.suptitle('Comparação: Dados Originais vs PCA', fontsize=16, y=1.02)
plt.tight_layout()
ax2.set_ylim(-6,8)
ax2.set_xlim(-6,8)
plt.show()

# ============================================================================
# PARTE 3: PCA COM TRÊS VARIÁVEIS (INCLUINDO NOTA FINAL)
# ============================================================================
# Recarregando os dados para análise limpa
Y = pd.read_csv('https://raw.githubusercontent.com/FCopf/datasets/refs/heads/main/Notas.csv')

# Selecionando três variáveis para análise
vars_pca = ['Estudo_horas', 'Frequencia', 'Nota_final']
Yvar = Y[vars_pca]

# ----------------------------------------------------------------------------
# Padronização dos dados: matriz de covariância versus matriz de correlação
# ----------------------------------------------------------------------------
# Padronizando os dados (média=0, desvio padrão=1)
scaler = StandardScaler()
Ypadr = scaler.fit_transform(Yvar)
Ypadr_df = pd.DataFrame(Ypadr, columns=vars_pca)

Yvar.mean()
Ypadr_df.mean()

Yvar.std(ddof=0)
Ypadr_df.std(ddof=0)

Yvar.cov(ddof=0)
Yvar.corr()

Ypadr_df.cov(ddof=0)
Ypadr_df.corr()

# ----------------------------------------------------------------------------
# Aplicando PCA aos dados tridimensionais
# ----------------------------------------------------------------------------
pca_3d = PCA()
F_3d = pca_3d.fit_transform(Ypadr)
F_3d_df = pd.DataFrame(F_3d, columns=[f'PCA{i+1}' for i in range(F_3d.shape[1])])

# Adicionando componentes ao dataframe original
Y[['PCA1', 'PCA2', 'PCA3']] = F_3d_df

# Análise da variância explicada
var_explicada = pca_3d.explained_variance_
var_explicada_ratio = pca_3d.explained_variance_ratio_
var_acumulada = np.cumsum(var_explicada_ratio)

print("\n" + "-"*50)
print("Análise da Variância:")
for i in range(len(var_explicada_ratio)):
    print(f"  PC{i+1}: {var_explicada_ratio[i]*100:.2f}% "
          f"(acumulada: {var_acumulada[i]*100:.2f}%)")

# ----------------------------------------------------------------------------
# Scree Plot - Visualização da variância explicada
# ----------------------------------------------------------------------------
# Gráfico de barras - Variância individual
plt.figure(figsize=(8, 5))
plt.bar(range(1, len(var_explicada_ratio) + 1), 
        var_explicada_ratio * 100, 
        alpha=0.7, color='steelblue')
plt.xticks(range(1, len(var_explicada_ratio) + 1))
plt.xlabel('Componente Principal', fontsize=12)
plt.ylabel('Variância Explicada (%)', fontsize=12)
plt.title('Scree Plot - Variância Individual', fontsize=14)
plt.grid(True, alpha=0.3)

# Adicionar valores no topo das barras
for i, v in enumerate(var_explicada_ratio):
    plt.text(i + 1, v * 100 + 1, f'{v*100:.1f}%', 
             ha='center', fontsize=10)

plt.tight_layout()
plt.show()

# ----------------------------------------------------------------------------
# Biplot - PCA com loadings (contribuição das variáveis)
# ----------------------------------------------------------------------------
plt.figure(figsize=(10, 10))

# Plotar as observações (scores)
sns.scatterplot(data=Y, x='PCA1', y='PCA2', alpha=0.7, s=100)

# Linhas de referência
plt.axhline(0, color='gray', linestyle='--', alpha=0.3)
plt.axvline(0, color='gray', linestyle='--', alpha=0.3)

# Adicionar nomes dos alunos
for i, nome in enumerate(Y['Nome']):
    plt.text(x=F_3d_df['PCA1'][i] + 0.05, 
             y=F_3d_df['PCA2'][i] + 0.05, 
             s=nome, fontsize=9)

# Calcular e plotar loadings (vetores das variáveis originais)
loadings = pca_3d.components_.T * np.sqrt(pca_3d.explained_variance_)

# Escala para os vetores de loading
escala_loading = 1.5

for i, var in enumerate(vars_pca):
    # Desenhar seta
    plt.arrow(0, 0, 
              loadings[i, 0] * escala_loading, 
              loadings[i, 1] * escala_loading,
              color='red', alpha=0.7, head_width=0.03, 
              head_length=0.08, linewidth=2)
    
    # Adicionar rótulo da variável
    plt.text(loadings[i, 0] * escala_loading * 1.25, 
             loadings[i, 1] * escala_loading * 1.25,
             var, color='red', fontsize=11,
             ha='center')

plt.title('Biplot: Scores e Loadings do PCA', fontsize=14)
plt.xlabel(f'PC1 ({var_explicada_ratio[0]*100:.1f}% da variância)', fontsize=12)
plt.ylabel(f'PC2 ({var_explicada_ratio[1]*100:.1f}% da variância)', fontsize=12)
plt.grid(True, alpha=0.3)

plt.show()

# ============================================================================
# PARTE 4: ANÁLISE DE CORRELAÇÕES E COVARIÂNCIAS
# ============================================================================
# ----------------------------------------------------------------------------
# Funções auxiliares para visualização
# ----------------------------------------------------------------------------
def scatter_com_lowess(x, y, color=None, label=None, frac=0.6, **kws):
    """Gráfico de dispersão com curva LOWESS suavizada"""
    ax = plt.gca()
    # Scatter plot
    ax.scatter(x, y, alpha=0.7, color=color, s=50)
    # Curva LOWESS
    smoothed = lowess(y, x, frac=frac)
    ax.plot(smoothed[:, 0], smoothed[:, 1], 
            color="red", linewidth=2, alpha=0.8)

def mostrar_correlacao(x, y, **kws):
    """Calcula e exibe o coeficiente de correlação de Pearson"""
    r, _ = pearsonr(x, y)
    ax = plt.gca()
    ax.annotate(f"r = {r:.2f}", 
                xy=(.5, .5), xycoords=ax.transAxes,
                ha='center', va='center', 
                fontsize=14, color='red', fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.3", 
                         facecolor="yellow", alpha=0.3))

# ----------------------------------------------------------------------------
# Matriz de correlação visual
# ----------------------------------------------------------------------------
print("\nMatriz de Correlação:")
print(Y[vars_pca].corr())

plt.figure(figsize=(12, 10))

# Criar PairGrid para visualização múltipla
g = sns.PairGrid(Y[vars_pca], diag_sharey=False)

# Triangular inferior: scatter com curva de tendência
g.map_lower(scatter_com_lowess, frac=0.7)

# Triangular superior: coeficiente de correlação
g.map_upper(mostrar_correlacao)

# Diagonal: distribuição das variáveis
g.map_diag(sns.histplot, kde=True, alpha=0.6, color='steelblue')

plt.suptitle('Matriz de Correlações e Distribuições', fontsize=16, y=1.02)
plt.tight_layout()
plt.show()

# ============================================================================
# PARTE 5: EXEMPLO SIMULADO COM DIFERENTES ESTRUTURAS DE CORRELAÇÃO
# ============================================================================

# ----------------------------------------------------------------------------
# Simulação 1: Variáveis com alta correlação em pares
# ----------------------------------------------------------------------------
# Configuração do gerador de números aleatórios
rng = np.random.default_rng(42)
media = np.array([0, 0, 0, 0])

# Matriz de covariância com correlações específicas
cov_correlacionada = np.array([
    [1.0, 0.9, 0.1, 0.1],
    [0.9, 1.0, 0.1, 0.1],
    [0.1, 0.1, 1.0, 0.8],
    [0.1, 0.1, 0.8, 1.0]
])

plt.figure(figsize=(12, 10))

# Gerar amostras
n_amostras = 200
dados_correlacionados = rng.multivariate_normal(media, cov_correlacionada, 
                                                 size=n_amostras)
X_corr = pd.DataFrame(dados_correlacionados, 
                      columns=[f'X{i+1}' for i in range(4)])

# Criar PairGrid para visualização múltipla
g = sns.PairGrid(X_corr, diag_sharey=False)
g.map_lower(scatter_com_lowess, frac=0.7)
g.map_upper(mostrar_correlacao)
g.map_diag(sns.histplot, kde=True, alpha=0.6, color='steelblue')
plt.suptitle('Matriz de Correlações e Distribuições', fontsize=16, y=1.02)
plt.tight_layout()
plt.show()

# ----------------------------------------------------------------------------
# Simulação 2: Variáveis independentes
# ----------------------------------------------------------------------------
# Matriz de covariância identidade (variáveis independentes)
cov_independente = np.eye(4)

# Gerar amostras
dados_independentes = rng.multivariate_normal(media, cov_independente, 
                                              size=n_amostras)
X_indep = pd.DataFrame(dados_independentes, 
                       columns=[f'X{i+1}' for i in range(4)])

# Criar PairGrid para visualização múltipla
g = sns.PairGrid(X_indep, diag_sharey=False)
g.map_lower(scatter_com_lowess, frac=0.7)
g.map_upper(mostrar_correlacao)
g.map_diag(sns.histplot, kde=True, alpha=0.6, color='steelblue')
plt.suptitle('Matriz de Correlações e Distribuições', fontsize=16, y=1.02)
plt.tight_layout()
plt.show()


# ----------------------------------------------------------------------------
# Comparação dos PCAs nas duas situações
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(12, 12))

for idx, (X_sim, titulo) in enumerate([(X_corr, 'Variáveis Correlacionadas'), 
                                        (X_indep, 'Variáveis Independentes')]):
    
    # Padronizar dados
    X_sim_scaled = StandardScaler().fit_transform(X_sim)
    
    # Aplicar PCA
    pca_sim = PCA()
    F_sim = pca_sim.fit_transform(X_sim_scaled)
    F_sim_df = pd.DataFrame(F_sim, columns=[f'PC{i+1}' for i in range(4)])
    
    var_exp_sim = pca_sim.explained_variance_ratio_
    
    # Gráfico 1: Scree Plot
    ax = axes[idx, 0]
    ax.bar(range(1, 5), var_exp_sim * 100, alpha=0.7, color='steelblue')
    ax.set_xlabel('Componente Principal')
    ax.set_ylabel('Variância Explicada (%)')
    ax.set_title(f'{titulo}\nScree Plot')
    ax.set_xticks(range(1, 5))
    ax.grid(True, alpha=0.3)
    
    # Adicionar valores
    for i, v in enumerate(var_exp_sim):
        ax.text(i + 1, v * 100 + 1, f'{v*100:.1f}%', 
                ha='center', fontsize=9)
    
    # Gráfico 2: PC1 vs PC2
    ax = axes[idx, 1]
    ax.scatter(F_sim_df['PC1'], F_sim_df['PC2'], alpha=0.5, s=30)
    ax.axhline(0, color='gray', linestyle='--', alpha=0.3)
    ax.axvline(0, color='gray', linestyle='--', alpha=0.3)
    ax.set_xlabel(f'PC1 ({var_exp_sim[0]*100:.1f}%)')
    ax.set_ylabel(f'PC2 ({var_exp_sim[1]*100:.1f}%)')
    ax.set_title(f'{titulo}\nPC1 vs PC2')
    ax.grid(True, alpha=0.3)
    
    # Adicionar loadings
    loadings_sim = pca_sim.components_.T * np.sqrt(pca_sim.explained_variance_)
    for i, var in enumerate(X_sim.columns):
        ax.arrow(0, 0, loadings_sim[i, 0]*2, loadings_sim[i, 1]*2,
                color='red', alpha=0.7, head_width=0.1, linewidth=1.5)
        ax.text(loadings_sim[i, 0]*2.2, loadings_sim[i, 1]*2.2,
               var, color='red', fontsize=10, fontweight='bold')


plt.suptitle('Comparação: Efeito da Estrutura de Correlação no PCA', 
             fontsize=16, y=1.02)
plt.tight_layout()
plt.show()