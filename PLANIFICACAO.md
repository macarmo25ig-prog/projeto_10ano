# **Planificação**

## Modelo de dados
- perguntas em Memória:
Vão ser utilizados tanto **listas** e **dicionarios** ambos, para ser mais facil de fazer as perguntas na Memoria, vai ser feito em outro .py, precisa ter as respostas correta e erradas, tem que ter categoria e dificuldade das perguntas.

```py
perguntas = [
    {
        "Perguntas" : "Quem foi o rei do pop?",
        "Respostas" : ["Elvis Presley", "Justin Bieber", "Anitta", "Michael Jackson"],
        "Certa" : 3
        "Categoria" : "Musica"
        "Dificuldade" : "facil"
    }
]
```

## Pontuação
- A pontuação vai ser usada em inteiro, vai ser feito em **lista** dependedo da dificuldade quando o jogador acertar vai receber os pontos (facil +1, medio +2, dificil +3, impossivel 4+) somando a o numero anterio, tem sempre que começar do zero e resetar o numero caso for jogar novamente.

```py
ponto = 0
```

## Pontuação guardada
- tem que ter um nome de jogador no inicil e guardar a pontuação em outro .py para salvas todos os pontos em para fazer um top 10 dos jogadores com seus nomes e pontuações.