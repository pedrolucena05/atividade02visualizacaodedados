import sys
import streamlit as st
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from COMPONENTS.products import products
from COMPONENTS.sideBar import sideBar
from COMPONENTS.temporalChart import temporalChart
from COMPONENTS.temporalMerged import temporalMerged
from COMPONENTS.pizzaCity import pieVendasCidade
from COMPONENTS.pizzaProduct import pieProdutos
from PROCESSES.filterGraphicsRange import filterGraphicsRange
from PROCESSES.loadDataframe import loadData, loadProducts

st.set_page_config(
    page_title="Dashboard",
    layout="wide"
)

if "unir_resultados" not in st.session_state:
    st.session_state.unir_resultados = False

if "qtd_graficos" not in st.session_state:
    st.session_state.qtd_graficos = 1

# Carrega os dados dos datasets .npz
df = loadData() # dataset principal
dfProducts = loadProducts() # dataset secundario para a tabela produtos

# Converte o tipo data para um tipo compativel com o python
df["OrderDate"] = pd.to_datetime(df["OrderDate"])

# Gera o Side Bar e obtem resultados
unir_resultados, data_inicio, data_fim, produtos_selecionados = sideBar(df)

# substitui o valor de nome do produto para id do produto
produtos_selecionados = [products[item] for item in produtos_selecionados]


st.subheader("Vendas ao longo do tempo")

periodos = []
for i in range(len(data_inicio)):

    periodos.append(f"(de {data_inicio[i].strftime('%d/%m/%Y')} à {data_fim[i].strftime('%d/%m/%Y')})")

st.write(", ".join(periodos))


unir = []

dfCity = []
dfProd = []

for i in range(len(data_inicio)):

    df_filtrado = filterGraphicsRange(
        df,
        data_inicio[i],
        data_fim[i],
        produtos_selecionados
    )

    unir.append(df_filtrado)

    df_vendas_cidade = (df_filtrado.groupby("City").size().reset_index(name="QuantidadeVendas").sort_values("QuantidadeVendas", ascending=False))
    dfCity.append(df_vendas_cidade)

    df_produtos = (df_filtrado.groupby("ProductName").size().reset_index(name="Quantidade").sort_values("Quantidade", ascending=False))
    dfProd.append(df_produtos)

if unir_resultados:

    temporalMerged(unir)

else:

    for df_filtrado in unir:
        temporalChart(df_filtrado)


col1, col2 = st.columns(2)

cont = 1
with col1:
    for df in dfCity:
        pieVendasCidade(df,key=f"pizza_cidade_{cont}")
        cont += 1

cont = 1
with col2:
    for df in dfProd:
        pieProdutos(df, key=f"pizza_produtos_{cont}")
        cont += 1

st.subheader("Produtos:")
st.dataframe(dfProducts)

