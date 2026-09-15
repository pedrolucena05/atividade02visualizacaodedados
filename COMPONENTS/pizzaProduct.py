import plotly.express as px
import streamlit as st

import plotly.express as px
import streamlit as st


def pieProdutos(df_produtos, key):

    fig = px.pie(
        df_produtos,
        names="ProductName",
        values="Quantidade",
        title="Quantidade de produtos vendidos"
    )

    st.plotly_chart(
        fig,
        width="stretch",
        key=key
    )