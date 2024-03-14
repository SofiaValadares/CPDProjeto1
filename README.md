# Performance Evaluation of a single and multi-core

Este projeto teve como objetivo o **estudo da performance do processador na hierarquia de memória** ao aceder tamanhos de dados altos, usando o produto de duas matrizes como objeto de estudo.

Isso será feito através de duas partes distintas: na primeira parte, será analisado o impacto da hierarquia de memória em um único núcleo de processamento, enquanto na segunda parte, serão investigadas implementações paralelas em sistemas multi-core. 

A Performance API (PAPI) será utilizada para coletar indicadores de desempenho relevantes.

## Performance Evaluation of a single core

Na primeira parte do projeto, foi requisitado a implementação de diferentes versões do algoritmo de produto de duas matrizes. De modo a facilitar a leitura do relatório.</br>
Nesta parte do projeto, será realizada uma avaliação de desempenho de um único núcleo de processamento. O foco será entender como a hierarquia de memória impacta o desempenho ao acessar grandes volumes de dados, utilizando a multiplicação de matrizes como exemplo.
Foram implementadas 3 diferentes versões de um algoritmos do produto de duas matrizes, ultilizando de duas diferentes liguagens, C++ e Python.

**1. MULTIPLICAÇÃO LINHA X COLUNA** </br>
Nesta abordagem, o algoritmo implementado multiplica uma linha da primeira matriz por cada coluna da segunda matriz. Esse algoritimo foi implenetado em C++ e Pyhton.

~~~C++
    Time1 = clock();

    for(i=0; i<m_ar; i++)
      {	for( j=0; j<m_br; j++)
        {	temp = 0;
          for( k=0; k<m_ar; k++)
          {	
            temp += pha[i*m_ar+k] * phb[k*m_br+j];
          }
          phc[i*m_ar+j]=temp;
        }
      }

    Time2 = clock();
    sprintf(st, "Time: %3.3f seconds\n", (double)(Time2 - Time1) / CLOCKS_PER_SEC);
    cout << st;
~~~
~~~Python
    Time1 = time.time()

    for i in range(m_ar):
        for j in range(m_br):
            temp = 0
            for k in range(m_ar):
                temp += pha[i*m_ar + k] * phb[k*m_br + j]
            phc[i*m_ar + j] = temp

    Time2 = time.time()
    print(f"Time: {((Time2 - Time1)):.3f} seconds\n")
~~~


O tempo de processamento é registrado para matrizes de entrada variando de 600x600 a 3000x3000 elementos, com incrementos de 400 em ambas as dimensões, nas duas linguagens.
O compilador C++ é configurado com a flag de otimização -O2 para garantir uma compilação otimizada.

MATRIZ | C | PYTHON |
:---------: | :------: | :-------: |
600 | 0.192 seconds | 32.082 seconds
1000 | 1.194 seconds | 158.198 seconds
1400 | 3.369 seconds | 439.760 seconds
1800 | 17.918 seconds | 946.323 seconds
2200 | 39.745 seconds | 1731.402 seconds
2600 | 70.490 seconds | x seconds
3000 | 118.942 seconds | 3502.117 seconds

Essas implementações permitirão comparar o desempenho entre diferentes linguagens de programação na execução do mesmo algoritmo de multiplicação de matrizes.

Foi observado que o tempo de processamento almenta conforme o tamanho da matriz. Fora isso também foi observado que a matriz sempre é mais rapidamente processada em C++ do que em python, esta diferença de tempo também fica maior quanto maior for a matriz.

**2. MULTIPLICAÇÃO LINHA X LINHA** </br>
Nessa vesão multipicamos cada linha de primeira matriz por cada linha da segunda matriz (explicar isso melhor) </br>
Também foi implementada nas mesmas duas liguagens que a primeira versão

~~~C++
    Time1 = clock();
	
	for(i=0; i<m_ar; i++)
	{
		for(j=0; j<m_ar; j++)
		{
			for(k=0; k<m_br; k++)
			{	
				phc[i*m_ar+k] += pha[i*m_ar+k] * phb[j*m_ar+k];
			}
		}
	}

    Time2 = clock();
    sprintf(st, "Time: %3.3f seconds\n", (double)(Time2 - Time1) / CLOCKS_PER_SEC);
    cout << st;
~~~
~~~Python
    Time1 = time.time()
    
    for i in range(m_ar):
        for j in range(m_ar):
            for k in range(m_br):
                phc[i*m_ar + k] += pha[i*m_ar + k] * phb[j*m_ar + k]


    Time2 = time.time()
    print(f"Time: {((Time2 - Time1)):.3f} seconds\n")
~~~

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

**3. MULTIPLICAÇÃO POR BLOCO** </br>
Esse foi implementado somente em c++

~~~C++
    Time1 = clock();
	
	for (ib=0; ib<m_ar; ib+= bkSize) 
	{
		for (jb=0; jb<m_br; jb+=bkSize) 
		{
			for (kb=0; kb<m_ar; kb+=bkSize)
			{
				for(i=ib; i<min(ib+bkSize, m_ar); i++)
				{	
					for(j=jb; j<min(jb+bkSize, m_br); j++)
					{	
						for(k=kb; k<min(kb+bkSize, m_ar); k++)
						{	
							phc[i*m_ar+j] += pha[i*m_ar+k] * phb[k*m_br+j];
						}
					}
				}
			}
		}
	}

    Time2 = clock();
    sprintf(st, "Time: %3.3f seconds\n", (double)(Time2 - Time1) / CLOCKS_PER_SEC);
    cout << st;
~~~

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
8192 | 3817.102 seconds 
10240 | 1407.182 seconds 
Block Size = 512
4096 | 375.748 seconds 
6144 | 314.221 seconds 
8192 | x seconds 
10240 | x seconds 

foi observado então abobrinhas 

## Performance evaluation of a multi-core implementation
Foi acrecentado paralelismo e tals, foi posto duas versões de paralelismo
Implementado somente em C++



### Produto de duas matrizes - Versão Python

Escolhemos implementar o [algoritmo](/link) que foi concedido aos estudantes em [Python](). Após ter a implementação concluída, registamos os tempos de processamento indicados abaixo:

#### EM C:

//Inserir tabela

#### EM Python:

//Inserir tabela




## 💻 Desenvolvedores:
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/gabrieltmjr">
        <img src="https://avatars.githubusercontent.com/u/73040950?v=4" width="100px;" alt="Foto Matheus Gomes"/><br>
        <sub>
          <b>Gabriel Machado Jr</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/guiga-sa">
        <img src="https://avatars.githubusercontent.com/u/123979639?v=4" width="100px;" alt="Foto Megas"/><br>
        <sub>
          <b>Guilherme Araujo</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/SofiaValadares">
        <img src="https://avatars.githubusercontent.com/u/113111708?v=4" width="100px;" alt="Foto Sofia Valadares"/><br>
        <sub>
          <b>Sofia Valadares</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
<br></br>



