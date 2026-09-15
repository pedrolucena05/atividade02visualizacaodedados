import streamlit as st
import pandas as pd


def temporalMerged(unir):

    graficos = []

    for i, df_filtrado in enumerate(unir):

        if df_filtrado.empty:
            continue

        # Agrupa as vendas por dia
        df_grafico = (
            df_filtrado
            .groupby("OrderDate")["Sales"]
            .sum()
            .sort_index()
            .reset_index(drop=True)
        )

        # Nome da linha
        df_grafico.name = f"Período {i + 1}"

        graficos.append(df_grafico)


    if len(graficos) == 0:
        st.warning("Não existem dados para exibir.")
        return


    # Junta pela posição, e não pela data
    df_merged = pd.concat(
        graficos,
        axis=1
    )


    # Cria eixo relativo
    df_merged.insert(
        0,
        "Dia",
        range(1, len(df_merged) + 1)
    )


    st.line_chart(
        df_merged,
        x="Dia",
        y=[
            coluna
            for coluna in df_merged.columns
            if coluna != "Dia"
        ],
        width="stretch",
        height=550
    )