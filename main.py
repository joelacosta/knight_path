import matplotlib.pyplot as plt
import numpy as np

def accesibles(celda, disponibles):
    i,j = celda
    lista = [(i+2,j+1),(i+2,j-1),(i-2,j+1),(i-2,j-1),(i+1,j+2),(i+1,j-2),(i-1,j+2),(i-1,j-2)]
    lista = [v for v in lista if v in disponibles]
    return lista

def siguiente(candidatos, disponibles):
    conectividad = [len(accesibles(c,disponibles)) for c in candidatos]
    ordenados = [c for _,c in sorted(zip(conectividad,candidatos))]
    return ordenados[0]

def construir_secuencia(shape: tuple = (8,8), inicial: tuple =(0,0), graficar = False):
    N = shape[1]*shape[0]
    disponibles = [(i,j) for i in range(shape[0]) for j in range(shape[1])]
    actual = inicial
    secuencia = [actual]
    disponibles.remove(actual)
    for n in range(N):
        candidatos = accesibles(actual,disponibles)
        if len(candidatos) == 0:
            print(f'Se llegó al final de la secuencia. Se completaron {n+1}/{N} casilleros')
            break
        actual = siguiente(candidatos, disponibles)
        secuencia.append(actual)
        disponibles.remove(actual)
    if graficar:
        plt.figure()
        tablero = np.zeros(shape) 
        plt.imshow(tablero,cmap = 'cool')
        [plt.hlines(i+0.5,-0.5,shape[1] - 0.5) for i in range(shape[0])]
        [plt.vlines(i+0.5,-0.5,shape[0] - 0.5) for i in range(shape[1])]
        [plt.text(j[1], j[0],i+1,ha='center',va='center') for i,j in enumerate(secuencia)]
        plt.xlim([-0.5,shape[0] - 0.5])
        plt.xlim([-0.5,shape[1] - 0.5])
        plt.savefig('tablero')
        plt.close()
    return secuencia

if __name__ == '__main__':
    construir_secuencia(graficar=True)

