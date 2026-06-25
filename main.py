import json
import random


# Objetivo: Carregar jogadores do ficheiro de jogadores
# Entra: 
# - ficheiro: Nomes
# Devolve:
# - jogadores: Lista com os jogadores
def carregar_nomes(ficheiro):
    jogadores = []
    with open(ficheiro, "r") as f:
        jogadores = json.load(f)
    return jogadores

# Objetivo: Guardar os nomes dos jogadores no ficheiro de jogadores
# Entra: 
# - ficheiro: Nomes
# Devolve:
# - lista: Ele devolve uma lista com os nomes guardados
def guarda_nomes(lista, ficheiro):
    with open(ficheiro, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)

# Objetivo: Pedir os nomes dos jogadores
# Entra: 
# - ficheiro: Nomes
# Devolve:
# - op: A introdução de um nome
def pedir_nome():
    op = input("Por favor introduza o seu nickname: ")
    return op

# Objetivo: Mostrar as classificações dos jogadores
# Entra: 
# - ficheiro: Nomes
# Devolve:
# - jogadores: Devolve o nome e os pontos do jogadores em um menu
def classificacao(jogadores):
    print("\n----------* Classificações *----------\n")
    for jogador in jogadores:
        print(f"Jogador: {jogador["Nome"]}\n")
        i = 1
        for pontuacao in jogador["Pontos"]:
            print(f"{i}ª Tentativa: {pontuacao}")
            i = i + 1
        print("\n----------* *----------\n")

# Objetivo: Mostrar o menu do jogo para os jogadores
# Entra: 
# - ficheiro: Main
# Devolve:
# - jogadores: Devolve ao jogadores o menu de inicil do jogo e a opção do jogador
def mostrar_menu(jogadores):
    while True:
        print("----------* Um quizz mesmo lindo! Como o professor!111! *----------")
        print("1 - Jogar")
        print("2 - Regras")
        print("3 - Classificações")
        print("0 - Sair")
        op = int(input("Introduz a tua opção: "))

        if op == 0:
            print("Adeus... Foi bom... Gostei muito! Adeus... Fico triste... Mas pronto... Eu fico aqui, sozinho... Xau... :(")
            break  
        elif op == 2:
            regras()
        elif op == 3:
            classificacao(jogadores)
        elif op > 3:
            print("Você introduziu o numero errado, por favor escolha o numero correto :)")
            return mostrar_menu()
        elif op < 0:
            print("Você introduziu o numero errado, por favor escolha o numero correto :)")
            return mostrar_menu()
        else:
            return op

# Objetivo: Carrgar as perguntas do outro ficheiro
# Entra: 
# - ficheiro: Perguntas.json
# Devolve:
# - jogadores: Um dicionario com listas com os nomes dos jogadores        
def carregar_perguntas():
    perguntas = []

    with open("perguntas.json", "r", encoding="utf-8") as f:
        perguntas = json.load(f)

    return perguntas

# Objetivo: Mostrar as perguntas guardadas no outro ficheiro de perguntas e deixar mais bonito as perguntas
# Entra: 
# - ficheiro: Perguntas
# Devolve:
# - jogadores: A opção do jogador por der escolher e tambem mostrando a pergunta ao jogador
def mostrar_pergunta(pergunta):
    i = 0
    print("\n----------* Pergunta *----------\n")
    print(f"-- {pergunta['Perguntas']} --")
    for resposta in pergunta["Respostas"]:
        print(f"{i} - {resposta}")
        i = i + 1
    print(f"-- Dificuldade: {pergunta['Dificuldade']}\n")
    op = int(input("Qual a resposta correta? ")) 
    return op

# Objetivo: Verifica se as respostas estão corretas com base nas informação do ficheiro de perguntas
# Entra: 
# - ficheiro: Perguntas
# Devolve:
# - jogadores: Se a resposta do jogador foi correta ou errada
def verifica_resposta(pergunta, resposta):
    if resposta == pergunta["Certa"]:
        return True
    else:
        return False

# Objetivo: Mostrar as regras do jogo ao jogador
# Entra: 
# - ficheiro: Main
# Devolve:
# - jogadores: Mostra as regras que ele tem que seguir pra jogar
def regras():
    print("------------------------------------*   Regras   *-----------------------------------------")
    print("\n1. Não pode selecionar algo fora das opções que tem de respota na hora que estiver jogando\n"   )
    print("2. Você ganha mais pontos depedendo da dificuldade da pergunta que acertar, sendo elas:")
    print("-- Facil +1 -- Medio +2 -- Dificil +3 --")
    print("\n3. toda vez que iniciar sua pontuação vai ser salva para vc poder ver dps no menu de classificação\n")
    input("Para sair aperte ENTER...")

# Objetivo: Mostrar um menu no fim do jogo ao jogador
# Entra: 
# - ficheiro: main
# Devolve:
# - jogadores: Um menu com as opções que ele pode escolher e informações da partida do jogador como: acertos de perguntas, erros e o total de pontos ganhos
def menu_final(pontos, p_perguntas, r_perguntas):

    print("---------------*  Fim de Jogo  *-----------------")
    print(f"\nvc acertou {p_perguntas} perguntas, Parabens!! :) \n")
    print(f"vc erro {r_perguntas} perguntas, melhor na proxima amigo :( ")
    print(f"\nvc teve {pontos} pontos, Parabens!! ;) \n")
    print(f"0 - Retornar")
    print(f"1 - Jogar Novamente")
    respota = int(input("Introduza a sua escolha: "))
    if respota == 0:
        main()
    elif respota == 1:
        main()

# Objetivo: Verifica se já existe um jogador no ficheiro de informações do jogadores
# Entra: 
# - ficheiro: nomes
# Devolve:
# - jogadores: Ele vai fazer um teste que se o jogador já existir o nome dele no ficheiro
def verifica_jogador(jogadores, nome):
    for jogador in jogadores:
        if jogador["Nome"] == nome:
            jogador_atual = jogador
            return jogador_atual
    
    jogador_atual = {
        "Nome" : nome,
        "Pontos" : []
    }
    jogadores.append(jogador_atual)
    return jogador_atual

# Objetivo: Atualizar o ficheiro do jogadores, como seus pontos e seu nome para fazer a classificação
# Entra: 
# - ficheiro: Nomes
# Devolve:
# - jogadores: Atualiza as infomações dos jogadores já existentes
def atualiza_jogador(jogadores, jogador_atual):
    for jogador in jogadores:
        if jogador["Nome"] == jogador_atual["Nome"]:
            jogador["Pontos"] = jogador_atual["Pontos"]
            return jogadores
    print("Deu cocó!")
    return 0

# Objetivo: A base principal do jogo que é aonde tem o numero de ponto, acertos e erros, as dificuldades, onde tem a chamada das funções já listadas e tambem o codigo principal para o jogo funcionar
# Entra: 
# - ficheiro: Main
# Devolve:
# - jogadores: É a onde o jogadores vão receber seus pontos de acordo com a dificuldade, suas respostas serão verificadas, onde as funções já vistas antes vão ficar, as informações e o nome dos jogadores serão mandadas pelas outra funções ao ficheiro de nomes
def main():
    jogadores = carregar_nomes("nomes.json")
    pontos = 0
    p_perguntas = 0
    r_perguntas = 0
    op = mostrar_menu(jogadores)
    if op == 1:
        nome = pedir_nome()
        jogador_atual = verifica_jogador(jogadores, nome)
        p = carregar_perguntas()

        perguntas_selecionadas = random.sample(p, 10)

        for pergunta in perguntas_selecionadas:
            op = mostrar_pergunta(pergunta)
            validacao = verifica_resposta(pergunta, op)
            if validacao:
                print("-- :O VOCÊ É UMA MAQUINAA! --")
                if pergunta["Dificuldade"] == "facil":
                    pontos = pontos + 1
                    p_perguntas = p_perguntas + 1
                elif pergunta["Dificuldade"] == "medio":
                    pontos = pontos + 2
                    p_perguntas = p_perguntas + 1
                elif pergunta["Dificuldade"] == "dificil":
                    pontos = pontos + 3
                    p_perguntas = p_perguntas + 1
                print(f"-- Vc tem {pontos} pontos --")
            else:
                print("-- :( Errouuuu --")
                print(f"-- Vc tem {pontos} pontos --")
                r_perguntas = r_perguntas + 1
        jogador_atual["Pontos"].append(pontos)
        jogadores = atualiza_jogador(jogadores, jogador_atual)
        guarda_nomes(jogadores, "nomes.json")

        menu_final(pontos, p_perguntas, r_perguntas)


main()


