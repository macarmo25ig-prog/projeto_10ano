import json
import random

def mostrar_menu():
    while True:
        print("----------* Pior quiz já feito *----------")
        print("1 - Jogar")
        print("2 - Regras")
        print("3 - Classificações")
        print("0 - Sair")
        op = int(input("Introduz a tua opção: "))

        if op == 0:
            break  
        elif op == 2:
            regras()
        elif op == 3:
            print("Aqui vai ficar a classificação")
        else:
            return op
        
def carregar_perguntas():
    perguntas = []

    with open("perguntas.json", "r", encoding="utf-8") as f:
        perguntas = json.load(f)

    return perguntas

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


def verifica_resposta(pergunta, resposta):
    if resposta == pergunta["Certa"]:
        return True
    else:
        return False
    
def regras():
    print("------------------------------------*   Regras   *-----------------------------------------")
    print("\n1. Não pode selecionar algo fora das opções que tem de respota na hora que estiver jogando\n"   )
    print("2. Você ganha mais pontos depedendo da dificuldade da pergunta que acertar, sendo elas:")
    print("-- Facil +1 -- Medio +2 -- Dificil +3 --")
    print("\n3. toda vez que iniciar sua pontuação vai ser salva para vc poder ver dps no menu de classificação\n")
    input("Para sair aperte ENTER...")

def menu_final(pontos, p_perguntas, r_perguntas):

    print("---------------*  Fim de Jogo  *-----------------")
    print(f"\nvc acertou {p_perguntas} perguntas, Parabens!! :) \n")
    print(f"vc erro {r_perguntas} perguntas, melhor na proxima amigo :( ")
    print(f"\nvc teve {pontos} pontos, Parabens!! ;) \n")
    print(f"0 - Retornar")
    print(f"1 - Jogar Novamente")
    respota = int(input("Introduza a sua escolha: "))
    if respota == 0:
        mostrar_menu()
    elif respota == 1:
        main()

def main():
    pontos = 0
    p_perguntas = 0
    r_perguntas = 0
    op = mostrar_menu()
    if op == 1:
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

        menu_final(pontos, p_perguntas, r_perguntas)

main()


