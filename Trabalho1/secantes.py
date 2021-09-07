''' Grupo30:
Felipe Andrade Garcia Tommaselli- 11800910
Gianluca Capezzuto Sardinha- 11876933 
Pedro Cavalini- 11801007
'''

def main(): 
    arquivo = open("secantes_saida.txt", "w")
    arquivo.write("Método das Secantes:\n")
    
    maxiter = input("Insira um valor para o MAXITER que você deseja:\n")

    k = 0 # começando com k igual a 0 e incrementando a cada iteração
    xk = -1 # tendo o primeiro intervalo de [-1, 0] e estabelecendo xk = -1 e xr = 0
    xr = 0 # xr, sendo r = k - 1 
    xrr = None # xrr, sendo rr = r - 1 = k - 2
    mod = abs(xk - xr)
    raiz = -pow(3, 0.5)/3.

    arquivo.write("No intervalo [-1, 0]\n")
    arquivo.write("\tk\t     xk\t\t   f(xk)\t   erro\n")

    # enquanto não for alcançada a precisão desejada e 
    # k for menor que a maxiter o loop acontece
    while(mod > 0.000001 and k <= int(maxiter)):
        
        print(k)
        fxk = funcao(xk)
        fxr = funcao(xr)

        arquivo.write("\t" + str(k) + "\t")
        arquivo.write(str(xk) + "\t")
        arquivo.write(str(fxk) + "\t")
        arquivo.write(str(abs(xk - raiz)) + "\n")

        # xrr == x (k - 2)
        xrr = xr 
        # xr == x (k-1)
        xr = xk 
        
        # atualiza xk com base no xr e xrr
        xk = (funcao(xr)*xrr - funcao(xrr)*xr)/(funcao(xr) - funcao(xrr))
        mod = abs(xk - xr)
    
        k += 1

    arquivo.write("\t" + str(k) + "\t")
    arquivo.write(str(xk) + "\t")
    arquivo.write(str(fxk) + "\t")
    arquivo.write(str(abs(xk - raiz)) + "\n")

    arquivo.close()

def funcao(x): # define a função que queremos aplicar o método de Newton, tendo como entrada x
    fx = 3*pow(x, 5) - 9*pow(x, 4) + 2*pow(x, 3) - 6*pow(x, 2) - x + 3
    return fx # retorna o resultado da função 


if __name__ == "__main__": # definição da função main
    main()
