''' TRABALHO #1 
Grupo30:
Felipe Andrade Garcia Tommaselli- 11800910
Gianluca Capezzuto Sardinha- 11876933
Pedro Cavalini- 11801007
'''

def main():
    
    # Abre o arquivo texto no modo escrita e adiciona o cabeçalho
    arquivo = open("bisseção_saida.txt", "w")
    arquivo.write("Método da Bisseção:\n")

    # recebe do usuário o maxiter
    maxiter = input("Insira um valor para o MAXITER que você deseja:\n")

    # cria uma serie de listas para armazenar os valores para as iteracoes que virão
    lista_k = list()
    lista_a = list()
    lista_b = list()
    lista_xk = list()
    lista_fxk = list()
    lista_erro = list()

    # * INTERVALO [-1,0]

    # declaração das variáveis  
    a = -1.     # limite inferior do intervalo
    b = 0.      # limite superior do intervalo
    xk = a
    xr = 0.  # xr, sendo r = k - 1
    raiz = -pow(3, 0.5) / 3.    # raiz calculada no wolfram
    precisao = 0.000001     # Para ter um erro < 10^-6

    # adiciona na lista os valores pré registrados acima na primeira posicao das listas
    lista_k.append(0)   # Começa sempre em k=0
    lista_a.append(a)
    lista_b.append(b)
    lista_xk.append(xk)
    lista_fxk.append(funcao(xk))
    lista_erro.append(abs(xk - raiz))

    # chama a funcao do metodo da bissecao
    mensagem, xk, lista_k, lista_a, lista_b, lista_xk, lista_fxk, lista_erro = metodo_bissecao(a, b, xk, xr, lista_k,
                                                                                               lista_a,
                                                                                               lista_b, lista_xk,
                                                                                               lista_fxk,
                                                                                               lista_erro, raiz,
                                                                                               maxiter, precisao)

    # testa se foi retornado sucesso ao achar a raiz
    if mensagem == "success":
        formatar_arquivo(arquivo, lista_k, lista_a, lista_b, lista_xk, lista_fxk, lista_erro, "[-1,0]")

    # * INTERVALO [0,1]

    # deleta o conteúdo de todas as listas
    del lista_k[:]
    del lista_a[:]
    del lista_b[:]
    del lista_xk[:]
    del lista_fxk[:]
    del lista_erro[:]

    # declaração das variáveis  
    a = 0.  # limite inferior do intervalo
    b = 1.  # limite superior do intervalo
    xk = a
    xr = 1.  # xr, sendo r = k - 1
    raiz = pow(3, 0.5) / 3. # raiz calculada no wolfram

    # adiciona na lista os valores pré registrados acima na primeira posicao das listas
    lista_k.append(0)
    lista_a.append(a)
    lista_b.append(b)
    lista_xk.append(xk)
    lista_fxk.append(funcao(xk))
    lista_erro.append(abs(xk - raiz))

    # chama a funcao do metodo da bissecao
    mensagem, xk, lista_k, lista_a, lista_b, lista_xk, lista_fxk, lista_erro = metodo_bissecao(a, b, xk, xr, lista_k,
                                                                                               lista_a,
                                                                                               lista_b, lista_xk,
                                                                                               lista_fxk,
                                                                                               lista_erro, raiz,
                                                                                               maxiter, precisao)

    # testa se foi retornado sucesso ao achar a raiz
    if mensagem == "success":
        formatar_arquivo(arquivo, lista_k, lista_a, lista_b, lista_xk, lista_fxk, lista_erro, "[0,1]")

    # fecha o arquivo texto
    arquivo.close()


# define a função que queremos aplicar o método de Newton, tendo como entrada x
def funcao(x):
    fx = 3 * pow(x, 5) - 9 * pow(x, 4) + 2 * pow(x, 3) - 6 * pow(x, 2) - x + 3
    return fx  # retorna o resultado da função


# aplica o método da bisseção
def metodo_bissecao(a, b, xk, xr, lista_k, lista_a, lista_b, lista_xk, lista_fxk, lista_erro, raiz, maxiter, precisao):

    k = 0

    # condições de parada: atinge a precisão desejada, xk já é raiz ou excede o máximo de iterações
    while abs(xk - xr) > precisao and funcao(xk) != 0 and k <= int(maxiter):
        # xr == x(k - 1), guarda o atual valor de xk na variável "atrasada" xr
        xr = xk
        # atualiza o valor de xk a partir do valor intermediatio no intervalo
        xk = float((a+b)/2)
        fxk = funcao(xk)

        # condição para achar o ponto de valor negativo para iniciar o método da bisseção
        # teste com a
        if funcao(a)*fxk < 0:
            b = xk

        # teste com b
        if fxk*funcao(b) < 0:
            a = xk
        # atualiza o k
        k += 1

        # adiciona os valores atualizados em uma nova iteracao nas tabelas
        lista_k.append(k)
        lista_a.append(a)
        lista_b.append(b)
        lista_xk.append(xk)
        lista_fxk.append(fxk)
        lista_erro.append(abs(xk - raiz))

    # checa se foi possivel chegar na raiz
    if k > int(maxiter) and abs(xk - xr) > precisao and funcao(xk) != 0:
        return "error", xk, lista_k, lista_a, lista_b, lista_xk, lista_fxk, lista_erro
    else:
        return "success", xk, lista_k, lista_a, lista_b, lista_xk, lista_fxk, lista_erro

# define a funcao que formatará o arquivo de texto a partir dos valores obtidos
def formatar_arquivo(arquivo, lista_k, lista_a, lista_b, lista_xk, lista_fxk, lista_erro, intervalo):
    
    # escreve o cabeçalho e as colunas 
    arquivo.write(f"\nNo intervalo {intervalo}\n")
    arquivo.write("\tk\t    a\t\t   b\t\t   xk\t\t   f(xk)\t   erro\n")

    # faz um looping para cada iteracao necessária para achar a raiz
    for k in lista_k:
        
        # formata os valores com as casas decimais escolhidas
        a = format(lista_a[k], '.8f')
        b = format(lista_b[k], '.8f')
        xk = format(lista_xk[k], '.8f')
        fxk = format(lista_fxk[k], '.8f')
        erro = format(lista_erro[k], '.8f')

        # escreves os valores no arquivo texto com a formatação querida
        arquivo.write("\t" + str(k) + "\t")
        arquivo.write(str(a) + "\t")
        arquivo.write(str(b) + "\t")
        arquivo.write(str(xk) + "\t")
        arquivo.write(str(fxk) + "\t")
        arquivo.write(str(erro) + "\n")



if __name__ == "__main__": # chama a função main
    main()