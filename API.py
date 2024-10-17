import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

#sidebar

st.sidebar.header("Filtros")

#Elementos de textos:

st.title("Isso é um titulo :blue[Título] :sunglasses:")
st.header("Isso aqui é um cabeçalho", divider = 'gray')
st.subheader("Isso aqui é um sub-cabeçalho", divider=True)
st.text("Isso aqui é um texto")

#Elementos de dados:
df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(df)

#Elementos de Seleção:

#CheckBox
selecao1 = st.checkbox("Mercado")

if selecao1:
    st.write(":D")

#Cor
cor = st.color_picker("Selecione a cor", "#00f900")
st.write("cor selecionada", cor)

#Multiselect
opcoes = st.multiselect(
    "Selecione as opções",
    ["green", "Yellow", "Red", "Blue"]
)
st.write("Sua seleção", opcoes)

#Radio
genero = st.radio(
    "Qual o seu estilo de filmes favorito?",
    [":rainbow[comedia]", "***Drama***", "Documentario :movie_camera:"],
    captions=[
        "Você é amostradinho."
        "Vai chorar manda audio."
        "Você é do rock?"
    ],
)

if genero == ":rainbow[Comedia]":
    st.write("Você selecionou comedia")
else:
    st.write("Você não selecionou comedia.")

#SelectBox
option = st.selectbox(
    "Qual o seu melhor contato?",
    ("Email", "Telefone", "Celular")
)

st.write("Você selecionou:", option)

#Slider

start_color, end_color = st.select_slider(
    "Selecione o range das cores",
    options=[
        "red",
        "orange",
        "yallow",
        "green",
        "blue",
        "indigo",
        "violet",
    ],
    value=("red", "blue"),
)

#Toggle
on = st.toggle("Activate feature")

if on:
    st.write("Feature activated!")













































