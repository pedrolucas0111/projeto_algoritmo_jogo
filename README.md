# Descrição do projeto - Jogo PONG

Este projeto implementa um jogo de Ping Pong simples utilizando a biblioteca Pygame em Python. O jogo permite que o usuário jogue contra um oponente controlado por outro usuário, e os controles são feitos através do teclado.

# Funcionalidades
Jogo simples de Ping Pong com controle para dois jogadores.
Pontuação de ambos os jogadores visível na tela.
A bola se move automaticamente e quica nas bordas da tela.
O jogo termina quando um dos jogadores atingir um número máximo de pontos (pode ser ajustado no código).

## PRÉ-REQUISITO
---
Instalar Python
Você pode baixar a versão mais recente do Python em:
https://www.python.org/downloads/

Instalar Pygame
O Pygame é a biblioteca utilizada para criar jogos em Python. Para instalá-la, basta executar o seguinte comando no terminal ou prompt de comando:

pip install pygame

#Como Jogar
Controle do jogador 1 (esquerda):

Use as teclas W para mover para cima e S para mover para baixo.

Controle do jogador 2 (direita):

Use as teclas Seta para cima e Seta para baixo para mover o paddles.
O objetivo do jogo é evitar que a bola passe pelo seu paddle e marcar pontos. O jogo termina quando um jogador atingir um número pré-determinado de pontos.

## Autores

- [Pedro Lucas Garcia de Oliveira - RGM 29997925](https://github.com/pedrolucas0111)
- [Luiza Gabrielly Vitorino da Costa - RGM 29951020](https://github.com/LuizaGVitorino)
- [Maria Victoria Araújo Lopes - RGM 29701325](https://github.com/araujovictoria23)
- [Geovana Silveira Endres - RGM 38193248](https://github.com/GeovanaSilvE)
- [Diogo da Silva Valeriano de Oliveira - RGM 29595177](https://github.com/diholiveira00)

# Documentação

Planejamento:
1. Objetivos do algoritmo definidos com clareza.
O objetivo principal é criar uma versão do jogo Pong onde:
Dois jogadores competem, controlando suas raquetes para rebater uma bola.
A bola deve aumentar a velocidade ao colidir com as raquetes.
O jogo termina quando um jogador atinge 10 pontos.
A interface permite a entrada de nomes para os jogadores e apresenta um menu final com opções para reiniciar ou sair.
Para esse ambiente interativo, foi utilizado a biblioteca ambiente interativo,pygame.
2. Métricas para avaliação de eficiência do algoritmo estabelecidas.
FPS (Frames por Segundo): O jogo deve manter 60 FPS para garantir uma experiência fluida.
Desempenho do loop principal: Deve ser capaz de processar eventos, atualizar estados e renderizar gráficos sem atrasos perceptíveis.
Respostas rápidas: Movimentos das raquetes e atualizações de pontuação devem ocorrer em tempo real.
Uso de memória: Deve ser controlado para evitar vazamentos ou sobrecargas, especialmente em loops de animação.
   3. Estratégia geral de resolução do problema proposta.
Dividir o jogo em componentes principais: raquetes, bola, e interface.
Controlar as colisões entre os elementos para movimentar a bola corretamente.
Usar eventos do Pygame para interações, como controle das raquetes e navegação nos menus.
Desenhar uma interface limpa com atualizações dinâmicas de pontuação, nomes e mensagens de vitória
Adicionar elementos estéticos e interação personalizada, como nomes dos jogadores e animações de vitória.
Dividir o problema em classes (Paddle, Ball) para facilitar o encapsulamento das funcionalidades.
4. Subproblemas identificados e divididos, se aplicável.
Movimentação das raquetes: Gerenciar inputs dos jogadores (teclas W/S e UP/DOWN).
Movimentação e colisão da bola: Atualizar a posição da bola com base na velocidade e detectar colisões com bordas e raquetes.
Pontuação: Atualizar a pontuação de acordo com o lado em que a bola sai da tela.
Exibição gráfica: Desenhar elementos do jogo (raquetes, bola, pontuações, mensagens).
Entrada de nomes e menu final: Capturar entradas de texto para nomes dos jogadores e implementar um menu funcional.


5. Estrutura geral do algoritmo esboçada.
Inicialização: Configurações iniciais de pygame,configurar a janela, variáveis de jogo e as classes que são Paddle e Ball encapsulam os objetos do jogo.
Loop Principal;
	  Capturar eventos (movimentos e saída).
Atualizar estados (posição da bola e raquetes, pontuações).
Redesenhar a tela com base nos novos estados.
Gerencia a interação com os jogadores
Detecção de fim de jogo: Checar se algum jogador alcançou 10 pontos.
Menu final: Apresentar opções de reinício ou saída.
Finalização: Encerrar o jogo com segurança.

 6. Casos limite ou situações especiais identificados.
Velocidade excessiva da bola: Aumentar a velocidade gradualmente, mas limitar seu valor máximo.
Movimento fora dos limites: Impedir que as raquetes saiam da área jogável.
Resoluções não suportadas: Garantir que os elementos do jogo sejam desenhados corretamente mesmo em tamanhos de tela diferentes.
Teclas pressionadas continuamente: Tratar múltiplas entradas simultâneas para evitar conflitos.

7. Análise teórica realizada para verificar a correção do algoritmo.
Movimentação da bola: A lógica de colisão considera direções e pontos de impacto, garantindo que a bola mude de trajetória corretamente. Para isso foi utilizada a função adjust_ball_velocity.
Limitação das raquetes: O uso da classe Paddle garante que as raquetes se mantenham dentro dos limites. A função handle_collision verifica adequadamente as condições de colisão com as raquetes e bordas.
Pontuação: As condições para aumentar a pontuação são definidas corretamente (quando a bola cruza os limites esquerdo ou direito da tela).
Estados do jogo: Os ciclos de jogo (início, gameplay, vitória, menu final) estão logicamente encadeados, evitando inconsistências.
Interface e entrada de dados: A coleta de nomes e comandos dos jogadores está integrada ao fluxo do jogo, garantindo uma transição suave entre telas e fases do jogo

8. Complexidade de Tempo (Time Complexity)
Desenho dos elementos
O método draw() redesenha todos os elementos na tela (placar, nomes, barra de separação, bolas e paddles) a cada frame. Como o número de elementos é constante, o tempo de execução desta etapa é O(1).
Movimentação da bola e colisões
A posição da bola é atualizada e verificada para colisões a cada iteração. Como há apenas duas paddles e as colisões com as paredes são fixas, o custo é O(1).
Movimentação dos paddles
As teclas pressionadas são verificadas a cada frame, com condições simples para limitar a movimentação. O custo também é O(1).
2. Complexidade de Espaço (Space Complexity)
Variáveis armazenadas
Cada paddle, bola e texto é representado como objetos ou primitivas simples. Esses elementos ocupam espaço constante na memória, independentemente do tamanho da tela ou número de frames. Assim, a complexidade de espaço é O(1).
3. Eficiência Geral
O algoritmo do jogo não depende diretamente do tamanho de entrada variável (como listas ou matrizes). Portanto:
A complexidade de tempo geral para cada frame é O(1).
A complexidade de espaço é O(1).
Essa análise indica que o jogo é eficiente e capaz de manter o desempenho constante independentemente da duração ou dos ajustes nos parâmetros (como tamanho da janela ou velocidade).

## Avaliação da eficácia do algoritmo em termos de tempo de execução, uso de recursos e precisão na resolução do problema. <br/>
Tempo de execução:<br/>
O jogo é executado em 60 FPS (quadros por segundo), o que é suficiente para uma experiência fluida. O uso do relógio (pygame.time.Clock()) regula o tempo, prevenindo consumo desnecessário de CPU.
O código não apresenta operações complexas ou loops intensivos, então o tempo de execução é eficiente.<br/>
Uso de recursos:<br/>
O uso de pygame é bem otimizado. Apenas os elementos necessários são redesenhados em cada frame.
As cores, fontes, e tamanhos são carregados uma vez, evitando reprocessamento.
O controle da velocidade da bola e o movimento dos jogadores são implementados de forma eficiente.<br/>
Precisão na resolução do problema:<br/>
A detecção de colisão (tanto nas bordas quanto nas raquetes) é precisa. A velocidade da bola é ajustada proporcionalmente ao ponto de colisão, simulando física simples.
A contagem de pontos e as condições de vitória funcionam conforme esperado.
Conclusão:<br/>
O algoritmo é eficaz, garantindo fluidez e precisão durante o jogo.
Avaliação da colaboração da equipe e cumprimento dos prazos.
Colaboração:<br/>
As responsabilidades foram bem distribuídas entre os membros da equipe.
O uso de classes (Paddle e Ball) e funções facilita a divisão do trabalho, tornando o código modular.<br/>
Cumprimento dos prazos:<br/>
Conseguimos ter uma ótima dinâmica, dividimos as partes e todos conseguiram entregar no prazo, sentimos algumas dificuldades mas em equipe conseguimos solucionar os erros a tempo. 

## Conclusões do projeto destacando os resultados e aprendizados.
Resultados: <br/>
O jogo foi desenvolvido com sucesso, seguindo o planejamento.
O algoritmo apresenta boa eficiência e funciona conforme o esperado.
A interface é intuitiva, e o jogo é dinâmico.
Aprendizados:
Uso de classes para organizar o código.
Controle do tempo e atualização de quadros em jogos com pygame.
Implementação de detecção de colisão e física básica.
Trabalho em equipe e divisão de responsabilidades para concluir um projeto.


#Check list
Checklist para o Projeto de Algoritmo em Computabilidade e Complexidade de Algoritmo<br/>
Fase 1: Análise [ Pedro e Luiza] <br/>
[Luiza] Problema selecionado e definido claramente.<br/>
[Luiza]  Compreensão aprofundada da natureza e desafios do problema.<br/>
[Pedro] Modelo matemático ou teórico desenvolvido para representar o problema.<br/>
Fase 2: Planejamento [Pedro e Luiza]<br/>
[Pedro] Objetivos do algoritmo definidos com clareza.<br/>
[Pedro] Métricas para avaliação de eficiência do algoritmo estabelecidas.<br/>
[Pedro] Estratégia geral de resolução do problema proposta.<br/>
[Pedro] Subproblemas identificados e divididos, se aplicável.<br/>
[Luiza] Estrutura geral do algoritmo esboçada.<br/>
[Luiza] Casos limite ou situações especiais identificados.<br/>
[Luiza] Análise teórica realizada para verificar a correção do algoritmo.<br/>
Fase 3: Desenho [Luiza]<br/>
[Luiza] Análise de complexidade realizada para avaliar a eficiência teórica do algoritmo.<br/>
[Pedro] Pontos críticos do algoritmo identificados para otimização, se necessário.<br/>
Fase 4: Programação e Teste [ Geovana] <br/>
[Geovana] Algoritmo traduzido com precisão em código de programação.<br/>
[Geovana] Código de programação escrito de forma clara e organizada.<br/>
[Geovana]  Testes rigorosos realizados em uma variedade de casos de teste.<br/>
[Geovana] Casos limite e situações especiais testados.<br/>
[Geovana] Erros e problemas durante o teste de programa identificados e corrigidos.<br/>
Documentação e Avaliação do Projeto [ ] <br/>
[Diogo ] Documentação completa, incluindo especificação do algoritmo e análise de complexidade.<br/>
[Diogo] Documentação revisada para clareza e rigor técnico.<br/>
[Maria  Victoria ] Avaliação da eficácia do algoritmo em termos de tempo de execução, uso de recursos e precisão na resolução do problema.<br/>
[Maria  Victoria] Avaliação da colaboração da equipe e cumprimento dos prazos.<br/>
Apresentação e Conclusão do Projeto [ ] <br/>
[Maria  Victoria] Apresentação do projeto preparada com informações claras e objetivas.<br/>
[Maria  Victoria] Conclusões do projeto destacando os resultados e aprendizados.<br/>
[Diogo ] Discussão sobre o projeto e respostas a perguntas da audiência.<br/>
Este checklist pode ser usado como um guia para garantir que todas as etapas do projeto sejam concluídas de forma eficaz e que o projeto seja avaliado de acordo com critérios específicos de sucesso. <br/>
