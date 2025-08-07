import streamlit as st
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv
import os


# Caminho absoluto do diretório raiz do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # sobe um nível (sai da pasta /web)

# Carrega as variáveis de ambiente do .env localizado na raiz
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Monta caminho absoluto do CSV
data_path = os.path.join(BASE_DIR, os.getenv("DATA_PATH", "scraping/emissoes.csv"))

# Carrega o CSV
df = pd.read_csv(data_path)

# Converter valores para bilhões
df["Valor"] = df["Valor"] / 1e9

# Configuração da página
st.set_page_config(page_title="Dashboard CRA", layout="wide")
st.title("📊 Dashboard CRA - Certificados de Recebíveis do Agronegócio")

# 1. Volume total por ano
st.markdown("## 1. Volume total de CRA emitido por ano")
df_ano = df.groupby("Ano")["Valor"].sum().reset_index()
fig_ano = px.bar(df_ano, x="Ano", y="Valor", text_auto=".1f", labels={"Valor": "R$ bilhões"})
fig_ano.update_layout(xaxis=dict(tickmode='linear', dtick=1, tickangle=-45))
st.plotly_chart(fig_ano, use_container_width=True)

# 2. Top 10 empresas por número de emissões
st.markdown("## 2. Top 10 empresas com maior número de emissões")
top_empresas = df["Empresa (Operação)"].value_counts().head(10).reset_index()
top_empresas.columns = ["Empresa (Operação)", "Número de Emissões"]
fig_top_emp = px.bar(top_empresas, x="Número de Emissões", y="Empresa (Operação)",
                     orientation="h", )
fig_top_emp.update_layout(yaxis=dict(tickfont=dict(size=12)))
st.plotly_chart(fig_top_emp, use_container_width=True)

# 3. Top 10 operações com maior valor emitido
st.markdown("## 3. Top 10 operações com maior valor total emitido")
top_valor = df.groupby("Empresa (Operação)")["Valor"].sum().nlargest(10).reset_index()
fig_top_valor = px.bar(top_valor, x="Valor", y="Empresa (Operação)", orientation="h",
                       text_auto=".1f", labels={"Valor": "R$ bilhões"},
                       )
fig_top_valor.update_layout(yaxis=dict(tickfont=dict(size=12)))
st.plotly_chart(fig_top_valor, use_container_width=True)

import streamlit as st
import plotly.express as px
import pandas as pd

st.markdown("## 4. Evolução das emissões - Empresas selecionadas (Gráfico de Barras)")

# Supondo que seu DataFrame se chame df
empresas_disponiveis = df["Empresa (Operação)"].unique().tolist()

# Top 5 empresas com maior valor total emitido
top5_empresas = df.groupby("Empresa (Operação)")["Valor"].sum().nlargest(5).index.tolist()

# Seleção de empresas
empresas_selecionadas = st.multiselect(
    "Selecione uma ou mais empresas para visualizar a evolução das emissões:",
    options=empresas_disponiveis,
    default=top5_empresas
)

# Botão para modo de visualização
modo_grafico = st.radio(
    "Modo de exibição do gráfico:",
    ["Agrupado", "Empilhado"],
    horizontal=True
)

# Define o modo de barra
barmode = "group" if modo_grafico == "Agrupado" else "stack"

# Filtrar os dados
df_filtrado = df[df["Empresa (Operação)"].isin(empresas_selecionadas)]
df_grouped = df_filtrado.groupby(["Ano", "Empresa (Operação)"])["Valor"].sum().reset_index()

# Gráfico
fig_barras = px.bar(
    df_grouped,
    x="Ano",
    y="Valor",
    color="Empresa (Operação)",
    barmode=barmode,
    hover_data={"Valor": ":.1f"},
    labels={"Valor": "R$ bilhões"},
    title="Evolução das emissões de CRA por empresa"
)

# Personalizações visuais
fig_barras.update_traces(
    text=None,
    marker_line_width=0.5,
    marker_line_color='gray'
)

fig_barras.update_layout(
    xaxis=dict(tickmode='linear', dtick=1),
    bargap=0.1,
    height=500,
    legend_title_text="Empresa",
)

# Exibir no Streamlit
st.plotly_chart(fig_barras, use_container_width=True)
