''' Grupo30:
Felipe Andrade Garcia Tommaselli- 11800910
Gianluca Capezzuto Sardinha- 11876933 
Pedro Cavalini- 11801007
'''

def main(): 
    arquivo = open("newton_saida.txt", "w")
    arquivo.write("Método de Newton:\n")

    maxiter = input("Insira um valor para o MAXITER que você deseja:\n")

    k = 0 # começando com k igual a 0 e incrementando a cada iteração
    xk = -1 # tendo o primeiro intervalo de [-1, 0] e estabelecendo xk = -1 e xr = 0
    xr = 0 # xr, sendo r = k - 1 
    mod = abs(xk - xr)
    raiz = -pow(3, 0.5)/3.

    arquivo.write("No intervalo [-1, 0]\n")
    arquivo.write("\tk\t     xk\t\t   f(xk)\t   f'(xk)\t   erro\n")

    # enquanto não for alcançada a precisão desejada e 
    # k for menor que a maxiter o loop acontece
    while(mod > 0.000001 and k <= int(maxiter)): 
        fx = funcao(xk)
        dx = derivada(xk)

        arquivo.write("\t" + str(k) + "\t")
        arquivo.write(str(xk) + "\t\t")
        arquivo.write(str(fx) + "\t")
        arquivo.write(str(dx) + "\t")
        arquivo.write(str(abs(xk - raiz)) + "\n")

        xr = xk # xr atribui o valor de xk, ou seja, x(k-1) atribui o valor de xk 
        xk = xk - (fx / dx) # xk atribui o próximo valor a ser calculado
        mod = abs(xk - xr) # precisão recalculada

        k += 1 
    
    arquivo.write("\t" + str(k) + "\t")
    arquivo.write(str(xk) + "\t\t")
    arquivo.write(str(fx) + "\t")
    arquivo.write(str(dx) + "\t")
    arquivo.write(str(abs(xk - raiz)) + "\n")

    arquivo.close()

def funcao(x): # define a função que queremos aplicar o método de Newton, tendo como entrada x
    fx = 3*pow(x, 5) - 9*pow(x, 4) + 2*pow(x, 3) - 6*pow(x, 2) - x + 3
    return fx # retorna o resultado da função 

def derivada(x): # define a derivada da função que queremos aplicar o método de Newton, tendo como entrada x 
    dx = 15*pow(x, 4) - 36*pow(x, 3) + 6*pow(x, 2) - 12*x -1 
    return dx # retorna o resultado da derivada da função 

if __name__ == "__main__": # definição da função main
    main()