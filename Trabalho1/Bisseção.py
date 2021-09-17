''' Grupo30:
Felipe Andrade Garcia Tommaselli- 11800910
Gianluca Capezzuto Sardinha- 11876933
Pedro Cavalini- 11801007
'''

def main():
    arquivo = open("bisseção_saida.txt", "w")
    arquivo.write("Método da Bisseção:\n")

    #maxiter = input("Insira um valor para o MAXITER que você deseja:\n")

    lista_k = list()
    lista_a = list()
    lista_b = list()
    lista_xk = list()
    lista_fxk = list()
    lista_erro = list()

    # * INTERVALO [-1,0]

    a = -1.
    b = 0.
    xk = a
    xr = 0.  # xr, sendo r = k - 1
    raiz = -pow(3, 0.5) / 3.
    maxiter = 100
    precisao = 0.000001

    lista_k.append(1)
    lista_a.append(a)
    lista_b.append(b)
    lista_xk.append(xk)
    lista_fxk.append(funcao(xk))
    lista_erro.append(abs(xk - raiz))

    mensagem, xk, lista_k, lista_a, lista_b, lista_xk, lista_fxk, lista_erro = metodo_bissecao(a, b, xk, xr, lista_k,
                                                                                               lista_a,
                                                                                               lista_b, lista_xk,
                                                                                               lista_fxk,
                                                                                               lista_erro, raiz,
                                                                                               maxiter, precisao)

    if mensagem == "success":
        formatar_arquivo(arquivo, lista_k, lista_a, lista_b, lista_xk, lista_fxk, lista_erro, "[-1,0]")

    # * INTERVALO [0,1]

    del lista_k[:]
    del lista_a[:]
    del lista_b[:]
    del lista_xk[:]
    del lista_fxk[:]
    del lista_erro[:]

    a = 0.
    b = 1.
    xk = a
    xr = 1.  # xr, sendo r = k - 1
    raiz = pow(3, 0.5) / 3.

    lista_k.append(1)
    lista_a.append(a)
    lista_b.append(b)
    lista_xk.append(xk)
    lista_fxk.append(funcao(xk))
    lista_erro.append(abs(xk - raiz))

    mensagem, xk, lista_k, lista_a, lista_b, lista_xk, lista_fxk, lista_erro = metodo_bissecao(a, b, xk, xr, lista_k,
                                                                                               lista_a,
                                                                                               lista_b, lista_xk,
                                                                                               lista_fxk,
                                                                                               lista_erro, raiz,
                                                                                               maxiter, precisao)

    if mensagem == "success":
        formatar_arquivo(arquivo, lista_k, lista_a, lista_b, lista_xk, lista_fxk, lista_erro, "[0,1]")

    arquivo.close()



def funcao(x):  # define a função que queremos aplicar o método de Newton, tendo como entrada x
    fx = 3 * pow(x, 5) - 9 * pow(x, 4) + 2 * pow(x, 3) - 6 * pow(x, 2) - x + 3
    return fx  # retorna o resultado da função



def metodo_bissecao(a, b, xk, xr, lista_k, lista_a, lista_b, lista_xk, lista_fxk, lista_erro, raiz, maxiter, precisao):

    k = 1
    while abs(xk - xr) > precisao and funcao(xk) != 0 and k <= int(maxiter):
        xr = xk
        xk = float((a+b)/2)
        fxk = funcao(xk)

        if funcao(a)*fxk < 0:
            b = xk

        if fxk*funcao(b) < 0:
            a = xk

        k += 1

        lista_k.append(k)
        lista_a.append(a)
        lista_b.append(b)
        lista_xk.append(xk)
        lista_fxk.append(fxk)
        lista_erro.append(abs(xk - raiz))

    if k > int(maxiter) and abs(xk - xr) > precisao and funcao(xk) != 0:
        return "error", xk, lista_k, lista_a, lista_b, lista_xk, lista_fxk, lista_erro
    else:
        return "success", xk, lista_k, lista_a, lista_b, lista_xk, lista_fxk, lista_erro



def formatar_arquivo(arquivo, lista_k, lista_a, lista_b, lista_xk, lista_fxk, lista_erro, intervalo):
    arquivo.write(f"\nNo intervalo {intervalo}\n")
    arquivo.write("\tk\t    a\t\t\t\t   b\t\t\t\t   xk\t\t\t\t   f(xk)\t\t\t\t   erro\n")

    for k in lista_k:
        a = lista_a[k-1]
        b = lista_b[k-1]
        xk = lista_xk[k-1]
        fxk = lista_fxk[k-1]
        erro = lista_erro[k-1]

        arquivo.write("\t" + str(k) + "\t")
        arquivo.write(str(a) + "\t")
        arquivo.write(str(b) + "\t")
        arquivo.write(str(xk) + "\t")
        arquivo.write(str(fxk) + "\t")
        arquivo.write(str(erro) + "\n")



if __name__ == "__main__": # definição da função main
    main()