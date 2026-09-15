import numpy as np
import pandas as pd
import streamlit as st
import sys

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))
DATASETS = ROOT / "DATASETS"


@st.cache_data
def loadData():

    arquivo = np.load(DATASETS / "dataframe.npz", allow_pickle=True)

    dados = {coluna: arquivo[coluna] for coluna in arquivo.files}

    df = pd.DataFrame(dados)

    # Garante que a coluna volte a ser datetime
    df["OrderDate"] = pd.to_datetime(df["OrderDate"])

    return df

@st.cache_data
def loadProducts():

    arquivo = np.load(DATASETS / "products.npz", allow_pickle=True)

    dados = {
        coluna: arquivo[coluna]
        for coluna in arquivo.files
    }

    products = pd.DataFrame(dados)

    return products
