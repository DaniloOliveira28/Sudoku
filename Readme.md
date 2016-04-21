# Projeto 1 - SCC-5900  – Projeto de algoritmos
Este projeto implementa um sistema que resolve o quebra-cabeças Sudoku utilizando algoritmos de força bruta. 

Porém, normalmente os algoritmos de força bruta são pouco eficientes em termos de performance, assim, afim de melhorar este fato adicionaremos algumas heurísticas.

# Problemas de Satisfação de Restrições (PSR)
Para aqueles que imaginam que o Sudoku é um problema de natureza oriental, desminto este grande equívoco. O problema proposto pelo jogo Sudoku é um problema, na verdade, que pode ser considerado de natureza de satisfação de restrição.

Calma, querido leitor, explico.

O objetivo do jogo Sudoku é encontrar uma solução na qual você precisa satisfazer um conjunto de regras.
Por exemplo, dada um tablueiro de Sudoku, semi-completado com números de 1 a 9, você precisa descobrir os outros números que completem o trabuleiro, porém você:
* não pode repetir número na mesma coluna;
* não pode repetir número na mesma linha;
* não pode repetir número na mesma grade 3x3. 

Ou seja, você precisa encontrar uma solução que respeite determinadas restrições. Problema de satisfação de restrição!

A àqueles que precisam ver para crer, demonstro abaixo:

Problema:
```
| 5 1 7 6 . . . 3 4 |
| 2 . 9 . . 4 . . . |
| 3 4 6 2 . 5 . 9 . |
| 6 . 2 . . . . 1 . |
| . 3 8 . . 6 . 4 7 |
| . . . . . . . . . |
| . 9 . . . . . 7 8 |
| 7 . 3 4 . . 5 6 . |
| . . . . . . . . . |
```
Solução:
```
| **5** **1** **7** **6** **9** **8** **2** **3** **4** |
| **2** **8** **9** 1 3 4 7 5 6 |
| **3** **4** **6** 2 7 5 8 9 1 |
| **6** 7 2 8 4 9 3 1 5 |
| **1** 3 8 5 2 6 9 4 7 |
| **9** 5 4 7 1 3 6 8 2 |
| **4** 9 5 3 6 2 1 7 8 |
| **7** 2 3 4 8 1 5 6 9 |
| **8** 6 1 9 5 7 4 2 3 |
```

Como você pode perceber na linha 1, os números não se repete, na coluna 1, os números não se repetem e no quadrado 3x3, os números não se repetem. Parabéns! Você tem uma solução e pode fazer outra coisa da sua vida.

Agora, formalizando o problema e as restrições de uma possível solução segundo PSR.
```javascript
Variáveis: {
    [0,0];[0,1];[0,2];[0,3];[0,4];[0,5];[0,6];[0,7];[0,8];
    [1,0];[1,1];[1,2];[1,3];[1,4];[1,5];[1,6];[1,7];[1,8];
    [2,0];[2,1];[2,2];[2,3];[2,4];[2,5];[2,6];[2,7];[2,8];
    [3,0];[3,1];[3,2];[3,3];[3,4];[3,5];[3,6];[3,7];[3,8];
    [4,0];[4,1];[4,2];[4,3];[4,4];[4,5];[4,6];[4,7];[4,8];
    [5,0];[5,1];[5,2];[5,3];[5,4];[5,5];[5,6];[5,7];[5,8];
    [6,0];[6,1];[6,2];[6,3];[6,4];[6,5];[6,6];[6,7];[6,8];
    [7,0];[7,1];[7,2];[7,3];[7,4];[7,5];[7,6];[7,7];[7,8];
    [8,0];[8,1];[8,2];[8,3];[8,4];[8,5];[8,6];[8,7];[8,8]
}
```

**Domínio**: {1, 2, 3, 4, 5, 6, 7, 8, 9}

**Restrições**:
* R1: Não repetir na linha;
* R2: Não repetir na coluna;
* R3: Não repetir no quadrado 3x3;

**Estado**

Um estado é uma atribuição de valores para algumas ou todas as variáveis.

**Atribuição**: um valor para uma varíavel

Atribuição **consistente**
* Atribuição que não viola nenhuma restrição. 

Atribuição **completa**
* Uma atribuição é **completa** quando toda variável possui um valor. 

**Solução**: Uma **solução** para um PSR é uma atribuição completa e consistente.

# Metodologia

Existem várias técnicas para resolver o problema do Sudo Ku. Neste trabalho vamos usar o Backtracking e mais algumas heurísticas.

A - Backtracking
https://en.wikipedia.org/wiki/Backtracking

B - Backtracking com verificação adiante
http://www.dai.ifma.edu.br/~jcsilva/material/IA-aula-5-CSP-2012.09.23.pdf

C - Backtracking com verificação adiante e mínimos valores remanescentes
http://www.dai.ifma.edu.br/~jcsilva/material/IA-aula-5-CSP-2012.09.23.pdf

obs.: Uma vez que número de atribuições pode ser muito grande para as podas mais fracas, o atual programa aborta a busca quando o número de atribuições excede 1000000 e então imprime uma mensagem “Numero de atribuicoes excede limite maximo”.

# Resultados

Ao rodar o resultados no conjunto de testes formado por 95 jogos de sudoku, chegamos ao seguinte resultado:

a- Resolveu 65 de 90 jogos. Executou em 1588 segundos. Somou 42.300.674 atribuições durante sua execução.

b- Resolveu 82 de 90 jogos. Executou em 1078 segundos. Somou 23.094.370 atribuições durante sua execução.

c- Resolveu 90 de 90 jogos. Executou em 98 segundos. Somou 1.493.560 atribuições durante sua execução.

# Análise

## Com relação a Tentativas

!(DaniloOliveira28)[Data/histograma_atribuicoes.png]
Através do gráfico acima, percebe-se que houve um ganho entre a execuções dos três métodos.

Percebe-se que o algoritmo A é o pior caso 

O algoritimo B reduz o número de execuções que estouraram o limite enquanto aumenta o número de amostras com menos de 130.000 atribuições.

Por fim, o algoritmo C executa praticamente todos 85/95 de amostras com menos de 130.000 atribuições e não estou o limite.

## Com relação ao Tempo Gasto na Execução

!(DaniloOliveira28)[Data/histograma_tempo.png]

Analisando os tempo gasto na execução percebe-se que o algoritmo mais rápido é de fato o C. Analisando o algoritmo A e B, há um fato curioso, o apesar do tempo geral de B ser menor que A, B em alguns casos é mais demorado que A!!!!


Porque? Bom, segundo minha análise, o tempo maior gasto em B em alguns casos ocorre devido ao fato que a cada atribuição consistente no tabuleiro requer que todos os valores que ainda não foram atribuídos e que são impactos por esta mudança sejam atualizados.

obs.: Os testes foram realizados em uma máquina:
MacBook Pro (Retina, 13-inch, Mid 2014), 2.6 GHz Intel Core i5, 8 GB 1600 MHz DDR3.


# Executando o Programa

    Usage: sudoku.py -p [a | b | c] [--cowmode]
        "a : Verificação Adiante"
        "b : Verificação Adiante"
        "c : Verificação Adiante e MVR"
        "--cowmode: Cow Heuristic"

# Cow Heuristic

!(DaniloOliveira28)[Data/cow.jpg]

# Referências
[1] https://uva.onlinejudge.org/external/9/p989.pdf
[1] http://stackoverflow.com/questions/1697334/algorithm-for-solving-sudoku
