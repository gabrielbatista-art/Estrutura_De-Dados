from deque2 import *

def media(valores,k):
    apuracao = deque()
    for c in range(len(valores)):
        if c < k - 1:
            apuracao.adiciona_ultimo(None)
        else:
            soma = sum(valores[c-(k-1):c+1])
            if c >= k - 1:
                resultado = soma / k
                apuracao.adiciona_ultimo(resultado)
    return apuracao

def receber_k():
    k = input("Digite o valor de k")

    if k == 0:
        raise IndexError("Valor inválido")
    elif k == "":
        k = 7
    else:
        k = int(k)
    return k

def receber_valores():
    numeros = []
    volume_trafego = int(input("Digite a quantidade de lista de carros registrados"))
    for i in range(volume_trafego):
        val_entrada = input("Digite o número do volume de carros, separada por vírgula: ")
        lista_valores = []
        for valor in val_entrada.split(","):
            lista_valores.append(int(valor.strip()))
        numeros.append(lista_valores)
    return numeros

def ler_arquivo(arquivo):
    informacao = []
    with open('arquivo.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        informacao = eval(conteudo)
    return informacao

menu = int(input("""Digite a opção que deseja: \n 1- Ler dados do volume de trafego a partir do teclado\n 2- Ler dados do volume de trafego a partir de arquivo texto"""))

if menu == 1:
    valores_trafego = receber_valores()
elif menu == 2:
    valores_trafego = ler_arquivo("arquivo.txt")
else:
    raise IndexError("Valor inválido")
    exit()

k = receber_k()

if valores_trafego:
    with open("medias.txt", "w") as salvar_result:
        for valores in valores_trafego:
            medias_moveis = media(valores_trafego, k)
            print("Médias móveis:", end=" ")
            while not medias_moveis.vazia():
                result = medias_moveis.delete_comeco()
                if result is not None:
                    print(f"{result:.1f}", end=", ")
                    salvar_result.write(f"{result:.1f}")
                else:
                    print("None", end=", ")
                    salvar_result.write("None")
                if not medias_moveis.vazia():
                    salvar_result.write(", ")
            salvar_result.write("\n")
            print() 
