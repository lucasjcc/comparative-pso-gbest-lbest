import random
import math
import numpy as np

#Função de custo sincx
def funcao_custo(x):
    f = 0
    D = len(x)
    for i in range(D):
        f+=math.sin(x[i])/x
    return f

#Função de custo esfera
'''def funcao_custo(x):
    f = 0
    D = len(x)
    for i in range(D):
        f+=x[i]**2
    return f '''

#Função de custo Rastrigin
"""def funcao_custo(x):
    f = 0
    D = len(x)
    for i in range(D):
        f = f + (x[i]**2 + 10 * np.cos(2 * math.pi * x[i]) + 10)
    return f"""
