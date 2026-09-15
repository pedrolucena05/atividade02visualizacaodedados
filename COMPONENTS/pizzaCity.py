import plotly.express as px
import streamlit as st


def pieVendasCidade(df_vendas_cidade, key):

    fig = px.pie(
        df_vendas_cidade,
        names="City",
        values="QuantidadeVendas",
        title="Quantidade de vendas por cidade"
    )

    st.plotly_chart(
        fig,
        width="stretch",
        key=key
    )