import matplotlib as mpl
import matplotlib.pyplot as plt
import random as rd
import numpy as np
import time

l = []

def minval(l):
    
    mini = l[0]
    
    for i in range(1, len(l)):
        
        if ( l[i] <= mini ):
            
            mini = l[i]
    
    return mini
debut = time.time()
n = 0

Tailles = []

Temps = []

while n < 5:
    
    li = [rd.randint(0, 15) for j in range(rd.randint(1, 10))]

    Tailles.append(len(li))
    
    if __name__ == "__main__":
    
        print ( 'Le plus petit élément de la liste {0} est: {1}'.format(li,  minval(li)))
        
    n = n + 1
    
    fin = time.time()
    
    Temps.append(fin - debut)

print('Ensemble des tailles pour les cinqs listes:{0}'.format(Tailles))

print('Ensemble des temps execution pour les cinqs listes:{0}'.format(Temps))

plt.title("Variation de la complexité de  l'algorithme de recherche du minimum", c = 'green')

plt.ylabel("Temps", c = 'r')

plt.xlabel("Tailles", c = 'purple')

plt.scatter(sorted(Tailles), sorted(Temps), c = 'r')

plt.plot(sorted(Tailles), sorted(Temps), linestyle = "solid", c = 'b')
