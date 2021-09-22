''' Grupo30:
Felipe Andrade Garcia Tommaselli- 11800910
Gianluca Capezzuto Sardinha- 11876933 
Pedro Cavalini- 11801007
'''

def main(): 
    arquivo = open("newton_saida.txt", "w")
    arquivo.write("Método de Newton:\n")

    maxiter = input("Insira um valor para o MAXITER que você deseja:\n")

    listak = list()
    listaxk = list()
    listafxk = list()
    listadxk = list()
    listaerro = list()

    #* INTERVALO [-1, 0]

    k = 0 # começando com k igual a 0 e incrementando a cada iteração
    xk = -1. # tendo o primeiro intervalo de [-1, 0] e estabelecendo xk = -1 e xr = 0
    xr = 0. # xr, sendo r = k - 1 
    raiz = -pow(3, 0.5)/3.

    listak.append(k)
    listaxk.append(xk)
    listafxk.append(funcao(xk))
    listadxk.append(derivada(xk))
    listaerro.append(abs(xk - raiz))

    # enquanto não for alcançada a precisão desejada e
    # k for menor que a maxiter o loop acontece
    while(abs(xk - xr) > 0.000001 and k <= int(maxiter)): 
        k, xk, xr, listak, listaxk, listafxk, listadxk, listaerro= metNewton(k, xk, xr, listak, listaxk, listafxk, listadxk, listaerro, raiz)                          

    formatar_arquivo(arquivo, listak, listaxk, listafxk, listadxk, listaerro, "[-1,0]")

    #* INTERVALO [0, 1]

    del listak[:]
    del listaxk[:]
    del listafxk[:]
    del listadxk[:]
    del listaerro[:]

    k = 0 # começando com k igual a 0 e incrementando a cada iteração
    xk = 1. # tendo o primeiro intervalo de [-1, 0] e estabelecendo xk = -1 e xr = 0
    xr = 0. # xr, sendo r = k - 1 
    raiz = pow(3, 0.5)/3.

    listak.append(k)
    listaxk.append(xk)
    listafxk.append(funcao(xk))
    listadxk.append(derivada(xk))
    listaerro.append(abs(xk - raiz))

    # enquanto não for alcançada a precisão desejada e 
    # k for menor que a maxiter o loop acontece
    while(abs(xk - xr) > 0.000001 and k <= int(maxiter)): 
        k, xk, xr, listak, listaxk, listafxk, listadxk, listaerro= metNewton(k, xk, xr, listak, listaxk, listafxk, listadxk, listaerro, raiz)                          

    formatar_arquivo(arquivo, listak, listaxk, listafxk, listadxk, listaerro, "[-1,0]")

    arquivo.close()

def funcao(x): # define a função que queremos aplicar o método de Newton, tendo como entrada x
    fx = 3*pow(x, 5) - 9*pow(x, 4) + 2*pow(x, 3) - 6*pow(x, 2) - x + 3
    return fx # retorna o resultado da função 

def derivada(x): # define a derivada da função que queremos aplicar o método de Newton, tendo como entrada x 
    dx = 15*pow(x, 4) - 36*pow(x, 3) + 6*pow(x, 2) - 12*x -1 
    return dx # retorna o resultado da derivada da função 

def metNewton(k, xk, xr, listak, listaxk, listafxk, listadxk, listaerro, raiz):

    fx = funcao(xk) # fx atribui o valor da função especificada no método no ponto xk
    dx = derivada(xk) # dx atribui o valor da função especificada no método no ponto xk
    
    xr = xk # xr = x(k-1)
    xk = xr - (fx/dx) # aplicação do método de newton, ou seja, essa é basicamente a função psi

    k += 1 # adiciona 1 a k a cada iteração

    listak.append(k)
    listaxk.append(xk)
    listafxk.append(funcao(xk))
    listadxk.append(derivada(xk))
    listaerro.append(abs(xk - raiz))

    return k, xk, xr, listak, listaxk, listafxk, listadxk, listaerro

def formatar_arquivo(arquivo, listak, listaxk, listafxk, listadxk, listaerro, intervalo):

    arquivo.write(f"\nNo intervalo {intervalo}\n")
    arquivo.write("\tk\t     xk\t\t\t\t   f(xk)\t\t\t\t   erro\n")

    for k in listak:
        xk = listaxk[k]
        fxk = listafxk[k]
        dxk = listadxk[k]
        erro = listaerro[k]
                
        if xk == 0.0 and fxk == 3.0 or xk == -1.0 and fxk == -16.0:
            arquivo.write("\t" + str(k) + "\t")
            arquivo.write(str(xk) + "000000000000000" + "\t")
            arquivo.write(str(fxk) + "000000000000000" + "\t")
            arquivo.write(str(dxk) + "\t")
            arquivo.write(str(erro) + "\n")
        else:
            arquivo.write("\t" + str(k) + "\t")
            arquivo.write(str(xk) + "\t")
            arquivo.write(str(fxk) + "\t")
            arquivo.write(str(dxk) + "\t")
            arquivo.write(str(erro) + "\n")

if __name__ == "__main__": # definição da função main
    main()