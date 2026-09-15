import streamlit as st


def sideBar(df):

    if "unir_resultados" not in st.session_state:
        st.session_state.unir_resultados = False

    if "qtd_graficos" not in st.session_state:
        st.session_state.qtd_graficos = 1

    def adicionarGrafico():
        st.session_state.qtd_graficos += 1

    def removerGrafico():

        if st.session_state.qtd_graficos > 1:

            ultimo = st.session_state.qtd_graficos - 1

            st.session_state.pop(
                f"data_inicio_{ultimo}",
                None
            )

            st.session_state.pop(
                f"data_fim_{ultimo}",
                None
            )

            st.session_state.qtd_graficos -= 1

    with st.sidebar:

        st.header("Período:")

        unir_resultados = st.checkbox(
            "Unir resultados",
            value=False,
            key="unir_resultados"
        )


        # Listas que armazenarão as datas
        data_inicio = []
        data_fim = []


        # Cria os calendários de cada gráfico
        for i in range(st.session_state.qtd_graficos):

            #st.subheader(f"Gráfico {i + 1}")

            inicio = st.date_input(
                "Data inicial:",
                value=df["OrderDate"].min().date(),
                format="DD/MM/YYYY",
                key=f"data_inicio_{i}"
            )

            fim = st.date_input(
                "Data final:",
                value=df["OrderDate"].max().date(),
                format="DD/MM/YYYY",
                key=f"data_fim_{i}"
            )

            data_inicio.append(inicio)
            data_fim.append(fim)


        col1, col2 = st.columns(2)

        with col1:

            st.button(
                "⊕",
                use_container_width=True,
                on_click=adicionarGrafico
            )


        with col2:

            st.button(
                "⊖",
                use_container_width=True,
                disabled=st.session_state.qtd_graficos <= 1,
                on_click=removerGrafico
            )


        # --------------------------
        # PRODUTOS
        # --------------------------

        st.header("Produtos:")

        produtos = (
            df["ProductName"]
            .dropna()
            .sort_values()
            .unique()
            .tolist()
        )

        produtos_selecionados = st.multiselect(
            "Produtos:",
            options=produtos,
            default=[]
        )


    return (
        st.session_state.unir_resultados,
        data_inicio,
        data_fim,
        produtos_selecionados
    )