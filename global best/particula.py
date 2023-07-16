import math
import random
from funcoes_custo import funcao_custo

class Particula:
    def __init__(self, dimensoes, espaco_busca):
        self.posicao=[]             # posição da partícula
        self.b_posicao = []         # melhor posição da partícula
        self.velocidade=[]          # velocidade da partícula
        self.fitness = math.inf     # Avaliação da posição
        self.b_fitness = math.inf   # Melhor fitness encontrado

        #Inicialização uniforme da população dentro do espaço de busca
        for i in range(dimensoes):
            self.velocidade.append(random.uniform(-1,1))
            self.posicao.append(random.uniform(espaco_busca[0], espaco_busca[1]))
            self.b_posicao.append(self.posicao)

    # Checagem do fitness das partículas
    def calcular_fitness(self):
        self.fitness=funcao_custo(self.posicao)

        # Checa se a posição atual é a melhor
        if self.fitness < self.b_fitness:
            self.b_posicao=self.posicao
            self.b_fitness=self.fitness

    # Atualiza a velocidade da partícula
    def atualizar_velocidade(self, g_best_posicao, dimensoes, parametro_constricao, w, c1, c2):

        for i in range(dimensoes):
            r1=random.random()
            r2=random.random()

            v1=w*self.velocidade[i]
            v2=c1*r1*(self.b_posicao[i]-self.posicao[i])
            v3=c2*r2*(g_best_posicao[i]-self.posicao[i])
            self.velocidade[i]=parametro_constricao*(v1+v2+v3)

    #Atualiza posição da partícula
    def atualizar_posicao(self, dimensoes, espaco_busca):
        for i in range(dimensoes):
            self.posicao[i]=self.posicao[i] + self.velocidade[i]

            # Caso necessário, ajustar a posição para dentro dos limites de D
            if self.posicao[i] > espaco_busca[1]:
                self.posicao[i]=espaco_busca[1]

            if self.posicao[i] < espaco_busca[0]:
                self.posicao[i]=espaco_busca[0]