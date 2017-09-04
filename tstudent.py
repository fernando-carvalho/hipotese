from numpy import std
from numpy import mean
from scipy import stats

# Teste de hipotese explicado no video em https://www.youtube.com/watch?v=nHDZJMG3Jn8
vetor1 = [6,33,21,26,10,29,33,29,37,15,2,21,7,26,13]
vetor2 = [10,8,17,4,17,14,9,4,21,3,7,10,29,13,14,2]

# Hipotese nula Ho = os valores do vetor 1 eh igual aos valores no vetor 2
# Hipotese alternativa (aquilo que queremos provar) H1 = os valores sao diferente
# O erro mais grave (erro tipo 1) eh rejeitar a hipotese nula quando ela eh verdadeira
# O valor do p-valor mede a probabilidade de rejeitar Ho quando Ho eh verdadeiro

media1 = mean(vetor1)
# ddof =1 faz com que o calcula seja do desvio padrao amostral (n-ddof) (Delta Degrees of Freedom)
dp1 = std(vetor1, ddof=1)

media2 = mean(vetor2)
dp2 = std(vetor2, ddof=1)

print "Vetor 1:", media1, dp1
print "Vetor 2:", media2, dp2

# Faz o teste de hipotese para testar as duas populacoes
# http://www.scipy-lectures.org/packages/statistics/index.html#student-s-t-test-the-simplest-statistical-test
print stats.ttest_ind(vetor1, vetor2)


# Teste para verificar se eh possivel que a amostra em vetor1
# saiu de uma populacao cuja media eh x

# Hipotese nula: vetor1 saiu de uma populacao com media x
# Hipotese alternativa: vetor1 eh diferente da populacao com media x
# Se o valor-p eh menor que 0.05, rejeita a hipotese nula e conclui
# que a probabilidade de vetor ter saido de tal populacao eh muito baixa
x = 12
print stats.ttest_1samp(vetor1, x)
