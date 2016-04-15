# Projeto 1 - SCC-5900  – Projeto de algoritmos
Este projeto implementa um sistema que resolve o quebra-cabeças Sudoku utilizando algoritmos de força bruta com adição de algumas heurísticas.

# Problemas de Satisfação de Restrições (PSR)
Para aqueles que imaginam que o Sudoku é um problema oriental, desminto este grande equívoco. O problema proposto pelo jogo Sudoku é um problema, na verdade, de satisfação de restrição. Calma, querido leitor, explico.

O objetivo do jogo Sudoku é encontrar uma solução na qual dado uma matriz quadrada, você precisa descobrir um conjunto de números que não se repetam na mesma coluna, nem na mesma linha nem na mesma grade 3x3.

A àqueles que precisam ver para crer, demonstro abaixo:

Problema:

5 1 7 6 0 0 0 3 4 
2 8 9 0 0 4 0 0 0 
3 4 6 2 0 5 0 9 0 
6 0 2 0 0 0 0 1 0 
0 3 8 0 0 6 0 4 7 
0 0 0 0 0 0 0 0 0 
0 9 0 0 0 0 0 7 8 
7 0 3 4 0 0 5 6 0 
0 0 0 0 0 0 0 0 0 

Solução:

**5** **1** **7** **6** **9** **8** **2** **3** **4**
**2** **8** **9** 1 3 4 7 5 6 
**3** **4** **6** 2 7 5 8 9 1 
**6** 7 2 8 4 9 3 1 5 
**1** 3 8 5 2 6 9 4 7 
**9** 5 4 7 1 3 6 8 2 
**4** 9 5 3 6 2 1 7 8 
**7** 2 3 4 8 1 5 6 9 
**8** 6 1 9 5 7 4 2 3 




Um PSR é um problema que visa através de técnicas e algoritmos encontrar uma solução que seja completa e 

PSR
Objetivo final: atribuição completa e consistente

# Executando
    default:
        python sudoku

    heurística A
        python sudoku -h A

    heurística B
        python sudoku -h B

# Resultados

# Análise

# Referências
[1] http://stackoverflow.com/questions/1697334/algorithm-for-solving-sudoku

