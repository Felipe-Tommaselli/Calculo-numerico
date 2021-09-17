''' Grupo30:
Felipe Andrade Garcia Tommaselli- 11800910
Gianluca Capezzuto Sardinha- 11876933 
Pedro Cavalini- 11801007
'''

def main(): 
    arquivo = open("newton_saida.txt", "w")
    arquivo.write("Método de Newton:\n")

    maxiter = input("Insira um valor para o MAXITER que você deseja:\n")

    #* INTERVALO [-1, 0]

    k = 0 # começando com k igual a 0 e incrementando a cada iteração
    xk = -1. # tendo o primeiro intervalo de [-1, 0] e estabelecendo xk = -1 e xr = 0
    xr = 0. # xr, sendo r = k - 1 
    raiz = -pow(3, 0.5)/3.

    # cabeçalho do arquivo texto
    arquivo.write("No intervalo [-1, 0]\n")
    arquivo.write("\tk\t\t     xk\t\t\t\t   f(xk)\t\t\t\t   f'(xk)\t\t\t\t   erro\n")

    # enquanto não for alcançada a precisão desejada e
    # k for menor que a maxiter o loop acontece
    while(abs(xk - xr) > 0.000001 and k <= int(maxiter)): 
        k, xk, xr, arquivo = metNewton(k, xk, xr, arquivo, raiz)                          

    arquivo.write("\t" + str(k) + "\t")
    arquivo.write(str(xk) + "\t")
    arquivo.write(str(funcao(xk)) + "\t")
    arquivo.write(str(derivada(xk)) + "\t")
    arquivo.write(str(abs(float(xk) - raiz)) + "\n")

    #* INTERVALO [0, 1]

    k = 0 # começando com k igual a 0 e incrementando a cada iteração
    xk = 1. # tendo o primeiro intervalo de [-1, 0] e estabelecendo xk = -1 e xr = 0
    xr = 0. # xr, sendo r = k - 1 
    raiz = pow(3, 0.5)/3.

    arquivo.write("\n\nNo intervalo [0,1]\n")
    arquivo.write("\tk\t\t     xk\t\t\t\t   f(xk)\t\t\t\t   f'(xk)\t\t\t\t   erro\n")

    # enquanto não for alcançada a precisão desejada e 
    # k for menor que a maxiter o loop acontece
    while(abs(xk - xr) > 0.000001 and k <= int(maxiter)): 
        k, xk, xr, arquivo = metNewton(k, xk, xr, arquivo, raiz)                          

    arquivo.write("\t" + str(k) + "\t")
    arquivo.write(str(xk) + "\t")
    arquivo.write(str(funcao(xk)) + "\t")
    arquivo.write(str(derivada(xk)) + "\t")
    arquivo.write(str(abs(float(xk) - raiz)) + "\n")

    arquivo.close()

def funcao(x): # define a função que queremos aplicar o método de Newton, tendo como entrada x
    fx = 3*pow(x, 5) - 9*pow(x, 4) + 2*pow(x, 3) - 6*pow(x, 2) - x + 3
    return fx # retorna o resultado da função 

def derivada(x): # define a derivada da função que queremos aplicar o método de Newton, tendo como entrada x 
    dx = 15*pow(x, 4) - 36*pow(x, 3) + 6*pow(x, 2) - 12*x -1 
    return dx # retorna o resultado da derivada da função 

def metNewton(k, xk, xr, arquivo, raiz):
    fx = funcao(xk)
    dx = derivada(xk)

    if xr == 0.0 and funcao(xr) == 3.0 or xk == -1.0 and fx == -16.0:
        arquivo.write("\t" + str(k) + "\t")
        arquivo.write(str(xk) + "000000000000000" + "\t")
        arquivo.write(str(fx) + "000000000000000" + "\t")
        arquivo.write(str(dx) + "000000000000000" + "\t")
        arquivo.write(str(abs(float(xk) - raiz)) + "\n")
    else:
        arquivo.write("\t" + str(k) + "\t")
        arquivo.write(str(xk) + "\t")
        arquivo.write(str(fx) + "\t")
        arquivo.write(str(dx) + "\t")
        arquivo.write(str(abs(float(xk) - raiz)) + "\n")
    
    xr = xk # xr = x(k-1)
    xk = xr - (fx/dx)

    k += 1

    return k, xk, xr, arquivo

if __name__ == "__main__": # definição da função main
    main()