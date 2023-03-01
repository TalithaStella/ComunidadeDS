# Para importar as bibliotecas as vezes tem que ir no terminal e escrescer pip install <nomedabiblioteca>

import pandas as pd
import streamlit as st

import plotly.express as px
import plotly.graph_objects as go
import folium
from haversine import haversine
from PIL import Image #pip install Image (não PIL)
from streamlit_folium import folium_static

df = pd.read_csv('train.csv')
df1 = df.copy()

df1.loc[:, 'ID'] = df1.loc[:,'ID'].str.strip()
df1.loc[:, 'Road_traffic_density'] = df1.loc[:,'Road_traffic_density'].str.strip()
df1.loc[:, 'Type_of_order'] = df1.loc[:,'Type_of_order'].str.strip()
df1.loc[:, 'Type_of_vehicle'] = df1.loc[:,'Type_of_vehicle'].str.strip()
df1.loc[:, 'City'] = df1.loc[:,'City'].str.strip()
df1.loc[:, 'Festival'] = df1.loc[:,'Festival'].str.strip()


trash1 = (df1['Delivery_person_Age'] != 'NaN ')
df1 = df1.loc[trash1, :].copy()

trash2 = (df1['City'] != 'NaN')
df1 = df1.loc[trash2, :].copy()

trash3 = (df1['Weatherconditions'] != 'NaN')
df1 = df1.loc[trash3, :].copy()

trash4 = (df1['Road_traffic_density'] != 'NaN')
df1 = df1.loc[trash4, :].copy()

trash04 = (df1['Festival'] != 'NaN ')
df1 = df1.loc[trash04, :].copy()

trash5 = (df1['multiple_deliveries'] != 'NaN ')
df1 = df1.loc[trash5, :].copy()
df1['multiple_deliveries'] = df1['multiple_deliveries'].astype(int)

df1['Delivery_person_Age'] = df1['Delivery_person_Age'].astype(int)

df1['Delivery_person_Ratings'] = df1['Delivery_person_Ratings'].astype(float)

df1['Order_Date'] = pd.to_datetime(df1['Order_Date'], format = '%d-%m-%Y')


df1['Time_taken(min)'] = df1['Time_taken(min)'].apply( lambda x: x.split( '(min) ' )[1] )
df1['Time_taken(min)'] = df1['Time_taken(min)'].astype(int)




# ===================================================================
# Slidebar no streamlit - TUDO QUE ESTIVER DENTRO DA BARRA PRECISA TER O .sidebar
# =================================================================== 

st.header('Visão Restaurantes') # O header fica como se fosse o .markdown ##


# Comando pra trazer imagem
image_path = 'foco.png'
image = Image.open( image_path )
st.sidebar.image( image, width=120 )


st.sidebar.markdown('# Cury Company')
st.sidebar.markdown('## Festest Delivery in Town')
st.sidebar.markdown("""---""")  # BARRA DE SEPARAÇÃO

st.sidebar.markdown('## Date Filter') # Adicionar a barra de arrastar

date_slider = st.sidebar.slider(
    'Select a date:',
    value=pd.datetime(2022, 4, 13), # ano/mes/dia
    min_value=pd.datetime(2022, 2, 11),
    max_value=pd.datetime(2022, 4, 6),
    format='DD-MM-YYYY' )

st.sidebar.markdown("""---""")

st.sidebar.markdown('## Traffic Condition Filter') # Adicionar filtro multi selecionável

traffic_options = st.sidebar.multiselect(
    'Which traffic condition?', 
    ['Low', 'Medium', 'High', 'Jam'], 
    default=['Low', 'Medium', 'High', 'Jam'] ) # pode deixar só com 1 parâmetro como padrão


st.sidebar.markdown("""---""") # Rodapé
st.sidebar.markdown("### Powered by Comunidade DS.")
st.sidebar.markdown("###### Talitha Oliveira")


# SETTANDO OS FILTROS

# Filtro de data
datas_sel = df1['Order_Date'] < date_slider
df1 = df1.loc[datas_sel, :]


# Filtro de transito
traff_sel = df1['Road_traffic_density'].isin( traffic_options ) # Isin - esta em <FILTRO CRIADO>
df1 = df1.loc[traff_sel, :]


# ===================================================================
# Layout no streamlit  -- Aqui vai no corpo da página
# ===================================================================


tab1, tab2, tab3 = st.tabs( ['Visão Gerencial', '_', '_'] )



with tab1: 
    
    with st.container():
        
        st.subheader ('Tem 2 colunas')
        
        
        col1, col2 = st.columns( 2) 
        with col1:
            st.markdown ('#### Metrics')

            


        with col2:
            st.markdown ('#### Metrics')

            


            
            
    with st.container():
        
        st.markdown("""---""")
        st.subheader( 'Tem 1 coluna' )
        



            
    with st.container():
        st.markdown("""---""")
        st.subheader('tb tem 2 colunas')
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('#### e')
            
            
                         
        with col2:
            st.markdown('#### q')   
            
        
                                     
            
       
    
with tab2:
    st.subheader ('_')

        
    
       
    

with tab3:
    st.subheader ('_')



