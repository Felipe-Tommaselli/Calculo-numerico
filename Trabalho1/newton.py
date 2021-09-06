''' Grupo30:
Felipe Andrade Garcia Tommaselli- 11800910
Gianluca Capezzuto Sardinha- 11876933 
Pedro Cavalini- 11801007
'''

import matplotlib.pyplot as plt

def main(): 
    arquivo = open("secantes_saida.txt", "w")
    arquivo.write("Método das Secantes:\n")

    k = 0
    xk = -1.0000000000000000
    xr = 0
    mod = abs(xk - xr)
    erro = 1./7.

    arquivo.write("No intervalo [-1, 0]\n")
    arquivo.write("\tk\t     xk\t\t   f(xk)\t   f'(xk)\t   erro\n")

    while(mod > 0.000001 and k <= 50):
        fx = funcao(xk)
        dx = derivada(xk)

        arquivo.write("\t" + str(k) + "\t")
        arquivo.write(str(xk) + "\t")
        arquivo.write(str(fx) + "\t")
        arquivo.write(str(dx) + "\t")
        arquivo.write(str(abs(xk - erro)) + "\n")

        xr = xk 
        xk = xk - (fx / dx)
        k += 1
        mod = abs(xk - xr)
    
    arquivo.write("\t" + str(k) + "\t")
    arquivo.write(str(xk) + "\t")
    arquivo.write(str(fx) + "\t")
    arquivo.write(str(dx) + "\t")
    arquivo.write(str(abs(xk - erro)) + "\n")

    arquivo.close()

def funcao(x): 
    fx = 3*(x**5) - 9*(x**4) + 2*(x**3) - 6*(x**2) - (x) + 3
    return fx

def derivada(x): 
    dx = 15*(x**4) - 36*(x**3) + 6*(x**2) - 12*(x) -1 
    return dx


if __name__ == "__main__":
    main()