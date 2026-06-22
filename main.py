import json

def mostrar_menu():
    while True:
        print("----------* Quizz mais lindo! *----------")
        print("1 - Jogar")
        print("2 - Regras")
        print("3 - Classificações")
        print("0 - Sair")
        op = int(input("Introduz a tua opção: "))

        if op == 0:
            break
        if op >= 1 and op <= 3:
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
    print(f"-- Dificuldade: {pergunta['Dificuldade']}\n --")
    op = int(input("Qual a resposta correta? ")) 
    return op


def verifica_resposta(pergunta, resposta):
    if resposta == pergunta["Certa"]:
        print(f"parabens")
    else:
        print(f"errouu feio")

def main():
    op = mostrar_menu()

    if op == 1:
        print("Aqui vai ficar a função de jogar")
    elif op == 2:
        print("Aqui vão ficar as regras")
    elif op == 3:
        print("Aqui vai ficar a classificação")


# main()
p = carregar_perguntas()
mostrar_pergunta(p[0])