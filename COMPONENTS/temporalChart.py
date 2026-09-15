import streamlit as st


def temporalChart(df_filtrado):

    # Soma as vendas de cada dia
    df_grafico = (
        df_filtrado
        .groupby("OrderDate")["Sales"]
        .sum()
        .reset_index()
        .sort_values("OrderDate")
    )

    st.line_chart(
        df_grafico,
        x="OrderDate",
        y="Sales"
    )