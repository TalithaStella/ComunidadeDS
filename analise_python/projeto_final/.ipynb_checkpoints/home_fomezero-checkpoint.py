# =====================
# BIBLIOTECAS NECESSÁRIAS
# =====================

import pandas as pd
import numpy as np

import plotly.express as px
import inflection
import streamlit as st
from PIL import Image 
# import plotly.graph_objects as go
# import folium
# from haversine import haversine

st.set_page_config( page_title='Fome Zero', layout='wide')

# ====================================================================================
# FUNÇÕES
# ====================================================================================

df = pd.read_csv('zomato.csv')

# Colocando o nome dos países pelo código
countries = {
    1: "Índia",
    14: "Austrália",
    30: "Brazil", 
    37: "Canadá", 
    94: "Indonesia", 
    148: "New Zeland", 
    162: "Philippines", 
    166: "Qatar", 
    184: "Singapure", 
    189: "South Africa",
    191: "Sri Lanka", 
    208: "Turkey", 
    214: "United Arab Emirates", 
    215: "England", 
    216: "United States of America",
}

# colocando nome nas cores dos códigos
colors = {
    '3F7E00': 'darkgreen', 
    '5BA829': 'green', 
    '9ACD32': 'lightgreen', 
    'CDD614': 'orange', 
    'FFBA00': 'red', 
    'CBCBC8': 'darkred', 
    'FF7800': 'darkred',
}


# Definindo o custo do prato pelo número
def create_price_tye(price_range):
    if price_range == 1:
        return 'cheap'
    elif price_range == 2:
        return 'normal'
    elif price_range == 3:
        return 'expensive'
    elif price_range == 4:
        return 'gourmet'

# Definindo o custo do prato pelo número
def create_yes_no(yes_no):
    if yes_no == 1:
        return 'Yes'
    else:
        return 'No'


# Renomear as colunas do DF
def rename_columns(dataframe):
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new

def color_name(color_code):
    return colors[color_code]

def country_name(country_id):
    return countries[country_id]


# Aplicando as defs

def clean_code(df1):
    
    df = df.dropna()
    df["country"] = df.loc[:, "Country Code"].apply(lambda x: country_name(x))
    df["color_name"] = df.loc[:, "Rating color"].apply(lambda x: color_name(x))
    df["Cuisines"] = df.loc[:, "Cuisines"].apply(lambda x: x.split(",")[0])
    df["price_type"] = df.loc[:, "Price range"].apply(lambda x: create_price_tye(x))
    df["delivering_now"] = df.loc[:, "Is delivering now"].apply(lambda x: create_yes_no(x))
    df["table_booking"] = df.loc[:, "Has Table booking"].apply(lambda x: create_yes_no(x))
    df["online_delivery"] = df.loc[:, "Has Online delivery"].apply(lambda x: create_yes_no(x))
    
    return df1



df1 = df.copy()


# --------------------------------------------------------
# Funções de gráfico
# --------------------------------------------------------


# ===================================================================
# Slidebar no streamlit - TUDO QUE ESTIVER DENTRO DA BARRA PRECISA TER O .sidebar
# =================================================================== 

st.header('FomeZero')


# Comando pra trazer imagem
image_path = 'foco.png'
image = Image.open( image_path )
st.sidebar.image( image, width=120 )


st.sidebar.markdown('# FomeZero')
st.sidebar.markdown('## Marketplace de Restaurantes')

st.sidebar.markdown("""---""")

st.sidebar.markdown('## Filtro de Países')
country_options = st.sidebar.multiselect(
    'Selecione os países', 
    ['Philippines', 'Brazil', 'Austrália', 'United States of America',
       'Canadá', 'Singapure', 'United Arab Emirates', 'Índia',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'], 
    default=['Philippines', 'Brazil', 'Austrália', 'United States of America',
       'Canadá', 'Singapure', 'United Arab Emirates', 'Índia',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'] ) 


st.sidebar.markdown("""---""") 
st.sidebar.markdown("### Powered by Comunidade DS.")
st.sidebar.markdown("###### Talitha Oliveira")


#country_sel = df1['country'].isin( country_options ) 
#df1 = df1.loc[country_sel, :]


# ===================================================================
# Layout no streamlit  -- Aqui vai no corpo da página
# ===================================================================




with st.container():
    st.markdown("""---""")
    st.markdown('### Somos uma startup focado em restaurantes de todos os paízes.')
    st.markdown('##### Abaixo um pouco de nós e de nossos clientes: ')
    



    #Slot de barras:
with st.container():
        col1, col2, col3, col4, col5 = st.columns( 5, gap= 'large') 
        

        with col1:

            
            rest_unicos = df1.loc[:, 'Restaurant ID'].nunique()
            col1.metric('Restaurantes únicos cadastrados', rest_unicos )

        with col2:

            
            count_unico = df1.loc[:, 'Country Code'].nunique()
            col2.metric('Países cadastrados', count_unico )

        with col3:

            cid_uniq = df1.loc[:, 'City'].nunique()
            col3.metric('Cidades cadastradas', cid_uniq )            


        with col4:

            score = df1.loc[:, 'Votes'].sum()
            col4.metric('Total de avaliações', score )
        
        with col5:
            cuis_all = df1.loc[:, 'Cuisines'].nunique()
            col5.metric('Quantidade de culinárias registradas', cuis_all)
        

           
       
    





