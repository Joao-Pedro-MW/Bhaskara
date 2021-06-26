from math import sqrt as rq
import time

a = input('Valor de A ')
a = int(float(a))
b = input('Valor de B ')
b = int(float(b))
c = input('Valor de C ')
c = int(float(c))

delta = (b**2 - (4*a*c)) #calcula o valor de delta: Fórmula (b^2 - 4.a.c)
#Concavidades
if a > 0: print("Concavidade para CIMA ") #concavidade do gráfico
else: print("Concavidade para BAIXO ")
#Possibilidades de valor de Delta
if delta < 0:
    print("Delta é negativo logo não tem raiz")
    time.sleep(3)
elif delta > 0:
    x_vertice = ((-(b))/2*a)
    y_vertice = ((-(delta)/4*a))
    delta = rq(delta)
    print("O valor de delta é: ",delta)
    time.sleep(3)
    x1 = (-b + delta)/(2*a)
    x2 = (-b - delta)/(2*a)
    print("O valor de x1 é: {}".format(x1))
    print("O valor de x1 é: {}".format(x2))
    print("O ponto máximo de altura de X é: {:.3f}".format(x_vertice)) #{:.3f} Formata o número float grande
    print("O ponto máximo de altura de Y é: {:.3f}".format(y_vertice)) # para um float de 3 casas decimais
    time.sleep(5)
elif delta == 0:
    print("Delta é igual zero, não existe raiz real para ele")
    
else: print("O valor inserido é inválido")