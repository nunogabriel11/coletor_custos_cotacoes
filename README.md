# Otimização de processos de transporte 
Desenvolvimento de um modelo de apoio à decisão capaz de , a partir da introdução da informação referente á descrição e localizações de uma mercadoria, identificar o respetivo documento portador desse custo e retribuindo o custo.<br /><br />

O âmbito deste projeto centrou-se na criação de um modelo de apoio à decisão (MAD), desenvolvido em python, com o objetivo de automatizar os processos de obtenção e fornecimento de cotações a clientes de transportes terrestres nacionais da empresa X.
Deste modo, a atual atividade manual deste processo, realizada por todos os departamentos da empresa, engloba um vasto conjunto de implicações capazes de afetar negativamente a obtenção e fornecimento das cotações, como por exemplo:
- Facilidade de erro de cálculo do peso taxável (cw) e/ou peso por metro de estrado (ldm);
- Necessidade de selecionar uma das 60 tabelas Excel existentes para obtenção do valor para cotação;
- Seleção errada do fator de dimensionalidade a considerar para o cálculo do cw e ldm;
- Erro humano;
- O tempo gasto em cada consulta é longo e dependente da experiência de cada colaborador;
- Necessidade de verificação das consultas realizadas;
- Incapacidade de realização das consultas por colaboradores inexperientes ou sem conhecimento para obtenção do cw e ldm.<br />

Sendo assim, aquando da receção de um pedido de cotação por parte de um cliente, a informação necessária para esta centra-se nas localizações de carga e descarga da mercadoria, características e dimensões da mesma, como também se esta poderá ser sobreposta por outras (designada de carga sobreponível ou não sobreponível).<br />
Como já referido, todos os setores necessitam de recorrer a determinadas tabelas Excel (desenvolvidas pela empresa X) para obter o custo que o cliente irá ter com determinado serviço prestado, em que atualmente é realizada manualmente. Para essa consulta, inicialmente cada departamento necessita de obter, a informação do cliente, as características da mercadoria, nomeadamente, comprimento, largura, altura, diâmetro (caso necessário) e quantidade, código postal de origem e destino, se a carga é sobreponível ou não, como também se o transporte da mercadoria irá ser realizado de ou para os armazéns da empresa, ou entre duas localizações que não os seus armazéns (tópicos obtidos com a informação mencionada no parágrafo anterior).<br />
De forma sucinta, o funcionamento do MAD requer um dado conjunto de inputs para o seu funcionamento de maneira a fornecer os outputs necessários para análise e conclusões pretendidas. Deste modo, os requisitos iniciais necessários centra-se nos documentos Excel (fornecidos pela empresa X) que englobam os valores (€) para as cotações a fornecer a cada cliente, a informação da mercadoria a transportar (peso, dimensão, localizações, entre outros), como também a informação necessária para identificação do cliente.<br />
Por outro lado, após a execução do MAD é retribuído como output o preço a fornecer ao cliente pela cotação requerida, o Dataset utilizado que expõe a o nome e tabela utilizada do cliente, como também a criação ou atualização de um ficheiro Excel “tempos.xlsx” incorporando toda a informação necessária relativa a essa consulta a partir do MAD (tempo de consulta, data de realização da consulta, origem/destino da carga, etc).<br />
Assim sendo, a seguinte figura retrata, esquematicamente, o ambiente necessário para o execução do MAD.

<p align="center">
  <img src="https://github.com/nunogabriel11/coletor_custos_cotacoes/blob/main/imgs/diagram.png?raw=true" width="400" />
</p><br />

<p align="center">
<i>Figura 1: Imagem ilustrativa dos inputs e outputs referentes ao MAD</i>
</p><br />

## Demonstração do uso do “artifact”
Aquando da obtenção de toda a informação necessária da mercadoria por parte do cliente (descrição e localizações de transporte), o utilizador encontra-se apto para recorrer ao “artifact” de modo a, então, realizar a consulta para obtenção do custo a fornecer ao cliente.<br />
Partindo agora para a análise visual da interface do programa do ponto de vista do utilizador, com a iniciação da aplicação, o utilizador depara-se com o primeiro menu (menu principal), em que escolherá uma das primeiras quatro opções, caso pretenda selecionar um determinado setor, a opções 5 em caso de necessitar de encerrar o programa, como se pode observar na seguinte imagem:<br />


<p align="center">
  <img src="https://github.com/nunogabriel11/coletor_custos_cotacoes/blob/main/imgs/menu1.png?raw=true" width="400" />
</p><br />

<p align="center">
<i>Figura 2: Imagem ilustrativa do menu principal do programa</i>
</p><br />






Posteriormente, caso o utilizador selecione alguma das opções associadas a cada departamento, é-lhe mostrado um novo menu relativo ao setor selecionado, na qual terá, novamente, de selecionar uma das opções (com exceção da última opção) associadas a cada cliente, estando a última opção reservada para a possibilidade de retroceder para o menu principal, por exemplo, em caso de seleção errada do departamento pretendido.<br />




<p align="center">
  <img src="https://github.com/nunogabriel11/coletor_custos_cotacoes/blob/main/imgs/menu2.png?raw=true" width="400" />
</p><br />

<p align="center">
<i>Figura 3: Imagem ilustrativa do “Menu Distribuição” (opção 1) e seus respetivos clientes</i>
</p><br />





Uma vez selecionado o cliente desejado, é mostrado ao utilizador uma pequena frase a informar o cliente selecionado, como também lhe é pedida toda a informação necessária para o consulta e obtenção do custo final do cliente.<br />
A seguinte imagem retrata um exemplo de possibilidade de sobreposição da mercadoria, o que significa que não irão ser pedidas ao utilizador informação referente ao caso de não sobreposição da carga (fator de dimensionalidade para ldm, , entre outros).

<p align="center">
  <img src="https://github.com/nunogabriel11/coletor_custos_cotacoes/blob/main/imgs/menu3.png?raw=true" width="400" />
</p><br />

<p align="center">
<i>Figura 4: Imagem ilustrativa de um exemplo de informação de carga introduzida, com possibilidade de sobreposição, após seleção do respetivo cliente</i>
</p><br />

Após a introdução de toda a informação necessária da mercadoria é fornecido, ao utilizador, o peso considerado para essa consulta, tal como a tabela selecionada e o custo que o cliente terá relativo à movimentação desta sua mercadoria entre as duas localizações pretendidas.<br />



<p align="center">
  <img src="https://github.com/nunogabriel11/coletor_custos_cotacoes/blob/main/imgs/menu4.png?raw=true" width="400" />
</p><br />

<p align="center">
<i>Figura 5: Imagem ilustrativa do custo obtido do cliente, tendo por base a informação da figura 17</i>
</p><br />




Já para o caso de consideração de a carga ser não sobreponível, o procedimento, até ao ponto de informação da carga, não sofre alterações, apenas existindo a necessidade de obter resposta, por parte do utilizador, a algumas variáveis de entrada adicionais, nomeadamente em relação à largura do veículo de transporte e ao número de paletes a considerar.<br />
É de realçar que este caso específico acontece exclusivamente quando a resposta de possibilidade de sobreposição de carga é “não”. <br />


<p align="center">
  <img src="https://github.com/nunogabriel11/coletor_custos_cotacoes/blob/main/imgs/menu5.png?raw=true" width="400" />
</p><br />

<p align="center">
<i>Figura 6: Imagem ilustrativa de um exemplo de informação de carga introduzida, com impossibilidade de sobreposição, e obtenção do custo, após seleção do respetivo cliente</i>
</p><br />



## Formulário de consultas manuais
A relevância de armazenar as cronometragens de cada consulta realizada com o MAD centra-se na contribuição da possível comparação e análise com os tempos de cada consulta realizada manualmente.<br />
Desta forma, foi realizado um inquérito com auxílio do Google Forms em que cada colaborador responderá a um pequeno grupo de questões focadas no seu setor, nome (ocultado por anonimato), se costuma consultar as tabelas de custos da Distribuição, tempo de experiência, tempos de consultas para mercadorias sobreponíveis e não sobreponíveis, como também obter a razão de não utilização das tabelas.<br />

## Análise de Cenários e Resultados Obtidos
As poupanças monetárias e temporais obtidas, a partir do MAD e do formulário, constituem resultados bastante positivos, para ambos, pelo que foi decidido ir mais longe de forma a ser possível obter uma análise dos resultados mais preciso e com variações. <br />  
Desta forma, uma utilização de análise de cenários irá permitir obter uma compreensão mais abrangente dos resultados e conclusões como também obter uma perspetiva das possibilidades futuras envolvidas no comportamento desses mesmos resultados.<br />
Por esta razão, decidiu-se proceder à realização de 3 distintos cenários caracterizados por uma perspetiva pessimista, realista e otimista.
De um modo geral, os resultados obtidos foram bastante satisfatórios com a análise de cenários. O cenário pessimista apresentou resultados menos favorecedores contribuindo com poupanças médias anuais de 6 166,84€ e uma eficiência média temporal de 86,50%, pelo que o cenário otimista demonstrou uma performance substancialmente superior obtendo uma poupança média de 8 166,49€ e uma Eficiência temporal média de 90,66%.

## Conclusão
Em síntese, apesar das pequenas limitações existentes, a precisão dos resultados por parte do programa comprovam a fiabilidade do seu funcionamento e obtenção de resultados. Por sua vez, a análise de cenários demonstrou poupanças financeiras anuais significativas para todos os casos específicos.<br />
Deste modo, a constituição deste projeto foi bem conseguida podendo-se concluir que a implementação de Transformação Digital na otimização dos processos de transporte, mais concretamente, na automatização do processo de realização de consultas de custos para clientes, é financeiramente vantajosa, para a organização, como também melhora significativamente a eficiência temporal quando comparada com as consultas manuais, pelo que a diminuição das limitações impostas, promoveria a obtenção de resultados financeiramente melhores e com maior precisão.
