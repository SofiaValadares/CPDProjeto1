Esse projeto foi desenvolvido na cadeira de Computação Paralela e Distributiva da FEUP, mestrada pelo professor Jorge Manuel Gomes Barbosa.

# Performance Evaluation of a single and multi-core

Este projeto teve como objetivo o **estudo da performance do processador na hierarquia de memória** ao aceder tamanhos de dados altos, usando o produto de duas matrizes.

Isso será feito através de duas partes distintas: na primeira parte, será analisado o impacto da hierarquia de memória em um único núcleo de processamento, enquanto na segunda parte, serão investigadas implementações paralelas em sistemas multi-core. 

A Performance API (PAPI) será utilizada para coletar indicadores de desempenho relevantes.

**Desenvolvedores:**
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/gabrieltmjr">
        <img src="https://avatars.githubusercontent.com/u/73040950?v=4" width="100px;" alt="Foto Gabriel"/><br>
        <sub>
          <b>Gabriel Machado Jr</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/guiga-sa">
        <img src="https://avatars.githubusercontent.com/u/123979639?v=4" width="100px;" alt="Foto Guilherme"/><br>
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

## Performance Evaluation of a single core
Na primeira parte do projeto, foi requisitado a implementação de diferentes versões do algoritmo de produto de duas matrizes. O algoritmo para multiplicação linha por coluna em C++ e pudemos escolher outra linguagem para usar e implementar o mesmo algoritmo de modo a comparar a execução. O algoritmo linha por linha e por bloco foi feito pelo grupo.

### **1. Multiplicação Linha x Coluna** </br>
Nesta abordagem, o algoritmo implementado multiplica uma linha da primeira matriz por cada coluna da segunda matriz. Esse algoritimo foi implementado em C++ e Python.

Nesta implementação, temos três loops aninhados:

- O loop externo `for (i)` percorre as linhas da matriz resultante `phc`. 
- Para cada linha, o segundo loop `for (j)` percorre as colunas da matriz resultante `phc`. 
- Dentro desses loops, outro loop `for (k)` é utilizado para calcular cada elemento da matriz resultante, que é a soma dos produtos dos elementos correspondentes das linhas da matriz `pha` e das colunas da matriz `phb`. 

A implementação nas duas linguagens segue a mesma lógica, mudando somente a sintaxe das linguagens.

**Implementação em C++:**

```cpp
Time1 = clock();

for(i=0; i<m_ar; i++)
{	
    for(j=0; j<m_br; j++)
    {	
        temp = 0;
        for(k=0; k<m_ar; k++)
        {	
            temp += pha[i*m_ar+k] * phb[k*m_br+j];
        }
        phc[i*m_ar+j]=temp;
    }
}

Time2 = clock();
sprintf(st, "Time: %3.3f seconds\n", (double)(Time2 - Time1) / CLOCKS_PER_SEC);
cout << st;
```
**Implementação em Python:**
```python
Time1 = time.time()

for i in range(m_ar):
    for j in range(m_br):
        temp = 0
        for k in range(m_ar):
            temp += pha[i*m_ar + k] * phb[k*m_br + j]
        phc[i*m_ar + j] = temp

Time2 = time.time()
print(f"Time: {((Time2 - Time1)):.3f} seconds\n")
```

Foram realizados testes onde o tempo de processamento é registrado para matrizes de entrada variando de 600x600 a 3000x3000 elementos, com incrementos de 400 em ambas as dimensões, em ambas as linguagens. 

<sup>Observação: No compilador C++, a flag de otimização -O2 é utilizada para garantir uma compilação otimizada.</sup>

| Tamanho da Matriz | C++ (segundos) | Python (segundos) |
|:------------------:|:---------------:|:-----------------:|
| 600                | 0.192           | 32.082            |
| 1000               | 1.194           | 158.198           |
| 1400               | 3.369           | 439.760           |
| 1800               | 17.918          | 946.323           |
| 2200               | 39.745          | 1731.402          |
| 2600               | 70.490          | x                 |
| 3000               | 118.942         | 3502.117 <sup>*1</sup>      |


<sup>Observação *1: Esse texte foi feito em uma maquina diferente, com um sistema operacional diferente (macOS), devido a indisponibilidade de tempo e maquinas Linux com a Performance API no momento.</sup>

Observa-se que o tempo de processamento aumenta conforme o tamanho da matriz, quando em valores maiores, mesmo que esse almento tenha o mesmo valor, o almento de tempo é maior. Além disso, é notável que a implementação em C++ é significativamente mais rápida do que a implementação em Python, e essa diferença de desempenho aumenta à medida que o tamanho da matriz aumenta. Essas análises fornecem insights valiosos sobre o desempenho relativo das duas linguagens na execução do mesmo algoritmo de multiplicação de matrizes.

### **2. Multiplicação Linha X Linha**
Nesta versão, realizamos a multiplicação de cada linha da primeira matriz por cada linha da segunda matriz. Ela foi implementada em C++ e em Python.

Nesta implementação, são usados três loops aninhados:

- O primeiro loop `for(i)` itera sobre as linhas da matriz resultante `phc` e também representa as linhas da matriz 'pha'. 
- Dentro deste loop, o segundo loop `for(j)` passa pelas linhas da matriz `phb`. 
- Por fim, o terceiro loop `for(k)` itera sobre as linhas da matriz resultante `phc` e é utilizado para calcular cada elemento da matriz resultante `phc`. Dentro deste último loop, cada elemento `phc[i*m_ar + k]` é incrementado pelo produto dos elementos correspondentes das linhas da matriz `pha` e das linhas da matriz `phb`.

**Implementação em C++:**
```cpp
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
```
**Implementação em Python:**
```python
Time1 = time.time()

for i in range(m_ar):
    for j in range(m_ar):
        for k in range(m_br):
            phc[i*m_ar + k] += pha[i*m_ar + k] * phb[j*m_ar + k]

Time2 = time.time()
print(f"Time: {((Time2 - Time1)):.3f} seconds\n")
```

Foram realizados testes onde o tempo de processamento é registrado para matrizes de entrada variando de 600x600 a 3000x3000 elementos, com incrementos de 400 em ambas as dimensões, em ambas as linguagens. 

| Tamanho da Matriz | C++ (segundos) | Python (segundos) |
|:------------------:|:---------------:|:-----------------:|
| 600                | 0.103           | 43.061            |
| 1000               | 0.492           | 199.246           |
| 1400               | 1.637           | 549.308           |
| 1800               | 3.714           | 1148.476          |
| 2200               | 6.972           | 2119.244          |
| 2600               | 12.087          | 4070.254          |
| 3000               | 17.878          | 3309.937 <sup>*1</sup> |

<sup>Observação *1: Este teste foi realizado em uma máquina diferente, com um sistema operacional diferente (macOS), devido à indisponibilidade de tempo e máquinas no momento.</sup>

O que já tinha sido observado na versão linha x coluna, foi também observado nesta versão, com a adição que o algoritimo em C++ se mostrou mais rapido e com menor aumento de tempo conforme a matriz aumentava, ao contrario dos testes em Python que se mostraram mais lentos em comparação a multiplicação linha x coluna (a execução do teste 3000 que ambos foram realizados em outra máquina e nesse caso o segundo algoritmo se provou mais rapido).

Também foram realizados testes com valores maiores variando de 4096x4096 a 10240x10240 elementos, com incrementos de 2048 em ambas as dimensões, somente na liguagem C++.

| Tamanho da Matriz | C (segundos) |
|:------------------:|:------------:|
| 4096               | 48.913       |
| 6144               | 164.480      |
| 8192               | 411.651      |
| 10240              | 792.512      |

Nestes testes podemos ver a real eficiencia do segundo algoritmo em C++ em relação ao primeiro, devido aos primeiros testes se mostrarem com menor tempo que aos dois últimos testes do primeiro algoritmo, e também em relação ao de Python, já que mesmo com numeros maiores o tempo de processamento se mostra inferior a varios testes realizados no algoritmo anterior.

Reforçamos mais uma vez a eficiencia do algoritimo em C++ e em de multiplição linha x linha em relação ao algoritimo de multiplição linha x coluna.

### **3. Multiplicação de Bloco**
Nesta versão, utilizamos o conceito de multiplicação por blocos para otimizar o desempenho da multiplicação de matrizes. Esta versão somente foi desenvolvida em C++.

O algoritmo implementado funciona da seguinte maneira:

- O loop externo `for(ib)` percorre as linhas da matriz resultante `phc` em blocos de tamanho `bkSize` na dimensão das linhas. 
- Dentro deste loop, há outro loop `for(jb)` que percorre as colunas da matriz resultante `phc` em blocos de tamanho `bkSize` na dimensão das colunas. 
- Em seguida, há um terceiro loop `for(kb)` que percorre as linhas da matriz `pha` em blocos de tamanho `bkSize` na dimensão das linhas. 
- Dentro desses três loops, há tres loops aninhados para calcular os elementos de cada bloco da matriz resultante `phc`. Esses loops percorrem as linhas (`for(i)`), as colunas (`for(j)`) e as linhas da matriz `pha` (`for(k)`) dentro dos blocos, limitados pelo tamanho do bloco e as dimensões das matrizes. 
- Dentro do loop mais interno, o elemento `phc[i*m_ar+j]` é calculado como a soma acumulada dos produtos dos elementos correspondentes das linhas da matriz `pha` e das colunas da matriz `phb`.

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

Essa abordagem permite reduzir os acessos à memória e otimizar o uso do cache, resultando em um desempenho melhorado em comparação com os métodos tradicionais de multiplicação de matrizes.

Os testes foram realizados variando o tamanho do bloco (`bkSize`) (128, 256, 512) e e também os tamanhos das matrizes variando de 4096x4096 a 10240x10240 elementos, com incrementos de 2048 em ambas as dimensões.

| Tamanho da Matriz | Tempo bkSize = 128 (em segundos)| Tempo bkSize = 256 (em segundos)| Tempo bkSize = 512 (em segundos)|
|:-----------------:|:-----------------:|:-----------------:|:-----------------:|
| 4096              | 89.187            | 91.182            | 375.748           |
| 6144              | 305.734           | 300.610           | 314.221           |
| 8192              | 723.451           | 3817.102          | x              |
| 10240             | 1422.087          | 1407.182          | x                 |


Estes resultados demonstram que o desempenho varia significativamente com o tamanho do bloco e o tamanho da matriz. Observa-se um aumento no tempo de execução à medida que o tamanho do bloco aumenta. No entanto alguns casos como no tamanho da matriz 6144, o tempo com bkSize = 256 é menor que o tempo com bkSize = 128. Não sabemos explicar o porque deste conceito, mas acreditamos que pode ser por causa da otimização do uso da cache.

Ao comparar estes resultados com o algoritmo de multiplicação linha x linha em relação ao tempo de execução a multiplicação em bloco se mostra menos eficiente. Porém ela poderia ser sim mais eficiente em relação ao algoritmo multiplicação linha x coluna, mas para chegarmos a conclusões mais concretas deveriam ser realizados mais testes.

## Performance evaluation of a multi-core implementation
Na segunda parte do projeto foi requisitado a implementação de versões paralelas da multiplicação de matrizes, especificamente a implementação linha a linha. Duas soluções paralelas distintas serão propostas e analisadas em termos de aceleração (speedup). O objetivo é comparar o desempenho das soluções paralelas em sistemas multi-core e avaliar sua eficácia em relação à implementação sequencial.

A diferença entre os dois algoritmos está na forma como as iterações são paralelizadas:

**Paralelo 1:**
```cpp
Time1 = clock();
#pragma omp parallel for
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
```

Neste algoritmo, a diretiva `#pragma omp parallel for` é utilizada para paralelizar o loop externo `for(i=0; i<m_ar; i++)`. Isso significa que cada iteração desse loop é distribuída entre várias threads para serem executadas em paralelo. No entanto, as iterações internas dos loops `j` e `k` ainda são executadas sequencialmente dentro de cada thread.

**Paralelo 2:**
```cpp
Time1 = clock();
#pragma omp parallel
for(i=0; i<m_ar; i++)
{
    for(j=0; j<m_ar; j++)
    {
        #pragma omp for
        for(k=0; k<m_br; k++)
        {   
            phc[i*m_ar+k] += pha[i*m_ar+k] * phb[j*m_ar+k];
        }
    }
}
Time2 = clock();
```
Neste segundo algoritmo, a diretiva `#pragma omp parallel` é usada para criar um grupo de threads, e a diretiva `#pragma omp for` é aplicada no loop interno `for(k=0; k<m_br; k++)`. Isso significa que cada iteração do loop interno é distribuída entre as threads disponíveis no grupo, permitindo que diferentes threads processem diferentes partes do cálculo em paralelo.

Em suma, enquanto o primeiro algoritmo paraleliza apenas o loop externo, distribuindo as iterações entre threads separadas, o segundo algoritmo paraleliza também o loop interno, permitindo que partes específicas do cálculo sejam executadas simultaneamente em diferentes threads. A escolha entre os dois depende das características específicas do problema e do hardware disponível.

Foram realizados testes nos dois algoritimos onde o tempo de processamento é registrado para matrizes de entrada variando de 600x600 a 3000x3000 elementos, com incrementos de 400 em ambas as dimensões.

| Tamanho da Matriz | Paralelo 1 (segundos) | Paralelo 2 (segundos) | Sequencial (segundos) |
|:------------------:|:---------------:|:-----------------:|:-----------------:|
| 4096               | 27.493          | 64.160            | 130.982           |
| 6144               | 99.528          | 145.206           | 486.125           |
| 8192               | 232.900         | x                 | 1092.793          |
| 10240              | 448.963         | 440.569           | 2077.101          |

<sub>Observação: Estes testes foram realizados em uma máquina diferente, com um sistema operacional diferente (macOS), e sem a flag de otimização -O2 devido à indisponibilidade de tempo e máquinas no momento. Por isso mesmo que também refizemos os testes da multiplicação linha x linha sem paramerilização sem a flag, para assim ser possivel comprarar os testes de maneira mais fidedigna.</sup>

Com essas informações podemos calcular o speedup utilizando a formula: `speedup = tempo de execução sequencial / tempo de execução paralela`

| Tamanho da Matriz | Paralelo 1 (Speedup) | Paralelo 2 (Speedup) |
|:------------------:|:-----------------:|:-----------------:|
| 4096               | 4.764             | 2.041             |
| 6144               | 4.884             | 3.347             |
| 8192               | 4.692             | x                 |
| 10240              | 4.626             | 4.714             |

Assim observamos que os testes paralelos podem até ser mais rápidos que os sequenciais, porém as vezes podem ser mais arriscados, tendo visto que nos deparamos com vários erros onde dois threads tentam acessar uma mesma região de memória no algoritmo paralelo 2.

## Conclusão do trabalho

Com esse trabalho concluímos que diferentes linguagens e algoritmos podem desenvolver diferentes performances em até diferentes sistemas operacionais, por isso devemos fazer testes para buscar aqueles que se encaixem nas necessidade do usuário.

Em nossos testes observamos uma maior velocidade de complicação em sistemas multi-core a single-core, porem temos que ter muito cuidado ao criar sistemas assim para que duas threads não acabem por tentar acertar uma mesma região de memória, ocasionando em um erro. Embora sistemas multi-core sejam mais rápidos eles devem ser criados com cautela e tem mais riscos.

Outra observação foi que pudemos observar que as versões em C++ se mostraram mais rápidas ao compilar que as versões em Python, porém diferentes algoritmos e sistemas operacionais podem mostrar diferentes comportamentos nas duas linguagens, vendo que certos testes se mostraram se manter uma melhor velocidade em Python quando foi trocado de sistemas operacionais. Para entender mais sobre isso é necessário fazer mais testes em outros sistemas.
 
No geral, reconhecemos a importância dos Engenheiros Informáticos conhecerem estas situações de modo a conseguirem trabalhar em problemas de otimização e desempenho de algoritmos em máquinas com single e/ou multi-core.

