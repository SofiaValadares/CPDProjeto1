ENTRADA | C | PYTHON |
:---------: | :------: | :-------: |
Multiplication 
600 | 0.192 seconds | 32.082 seconds
1000 | 1.194 seconds | 158.198 seconds
1400 | 3.369 seconds | 439.760 seconds
1800 | 17.918 seconds | 946.323 seconds
2200 | 39.745 seconds | 1731.402 seconds
2600 | 70.490 seconds | x seconds
3000 | 118.942 seconds | x seconds
Line Multiplication 
600 | 0.103 seconds | 43.061 seconds
1000 | 0.492 seconds | 199.246 seconds
1400 | 1.637 seconds | 549.308 seconds
1800 | 3.714 seconds | 1148.476 seconds
2200 | 6.972 seconds | 2119.244 seconds
2600 | 12.087 seconds | 4070.254 seconds
3000 | 17.878 seconds | x seconds
4096 | 48.913 seconds | |
6144 | 164.480 seconds | |
8192 | 411.651 seconds | |
10240 | 792.512 seconds | |
Block Multiplication 
Block Size = 128
4096 | 89.187 seconds | |
6144 | 305.734 seconds | |
8192 | 723.451 seconds | |
10240 | 1422.087 seconds | |
Block Size = 256
4096 | 91.182 seconds | |
6144 | 300.610 seconds | |
8192 | x seconds | |
10240 | 1407.182 seconds | |
Block Size = 512
4096 | 375.748 seconds | |
6144 | 314.221 seconds | |
8192 | x seconds | |
10240 | x seconds | |



# Performance Evaluation of a single and multi-core

Este projeto teve como objetivo o **estudo da performance do processador na hierarquia de memória** ao aceder tamanhos de dados altos, usando o produto de duas matrizes como objeto de estudo.

De modo a recolher indicadores de performance relevantes, recorremos ao uso de Performance API (PAPI) como indicado no enunciado.

## Performance Evaluation of a single core

Na primeira parte do projeto, foi requisitado a implementação de diferentes versões do algoritmo de produto de duas matrizes. De modo a facilitar a leitura do relatório.
Na primeira parte do projeto tivemos que implementar 3 diferentes versões de um algoritmos do produto de duas matrizes e realizar testes onde deveríamos registrar o tempo de processamento desse códigos.

1. Multiplicação Linha x Coluna
Tivemos que implementar essa versão em duas linguagens, uma em C/C++ e outra em uma linguagem escolhida pelo grupo, a linguagem selecionada foi o python

explicacao do algoritmo em c
explicacao do algoritmo em python

Assim foi realizados os teste bla ela

MATRIZ | C | PYTHON |
:---------: | :------: | :-------: |
600 | 0.192 seconds | 32.082 seconds
1000 | 1.194 seconds | 158.198 seconds
1400 | 3.369 seconds | 439.760 seconds
1800 | 17.918 seconds | 946.323 seconds
2200 | 39.745 seconds | 1731.402 seconds
2600 | 70.490 seconds | x seconds
3000 | 118.942 seconds | x seconds

Foi observado que os testes realizados em C++ foram mais rápido e mais abobrinhas

2. Multiplicação Linha X Linha
Também foi implementado com as duas linguagens citadas acima e bla boa

explicacao do algoritmo em c
explicacao do algoritmo em python

Assim foi realizados os teste bla ela

MATRIZ | C | PYTHON |
:---------: | :------: | :-------: |
600 | 0.103 seconds | 43.061 seconds
1000 | 0.492 seconds | 199.246 seconds
1400 | 1.637 seconds | 549.308 seconds
1800 | 3.714 seconds | 1148.476 seconds
2200 | 6.972 seconds | 2119.244 seconds
2600 | 12.087 seconds | 4070.254 seconds
3000 | 17.878 seconds | x seconds


Foi observado o mesmo que no exemplo anterior e tal tal

Também foram realizados testes somente em c com valores maiores
MATRIZ | C |
:---------: | :------: |
4096 | 48.913 seconds 
6144 | 164.480 seconds 
8192 | 411.651 seconds 
10240 | 792.512 seconds 

3. Multiplicação por bloco
Esse foi implementado somente em c++

explicacao do algoritmo em c

fizemos testes e tals
MATRIZ | C |
:---------: | :------: |
Block Size = 128
4096 | 89.187 seconds 
6144 | 305.734 seconds 
8192 | 723.451 seconds 
10240 | 1422.087 seconds 
Block Size = 256
4096 | 91.182 seconds 
6144 | 300.610 seconds 
8192 | x seconds 
10240 | 1407.182 seconds 
Block Size = 512
4096 | 375.748 seconds 
6144 | 314.221 seconds 
8192 | x seconds 
10240 | x seconds 

foi observado então abobrinhas 

