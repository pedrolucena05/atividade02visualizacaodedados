import numpy as np
import pandas as pd
import kagglehub
from pathlib import Path

from kagglehub import KaggleDatasetAdapter


df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "erfan4524/e-commerce-sales-data-analysis-and-eda",
    "clean_final_data.csv"
)

df["OrderDate"] = pd.to_datetime(df["OrderDate"])

ROOT = Path(__file__).resolve().parent.parent
DATASETS = ROOT / "DATASETS"


dados = {}

for coluna in df.columns:

    if df[coluna].dtype == "object":
        dados[coluna] = df[coluna].fillna("").astype(str).to_numpy()

    else:
        dados[coluna] = df[coluna].to_numpy()


status = dados["Status"]

mascara = ~np.isin(status, ["Cancelled", "Returned"])

for coluna in dados:
    dados[coluna] = dados[coluna][mascara]


ordem = np.argsort(dados["OrderDate"])

for coluna in dados:
    dados[coluna] = dados[coluna][ordem]


np.savez_compressed(DATASETS / "dataframe.npz", **dados)

df_numpy = pd.DataFrame(dados)

print(df_numpy.iloc[:, :9].head())
print(df_numpy.iloc[:, -8:].head())

print(
    df[["ProductName", "ProductID"]]
    .drop_duplicates()
)


product_id = dados["ProductID"]
product_name = dados["ProductName"]

sales = dados["Sales"].astype(float)
quantity = dados["Quantity"].astype(float)


# Evita divisão por zero
mascara_quantity = quantity > 0

product_id_valido = product_id[mascara_quantity]
product_name_valido = product_name[mascara_quantity]

sales_valido = sales[mascara_quantity]
quantity_valida = quantity[mascara_quantity]


# Calcula preço unitário
preco_unitario = sales_valido / quantity_valida

# IDENTIFICA OS PRODUTOS ÚNICOS
products_ids, primeira_posicao, grupo = np.unique(
    product_id_valido,
    return_index=True,
    return_inverse=True
)


# Nome correspondente a cada ProductID
products_names = product_name_valido[primeira_posicao]



# QUANTIDADE TOTAL VENDIDA POR PRODUTO
products_quantity = np.bincount(
    grupo,
    weights=quantity_valida
)



# PREÇO MÍNIMO
products_min_price = np.full(
    len(products_ids),
    np.inf
)

np.minimum.at(
    products_min_price,
    grupo,
    preco_unitario
)



# PREÇO MÁXIMO
products_max_price = np.full(
    len(products_ids),
    -np.inf
)

np.maximum.at(
    products_max_price,
    grupo,
    preco_unitario
)



# SALVA PRODUCTS.NPZ
np.savez_compressed(
    DATASETS / 'products.npz',
    ProductID=products_ids,
    ProductName=products_names,
    Quantity=products_quantity,
    MinPrice=products_min_price,
    MaxPrice=products_max_price
)