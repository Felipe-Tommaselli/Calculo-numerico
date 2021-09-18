''' Grupo30:
Felipe Andrade Garcia Tommaselli- 11800910
Gianluca Capezzuto Sardinha- 11876933 
Pedro Cavalini- 11801007
'''

def main(): 

    # Abre o arquivo texto no modo escrita e adiciona o cabeçalho
    arquivo = open("secantes_saida.txt", "w")
    arquivo.write("Método das Secantes:\n")

    # recebe do usuário o maxiter
    maxiter = input("Insira um valor para o MAXITER que você deseja:\n")

    # cria uma serie de listas para armazenar os valores para as iteracoes que virão
    listak = list()
    listaxk = list()
    listafxk = list()
    listaerro = list()

    #* INTERVALO [-1,0]

    # declaração das variáveis  
    k = 0 # começando com k igual a 0 e incrementando a cada iteração
    xk = -1. # tendo o primeiro intervalo de [-1, 0] e estabelecendo xk = -1 e xr = 0
    xr = 0. # xr, sendo r = k - 1 
    xrr = None # xrr, sendo rr = r - 1 = k - 2
    raiz = -pow(3, 0.5)/3. # raiz calculada no wolfram

    # adiciona na lista os valores pré registrados acima na primeira posicao das listas
    listak.append(k)
    listaxk.append(xk)
    listafxk.append(funcao(xk))
    listaerro.append(abs(xk - raiz))

    # roda em loop ingenquanto não for alcançada a precisão desejada ou
    # o k for menor que a maxiter
    while(abs(xk - xr) > 0.000001 and k <= int(maxiter)):
        # chama a funcao do metodo das secantes
        k, xk, xr, xrr, listak, listaxk, listafxk, listaerro = m_das_secantes(k, xk, xr, xrr, listak, listaxk, listafxk, listaerro, raiz)

    # formatar o arquivo a partir dos valores armazenados nas listas
    formatar_arquivo(arquivo, listak, listaxk, listafxk, listaerro, "[-1,0]")

    #* INTERVALO [0,1]
    
    # libera o espaço das listas
    del listak[:]
    del listaxk[:]
    del listafxk[:]
    del listaerro[:]

    # declaração das variáveis  
    k = 0 # começando com k igual a 0 e incrementando a cada iteração
    xk = 0. # tendo o primeiro intervalo de [-1, 0] e estabelecendo xk = -1 e xr = 0
    xr = 1. # xr, sendo r = k - 1 
    xrr = None # xrr, sendo rr = r - 1 = k - 2
    raiz = pow(3, 0.5)/3.

    # adiciona na lista os valores pré registrados acima na primeira posicao das listas
    listak.append(k)
    listaxk.append(xk)
    listafxk.append(funcao(xk))
    listaerro.append(abs(xk - raiz))

    # roda em loop ingenquanto não for alcançada a precisão desejada ou
    # o k for menor que a maxiter
    while(abs(xk - xr) > 0.000001 and k <= int(maxiter)):
        # chama a funcao do metodo das secantes
        k, xk, xr, xrr, listak, listaxk, listafxk, listaerro = m_das_secantes(k, xk, xr, xrr, listak, listaxk, listafxk, listaerro, raiz)

    # formatar o arquivo a partir dos valores armazenados nas listas
    formatar_arquivo(arquivo, listak, listaxk, listafxk, listaerro, "[0,1]")

    # fecha o arquivo texto
    arquivo.close()

# define a função que queremos aplicar o método de Newton, tendo como entrada x
def funcao(x):
    # função dada no enunciado
    fx = 3*pow(x, 5) - 9*pow(x, 4) + 2*pow(x, 3) - 6*pow(x, 2) - x + 3
    # retorna o resultado da função
    return fx 

# define o método das secantes visto em aula que será aplicado conforme roda as iteracoes
# no looping que chama a funcao, os valores são armazenados nas respectivas listas
def m_das_secantes(k, xk, xr, xrr, listak, listaxk, listafxk, listaerro, raiz):

    # xrr == x(k - 2), guarda o atual valor de xr na variável "atrasada" xrr
    xrr = xr 
    # xr == x(k - 1), guarda o atual valor de xk na variável "atrasada" xr
    xr = xk 
    # atualiza xk com base no xr e xrr a partir do metodo das secantes, a formula é
    # obtida a partir da descritização do método de newton
    xk = (funcao(xr)*xrr - funcao(xrr)*xr)/(funcao(xr) - funcao(xrr))
    # atualiza o k
    k += 1
    
    # adiciona os valores atualizados em uma nova iteracao nas tabelas
    listak.append(k)
    listaxk.append(xk)
    listafxk.append(funcao(xk))
    listaerro.append(abs(xk - raiz))

    # retorna todos os valores atualizados
    return k, xk, xr, xrr, listak, listaxk, listafxk, listaerro

# define a funcao que formatará o arquivo de texto a partir dos valores obtidos
def formatar_arquivo(arquivo, listak, listaxk, listafxk, listaerro, intervalo):

    # escreve o cabeçalho e as colunas 
    arquivo.write(f"\nNo intervalo {intervalo}\n")
    arquivo.write("\tk\t\txk\t\tf(xk)\t\terro\n")

    # faz um looping para cada iteracao necessária para achar a raiz
    for k in listak:
        
        # formata os valores com as casas decimais escolhidas
        xk = format(listaxk[k], '.8f')
        fxk = format(listafxk[k], '.8f')
        erro = format(listaerro[k], '.8f')

        # escreves os valores no arquivo texto com a formatação querida
        arquivo.write("\t" + str(k) + "\t")
        arquivo.write(str(xk) + "\t")
        arquivo.write(str(fxk) + "\t")
        arquivo.write(str(erro) + "\n")


if __name__ == "__main__": # definição da função main
    main()
