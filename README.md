### Projeto - Análise e Modelagemd e Série Temporal

Neste projeto será efetuado a ingestão dos valores de uma ação da bolsa de valores, como o seu preço de abertura, fechamento e o volume. Para tal, usaremos um script de consulta via API (ingestor_api.py). Posteriormente será efetuado uma análise e aplicação de técnicas de ciência de dados para a modelagem de um modelo de série temporal e finalmente iremos aplicar esses modelos desenvolvidos para prever o valor da ação para o próximo dia.

Esse projeto foi desenvolvido dia 30-04-2024, portando ainda não temos o valor de fechamento da ação. Então podemos definir que o objetivo principal será prever o valor de fechamento para o dia 30 e posteriormente (dia 01-05-2024) comparar as nossas previsões com o valor real retornado pela API.

### Execução

99% do projeto está contido em um arquivo Jupyter e o nosso ingestor em um arquivo .py.

Para instalar as dependências, basta fazer a instalaçã do requirements.txt disponível no git

```pip install -r requirements.txt```

Como se trata de um projeto acadêmico, o noteboook "models_predict.ipynb" está com todas as etapas comentadas para facilitar o entendimento.