# Dashboard de Análise de Vendas

Projeto de análise de dados de vendas desenvolvido para a disciplina .

O usuário pode selecionar o período que deseja analisar, escolher produtos específicos e comparar dois ou mais períodos.

## Funcionalidades

* Filtro por data inicial e final;
* Filtro por produtos;
* Gráfico temporal de vendas;
* Comparação entre múltiplos períodos;
* Gráfico de vendas por cidade;
* Gráfico de quantidade de produtos vendidos.

## Controles

### ⊕ Adicionar período

Adiciona um novo intervalo de datas para comparação.

### ⊖ Remover período

Remove o último período adicionado.

### Unir resultados

Sobrepõe os gráficos dos diferentes períodos em uma única visualização.

Os períodos são alinhados pelo início da análise, permitindo comparar o comportamento das vendas independentemente da data real.

Para melhor visualização, recomenda-se utilizar essa opção com períodos de até aproximadamente **3 meses**.

## Executando com Docker

É necessário ter **Docker** e **GNU Make** instalados.

Criar a imagem:

```bash
make build
```

Iniciar o container:

```bash
make run
```

Abrir o dashboard:

```bash
make show
```

Ou executar tudo de uma vez:

```bash
make start
```

O dashboard estará disponível em:

```text
http://localhost:8501
```

Para parar:

```bash
make stop
```

## Docker

O projeto é executado dentro de um container Docker. Durante o build, o `initializer.py` processa os dados e gera os arquivos utilizados pelo Streamlit.

O dashboard é iniciado com:

```bash
streamlit run MAIN/dashboard.py
```

## Tecnologias

* Python
* Pandas
* NumPy
* Streamlit
* Plotly
* Docker
* GNU Make
