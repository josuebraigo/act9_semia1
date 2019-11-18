import de_simple
import cost_functions as fx
import matplotlib.pyplot as plt
import numpy as np

bounds = [(-1,1),(-1,1)]              
popsize = [4, 4, 8, 16]      #Dimensiones       
mutate = 0.2                #mutacion       
recombination = 0.7                 
maxiter = 2000  #Generaciones


x = np.linspace(0, 21, 21)

"""de_simple.minimize(fx.sphere, bounds, 4, mutate, recombination, maxiter)
promedioEjecucion = np.array(de_simple.promedios)

print(promedioEjecucion)
plt.plot(x, promedioEjecucion)
plt.show()

"""

def run(funcion):
    
    promediosFinales = []

    for dimension in popsize:
        
        promediosEjecucion1 = de_simple.minimize(funcion, bounds, dimension, mutate, recombination, maxiter)
    
        promediosEjecucion2 = de_simple.minimize(funcion, bounds, dimension, mutate, recombination, maxiter)
        
        promediosEjecucion3 = de_simple.minimize(funcion, bounds, dimension, mutate, recombination, maxiter)
        
        promediosEjecucion4 = de_simple.minimize(funcion, bounds, dimension, mutate, recombination, maxiter)
    
        promediosEjecucion5 = de_simple.minimize(funcion, bounds, dimension, mutate, recombination, maxiter)
        
        suma = 0
        cont = 0
        promedio = 0
        promedios = []
        
        for i in promediosEjecucion1:
            suma = promediosEjecucion1[cont] + promediosEjecucion2[cont] + promediosEjecucion3[cont] + promediosEjecucion4[cont] + promediosEjecucion5[cont]
            cont += 1
            promedio = (suma / 5)
            promedios.append(promedio)
            
        promediosFinales.append(promedios)
        plt.plot(x, promedios)
        plt.show()
        
        
    for i in range(len(promediosFinales)):
        plt.plot(x, promediosFinales[i])
        
    plt.show()
        
run(fx.sphere)
run(fx.rosenbroc)
run(fx.rastring)
run(fx.quartic)
    

##print("Rosenbroc")
##de_simple.minimize(fx.rosenbroc, bounds, popsize, mutate, recombination, maxiter)

##print("Rastring")
##de_simple.minimize(fx.rastring, bounds, popsize, mutate, recombination, maxiter)

##print("Quartic")
##de_simple.minimize(fx.quartic, bounds, popsize, mutate, recombination, maxiter)


