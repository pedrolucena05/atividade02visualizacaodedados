import streamlit as st


def filterGraphicsRange(df, data_inicio, data_fim, produtos_selecionados):

    if data_inicio <= data_fim:

        df_filtrado = df[(df["OrderDate"].dt.date >= data_inicio) & (df["OrderDate"].dt.date <= data_fim) & (df["ProductID"].isin(produtos_selecionados))]

    else:

        st.error("A data inicial não pode ser maior que a data final.")
        df_filtrado = df.iloc[0:0]

    return df_filtrado