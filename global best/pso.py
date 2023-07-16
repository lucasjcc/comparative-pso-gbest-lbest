#--- ------------DEPENDÊNCIAS ----------------------------------------------+

import random
import math
from particula import Particula
import time


#--- ------------PARÂMETROS ----------------------------------------------+

parametro_constricao = 1                    #Parâmetro de constrição
w = 1                                       #Inércia
c1 = 1.496180                               #Coeficiente de aceleração cognitivo
c2 = 1.496180                               #Coeficiente de aceleração social    
dimensoes = 1                               #Dimensão do problema
interacoes = 5000                           #Número de iterações desejadas
tamanho_populacao = 20                      #Tamanho da população (tamanho do enxame - swarm)
espaco_busca = [-math.pi/3,math.pi/3]       #Espaço de busca do algortimo
quantidade_execucoes = 1                    #Quantidade de testes do algoritmo


#--- ------------MAIN----------------------------------------------+

def main():
    melhores_solucoes_execucao = []
    media = 0
    desvio_padrao = 0

    inicio = time.time()

    for execucao in range (quantidade_execucoes):
        g_best_fitness= math.inf          
        g_best_posicao=[]
        populacao = []

        #Inicialização da população (enxame)
        for i in range(tamanho_populacao):
            particula = Particula(dimensoes, espaco_busca)
            populacao.append(particula)
    
        #Otimização das partículas
        for i in range(interacoes):

            for j in range(tamanho_populacao):
                populacao[j].calcular_fitness()

                # Saber se a partícula é a melhor global
                if populacao[j].fitness < g_best_fitness:
                    g_best_posicao=list(populacao[j].posicao)
                    g_best_fitness= populacao[j].fitness

            # Atualizar velocidade e posição
            for j in range(tamanho_populacao):
                populacao[j].atualizar_velocidade(g_best_posicao, dimensoes, parametro_constricao, w, c1, c2)
                populacao[j].atualizar_posicao(dimensoes, espaco_busca)
        
        melhores_solucoes_execucao.append(g_best_fitness)
    
    fim = time.time()

    #Cálculo do valor da média dos melhores valores obtidos nas execuções
    soma = 0
    for i in range(quantidade_execucoes):
        soma = soma + melhores_solucoes_execucao[i]
    media = soma/quantidade_execucoes

    #Cálculo do desvio padrão
    num = 0
    for i in range(quantidade_execucoes):
        num = (melhores_solucoes_execucao[i]-media)**2
    desvio_padrao = math.sqrt(num/quantidade_execucoes)

    #Mostrar resultados
    print ("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
    print ("Melhores solucoes: " + str(melhores_solucoes_execucao) + "\n")
    print ("Média: " + str(media) + "\n")
    print ("Desvio padrão: " + str(desvio_padrao) + "\n")
    print ("Tempo de execução: " + str(fim - inicio) + "\n")
    print ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

if __name__ == "__main__":
    main()
