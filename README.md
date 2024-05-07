# Projeto - Análise e Modelagem de Modelo Série Temporal

## Objetivo  

Neste projeto será efetuado a ingestão dos valores de uma ação da bolsa de valores, como o seu preço de abertura, fechamento e o volume. Para tal, usaremos um script de consulta via API (ingestor_api.py). Posteriormente será efetuado uma análise e aplicação de técnicas de ciência de dados para a modelagem de um modelo de série temporal e finalmente iremos aplicar esses modelos desenvolvidos para prever o valor da ação para o próximo dia.  

## Dataset  

O dataset utilizado neste projeto é composto pelas informações diárias dos valores de uma ação da bolsa de valores. Neste caso,será utilzado a ação (PBR), ação da Petrobrás.  

O algoritmo "ingestor_api.py" retorna um dataframe com os seguintes valores  

Data | Open | High | Low | Close | Volume  

Onde:
    Data: Data da ocorrência;  
    Open: Valor de abertura da ação no dia;  
    High: Valor mais alto atingido durante o dia;  
    Low: Valor mais baixo atingido durante o dia;  
    Close: Valor de fechamento, ao final do dia;  
    Volume: Volume de ações comercializadas.  


## Resultados Esperados  

Esse projeto foi desenvolvido dia 30-04-2024, portando foram utilizadas informações até o dia 29-04-2024. De acordo com o objetivo desse projeto, podemos definir um objetivo específico, que será a previsão do valor de fechamento da ação (PBR) para o dia 30-04-2022.  

Após essa previsão, iremos comparar com o resultado real de fechamento da ação, no dia posterior, ou seja 01-05-2024, onde já teremos o resultado via API. Tal comparação nos permitiŕa comparar o desempenho dos modelos desenvolvidos e verificar se os resultados de treino e teste reflitirão em um desempenho real em produção.  


## Execução do Projeto  

O desenvolvimento principal do projeto foi executado em um Jupyter Notebook, contemplando todas as análises, comentários e definições.  

Para instalar as dependências, basta fazer a instalaçã do requirements.txt disponível no git em um ambiente virtual;  

```pip install -r requirements.txt```

Como se trata de um projeto acadêmico, pode-se ser encontrado inconsistências ou pontos a serem melhorados, portanto deixo abaixo meu e-mail para possíveis contribuições.
  
```andradejr95@gmail.com```