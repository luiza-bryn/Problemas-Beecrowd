# Resolucao-de-problemas
Diversos códigos envolvendo questões de programação (questões encontradas em olimpíadas de informática, provas, etc)

# Questões presentes neste repositório

1. **bazinga.py - Bazinga! (Maratona UnB de Programação 2014)**

No oitavo episodio da segunda temporada do seriado The Big Bang Theory, The Lizard-Spock Expansion, Sheldon e Raj discutem qual dos dois é o melhor: o filme Saturn 3 ou a série Deep Space 9. 
A sugestão de Raj para a resolução do impasse é uma disputa de Pedra-Papel-Tesoura. Contudo, Sheldon argumenta que, se as partes envolvidas se conhecem, entre 75% e 80% das disputas de Pedra-Papel-Tesoura terminam empatadas, e então sugere o Pedra-Papel-Tesoura-Lagarto-Spock.

As regras do jogo proposto são:
- a tesoura corta o papel;
- o papel embrulha a pedra;
- a pedra esmaga o lagarto;
- o lagarto envenena Spock;
- Spock destrói a tesoura;
- a tesoura decapita o lagarto;
- o lagarto come o papel;
- o papel contesta Spock;
- Spock vaporiza a pedra;
- a pedra quebra a tesoura.

Embora a situação não se resolva no episódio (ambos escolhem Spock, resultando em um empate), não é difıcil deduzir o que aconteceria se a disputa continuasse. 
Caso Sheldon vencesse, ele se deleitaria com a vitória, exclamando "Bazinga!"; caso Raj vencesse, ele concluiria que "Raj trapaceou!"; caso o resultado fosse empate, ele exigiria nova partida: "De novo!". 
Conhecidas as personagens do jogo escolhido por ambos, faça um programa que imprima a provável reação de Sheldon.

Entrada
A entrada consiste em uma série de casos de teste. A primeira linha contém um inteiro positivo T (T ≤ 100), que representa o número de casos de teste. 
Cada caso de teste é representado por uma linha da entrada, contendo as escolhas de Sheldon e Raj, respectivamente, separadas por um espaço em branco. 
As escolha possíveis são as personagens do jogo: pedra, papel, tesoura, lagarto e Spock.

Saida
Para cada caso de teste deverá ser impressa a mensagem "Caso #t: R", onde t é o número do caso de teste (cuja contagem se inicia no número um) e R é uma das três reações possíveis de Sheldon: "Bazinga!", "Raj trapaceou!", ou "De novo!".

2. **magic_and_swords.py - Bazinga! (Maratona UnB/CIC de Programação 2015)**

No tower defense Magic and Sword, o jogador pode lançar magias de área para derrotar as unidades inimigas. As magias são elementais: fogo, água, ar e terra, e a região afetada é determinada por um círculo cujo raio depende do nível da magia.

A tabela abaixo lista cada magia, o dano e o respectivo raio por nível:

| Magia | Descrição                                                                  | Dano | Level 1 | Level 2 | Level 3 |
|-------|----------------------------------------------------------------------------|------|---------|---------|---------|
| Fogo  | Um meteoro é conjurado para eliminar unidades inimigas com o calor do fogo | 200  | 20      | 30      | 50      |
| Água  | Uma tsunami arrasta os inimigos com a força da água                        | 300  | 10      | 25      | 40      |
| Terra | Um terremoto abala as unidades inimigas, causando dano massivo             | 400  | 25      | 55      | 70      |
| Ar    | Um tornado mina as forças inimigas com a velocidade do ar                  | 100  | 18      | 38      | 60      |

As unidades inimigas são delimitadas por um retângulo de largura w e altura h, com canto inferior esquerdo posicionado no ponto (x0, y0). O inimigo sofrerá dano caso seu retângulo delimitador tenha qualquer intercessão com a área deﬁnida pelo círculo da magia.

Dada a posição e o retângulo delimitador da unidade inimiga, o centro da explosão e o identiﬁcador e o nível da magia, determine o dano sofrido pela unidade. Caso a unidade esteja fora do alcance da magia, o dano sofrido é igual a zero.

Entrada
A entrada consiste em T (1 ≤ T ≤ 1000) casos de teste, onde o valor de T é informado na primeira linha da entrada. Cada caso de teste é composto por duas linhas. A primeira contém quatro número inteiros que repre-sentam as dimensões w e h (1 ≤ w, h ≤ 1000) do retângulo e as coordenadas x0 e y0 (0 ≤ x0, y0 ≤ 1000) do canto inferior esquerdo. A segunda linha do caso de teste contém uma string com o identiﬁcador da magia (ﬁre para fogo, water para água, earth para terra e air para ar), o nível N desta magia (1 ≤ N ≤ 3) e as coordenadas cx e cy (0 ≤ cx, cy ≤ 1000) do centro da área da explosão.

Saída
Para cada caso de teste, a saída deve ser o valor do dano recebido pela unidade, seguido de uma quebra de linha.