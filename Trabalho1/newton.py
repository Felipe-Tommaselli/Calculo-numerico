''' Grupo30:
Felipe Andrade Garcia Tommaselli- 11800910
Gianluca Capezzuto Sardinha- 11876933 
Pedro Cavalini- 11801007
'''

def main(): 

    # abre o arquivo texto no modo escrita e adiciona o cabeçalho
    arquivo = open("newton_saida.txt", "w")
    arquivo.write("Método de Newton:\n")

    # recebe do usuário o maxiter
    maxiter = input("Insira um valor para o MAXITER que você deseja:\n")

    # cria uma série de listas para armazenar os valores para as iterações que virão a acontecer
    listak = list()
    listaxk = list()
    listafxk = list()
    listadxk = list()
    listaerro = list()

    #* INTERVALO [-1, 0]

    # declaração das variáveis
    k = 0 # começando com k igual a 0 e incrementando a cada iteração
    xk = -1. # tendo o primeiro intervalo de [-1, 0] e estabelecendo xk = -1 e xr = 0
    xr = 0. # xr, sendo r = k - 1 
    raiz = -pow(3, 0.5)/3. # raiz calculada no wolfram

    # adiciona na lista os valores pré registrados acima na primeira posicao das listas
    listak.append(k)
    listaxk.append(xk)
    listafxk.append(funcao(xk))
    listadxk.append(derivada(xk))
    listaerro.append(abs(xk - raiz))

    # enquanto não for alcançada a precisão desejada e
    # k for menor que a maxiter o loop acontece
    while(abs(xk - xr) > 0.000001 and k <= int(maxiter)): 
        # chama a função do método de Newton
        k, xk, xr, listak, listaxk, listafxk, listadxk, listaerro= metNewton(k, xk, xr, listak, listaxk, listafxk, listadxk, listaerro, raiz)                          

    # formata o arquivo a partir dos valores armazenados nas listas
    formatar_arquivo(arquivo, listak, listaxk, listafxk, listadxk, listaerro, "[-1,0]")

    #* INTERVALO [0, 1]

    # libera o espaço das listas para o outro intervalo
    del listak[:]
    del listaxk[:]
    del listafxk[:]
    del listadxk[:]
    del listaerro[:]

    # declaração das variáveis
    k = 0 # começando com k igual a 0 e incrementando a cada iteração
    xk = 1. # tendo o primeiro intervalo de [-1, 0] e estabelecendo xk = -1 e xr = 0
    xr = 0. # xr, sendo r = k - 1 
    raiz = pow(3, 0.5)/3. # raiz calculada no wolfram

    # adiciona na lista os valores pré registrados acima na primeira posicao das listas
    listak.append(k)
    listaxk.append(xk)
    listafxk.append(funcao(xk))
    listadxk.append(derivada(xk))
    listaerro.append(abs(xk - raiz))

    # enquanto não for alcançada a precisão desejada e 
    # k for menor que a maxiter o loop acontece
    while(abs(xk - xr) > 0.000001 and k <= int(maxiter)): 
        # chama a funcao do método de Newton
        k, xk, xr, listak, listaxk, listafxk, listadxk, listaerro= metNewton(k, xk, xr, listak, listaxk, listafxk, listadxk, listaerro, raiz)                          

    # formata o arquivo de texto
    formatar_arquivo(arquivo, listak, listaxk, listafxk, listadxk, listaerro, "[0,1]")

    # fecha o arquivo de texto
    arquivo.close()

# define a função que queremos aplicar o método de Newton, tendo como entrada x
def funcao(x): 
    # função dada no enunciado
    fx = 3*pow(x, 5) - 9*pow(x, 4) + 2*pow(x, 3) - 6*pow(x, 2) - x + 3
    return fx # retorna o resultado da função 

# define a derivada da função que queremos aplicar o método de Newton, tendo como entrada x 
def derivada(x): 
    dx = 15*pow(x, 4) - 36*pow(x, 3) + 6*pow(x, 2) - 12*x -1 
    return dx # retorna o resultado da derivada da função 

# define o método de Newton visto em aula que será aplicado conforme roda as iteracoes
# no looping que chama a funcao, os valores são armazenados nas respectivas listas
def metNewton(k, xk, xr, listak, listaxk, listafxk, listadxk, listaerro, raiz):

    fx = funcao(xk) # fx atribui o valor da função especificada no método no ponto xk
    dx = derivada(xk) # dx atribui o valor da função especificada no método no ponto xk
    
    # atualiza xk com base em xr a partir do método de Newton
    xr = xk # xr = x(k-1)
    xk = xr - (fx/dx) # aplicação do método de newton, ou seja, essa é basicamente a função psi

    k += 1 # adiciona 1 a k a cada iteração

    # adiciona os valores atualizados em uma nova iteração nas tabelas
    listak.append(k)
    listaxk.append(xk)
    listafxk.append(funcao(xk))
    listadxk.append(derivada(xk))
    listaerro.append(abs(xk - raiz))

    # retorna todos os valores atualizados
    return k, xk, xr, listak, listaxk, listafxk, listadxk, listaerro

# define a funcao que formatará o arquivo de texto a partir dos valores obtidos
def formatar_arquivo(arquivo, listak, listaxk, listafxk, listadxk, listaerro, intervalo):

    # escreve o cabeçalho e as colunas
    arquivo.write(f"\nNo intervalo {intervalo}\n")
    arquivo.write("\tk\t     xk\t\t   f(xk)\t f'(xk)\t\t   erro\n")

    # faz um looping para cada iteracao necessária para achar a raiz
    for k in listak:

        # formata os valores com as casas decimais escolhidas
        xk = format(listaxk[k], '.8f')
        fxk = format(listafxk[k], '8f')
        dxk = format(listadxk[k], '.8f')
        erro = format(listaerro[k], '.8f')
                
        # escreves os valores no arquivo texto com a formatação querida    
        arquivo.write("\t" + str(k) + "\t")
        arquivo.write(str(xk) + "\t")
        arquivo.write(str(fxk) + "\t")
        arquivo.write(str(dxk) + "\t")
        arquivo.write(str(erro) + "\n")

if __name__ == "__main__": # definição da função main
    main()