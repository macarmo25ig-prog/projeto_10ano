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
- O jogo tera que processar o total de pontos do jogador, as perguntas, as opções escolhidas, qual a dificuldade e categoria que ele escolheu no quiz.

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

## 4) Fluxo do programa

1. Ao iniciar, ele ira limpar o ecrã e mostrar primeiro uma pergunta de qual é o seu nome.

2. Depois de colocar o nome, ira aparecer o menu do jogo com as opções.

3. Se o jogador selecionar jogar, vai aparecer um menu para escolher a dificuldade e a categoria que vai ser o quiz, caso o jogador escolha errado ou opção que não existe, vai aparecer um erro na tela pedindo pra selecionar uma das opções disponiveis e vai voltar pro menu para escolher uma opção correta e não ira fechar o jogo.

4. Depois que o utilizador selecionar as opções de jogo, vai carregar as perguntas e vai fazer um ciclo aparecendo um por um, com as respostas e opções a baixo da pergunta, depois de completar todas as perguntas o ciclo vai terminar.

5. Passando pra tela final do jogo, com a pontuação do jogador, a quantidade de acertos e duas opções de voltar a tela inicial e a opção de repetir o jogo, caso o jogador escolhar repetir vai voltar a fazer o ciclo de perguntas para o usuario e repetir a tela final, mas caso o jogador/utilizador escolher a opção de voltar ao menu, vai levar o jogador/utilizador a tela inicial e não tendo que escolher um nome dessa vez, E todas as informações do jogo antigo tem que ser guardado, o total de acerto, o total de erros, a dificuldade e caso o jogador jogue novamente, as perguntas iram ser alternadas.

6. No menu tambem tem a opção de ver o Top 10 melhores jogadores que jogaram, esconlhendo essa opção você consegue ver o seu local na tabela com as suas informações.

## 5) Ecrãs do programa
| Ecrã | O que mostrar / pedir ao utilizador      |
| ------- | ---------------- |
| Menu_nome  | Ira pedir ao utilizador que coloque seu nome de jogador |
| Menu_inicial    | ira aparecer as opções de jogo na tela do jogador, como: jogar,top melhores, regras, sair |
| Menu_dificuldade  | Sera o menu de dificuldades depois de escolher jogar na tela inicila |
| Menu_classificação | Sera o menu onde vai aparecer o top melhores jogadores e suas pontuações |
| Menu_final  | Tela final depois que o jogo acabar que aparecera as informações da partida |
| Menu_regras| sera a tela onde ficara as informações do jogo |

## 6)