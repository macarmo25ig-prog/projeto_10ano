# **Planificação**

## 1) Modelo de Dados: 

### Perguntas em Memória
- perguntas em Memória:
Vão ser utilizados tanto **listas** e **dicionarios** ambos, para ser mais facil de fazer as perguntas na Memoria, vai ser feito em outro .py, precisa ter as respostas correta e erradas, tem que ter categoria e dificuldade das perguntas.

```py
perguntas = [
    {
        "Perguntas" : "Quem foi o rei do pop ?",
        "Respostas" : ["Elvis Presley", "Justin Bieber", "Anitta", "Michael Jackson"],
        "Certa" : 3
        "Categoria" : "Musica"
        "Dificuldade" : "facil"
    },
    {
        "Perguntas" : "Qual é o metal cujo símbolo químico é AU ?"
        "Respostas" : ["Prata", "cobre", "ouro", "ferro"],
        "Certa" : 2
        "Categoria" : "Ciencias"
        "Dificuldade" : "dificil"

    }
]
```

### Pontuação
- A pontuação vai ser usada em inteiro, vai ser feito em **listas** e **dicionarios** dependedo da dificuldade quando o jogador acertar vai receber os pontos (facil +1, medio +2, dificil +3, impossivel 4+) somando a o numero anterio, tem sempre que começar do zero e resetar o numero caso for jogar novamente.

### Pontuação guardada
- tem que ter um nome de jogador no inicil e guardar a pontuação em outro .py para salvas todos os pontos em para fazer um top 10 dos jogadores com seus nomes e pontuações.

## 2) Entradas / Processamento / Saídas

### Entradas
- O utilizador vai escrever as escolhas dele, seu nome de jogador, as opções que ele quer, a dificuldade e tambem a categoria do quiz, que ele ira jogar.

### Processamento
- O jogo tera que processar o total de pontos do jogador, as perguntas, as opções escolhidas, como a dificuldade, categoria que ele escolheu no quiz.

### Saídas 
- Tera que aparecer na tela do utilizador o total de pontos que ele teve no final, tem que aparecer quantas perguntas ele acertou, as opções escolhidas pelo jogador e tambem tera que aparecer um "botão" de repitir ou voltar para o menu

## 3) Lista de funções

| Função  |   Descrição      |    Responsabilidades    |   Localização (nome do ficheiro)|
| ------- | ---------------- |-------------------------|---------------------------------|
| `mostrar_menu`    | Mostra o menu e lê a escolha do utilizador   | Matheus | `menus.py`|
| `carregar_perguntas`    | Leitura do ficheiro JSON com as perguntas | Matheus | `perguntas.py`|
| `selecionar_perguntas`    | Vai selecionar uma pergunta no ficheiro de perguntasa   | Matheus | `selecionar_perguntas.py`|
| `guardar_pontos`    | Vai guardar o total de pontos que vc fez e somar para ter o total | Matheus | `pontos.py`|
| `mostrar_pergunta`    | Mostra as perguntas ao usuario   | Matheus | `mostrar_pergunta.py`|
| `tela_final`    | Mostra a tela final ao utilizador, suas opções, quantos pontos ele ganhou e quantas perguntas ele acertou | Matheus | `tela_final.py`|