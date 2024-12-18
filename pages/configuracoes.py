import streamlit as st
import pandas as pd
from pymongo import MongoClient

# Configuração do MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["nome_do_banco"]  # Substitua pelo nome do seu banco de dados
collection = db["nome_da_colecao"]  # Substitua pelo nome da sua coleção

st.title("Configurações")

# Carregar arquivo Excel
uploaded_file = st.file_uploader("Escolha um arquivo Excel", type=["xlsx"])

if uploaded_file is not None:
    # Ler o arquivo Excel
    df = pd.read_excel(uploaded_file)

    # Inserir dados no MongoDB
    for index, row in df.iterrows():
        data = row.to_dict()
        collection.insert_one(data)

    st.success("Dados inseridos com sucesso no MongoDB!")
