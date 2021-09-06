''' Grupo30:
Felipe Andrade Garcia Tommaselli- 11800910
Gianluca Capezzuto Sardinha- 11876933 
Pedro Cavalini- 11801007
'''

def main(): 
    arquivo = open("newton_saida.txt", "w")
    arquivo.write("Método de Newton:\n")

    k = 0
    xk = -1.0 
    xr = 0
    xrr = None 
    mod = abs(xk - xr)
    erro = 1./7.

    arquivo.write("No intervalo [-1, 0]\n")
    arquivo.write("\tk\t     xk\t\t   f(xk)\t   erro\n")

    while(mod > 0.000001 and k <= 10):
        
        print(k)
        fxk = funcao(xk)
        fxr = funcao(xr)

        arquivo.write("\t" + str(k) + "\t")
        arquivo.write(str(xk) + "\t")
        arquivo.write(str(fxk) + "\t")
        arquivo.write(str(abs(xk - erro)) + "\n")
        
        xrr = xr # xrr == x sub(k - 2)
        xr = xk # xr == x sub(k-1)
        
        xk = (funcao(xr)*xrr - funcao(xrr)*xr)/funcao(xr) - funcao(xrr)
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

if __name__ == "__main__":
    main()
