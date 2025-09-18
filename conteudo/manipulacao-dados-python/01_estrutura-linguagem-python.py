# Introdução ao Python

# Pacotes essenciais
import math
import numpy as np
import pandas as pd


# --------------------------------------------
# Operações aritméticas
2 + 4
2 * 4
2 - 4
2**4
13 / 2
13 // 2
13 % 2
5 * (9 + 2)
5 * 9 + 2
3 + 4**2

# Funções matemáticas
math.log(100)
math.log10(100)
math.sqrt(36)
math.pi
math.sin(0.5 * math.pi)
math.sin(math.radians(90))

np.log(100)
np.sqrt(36)

# --------------------------------------------
# Atribuição de valores
x = np.log(100)
x
y = x + 10
y
x = 5
y = x + 10
y

a = math.sqrt(49)
A = math.sqrt(81)
a, A

# --------------------------------------------
# Listas
x = [4, 3.0, 5, 9, 10]
x
type(x)
len(x)
x[5]
x[0:]

x * 2

# Arrays NumPy
y = np.array(x)
y
type(y)
len(y)
y[0]
y[0:2]

x * 2
y * 2
[i * 2 for i in x]


# Sequências
list(range(2, 11))
np.linspace(2, 10, 4)
np.repeat(4, 6)
[2, 5] * 3
np.tile([2, 5], 3)

# --------------------------------------------
# Strings
especies = ["Deuterodon iguape", 
"Characidium japuhybense", 
"Trichomycterus zonatus"]
especies
sorted(especies)
especies = [
    "Deuterodon iguape",
    "Characidium japuhybense",
    "Trichomycterus zonatus",
    4]

especies[3] + 3

# --------------------------------------------
# Arrays 2D (matrizes)
x = [
    [21, 26, 5, 18],
    [17, 28, 20, 15],
    [13, 14, 27, 22]
]

x
x[0]
x[0][0]

y = np.array(x)
y
y[0]
y[0][0]
y[0, 0]
y[0,]
y[0,:]
y[:,0]



# --------------------------------------------
# Dicionários

nosso_dic = {
    'Ilha' : ['Ilhabela', 'Anchieta', 'Cardoso'],
    'Areaskm2': [347.5, 8.3, 131]
}
nosso_dic
nosso_dic.keys()

# --------------------------------------------
# DataFrames
df = pd.DataFrame(nosso_dic)
df
df['Ilha']