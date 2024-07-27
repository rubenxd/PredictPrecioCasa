import pandas as pd
import pickle
import streamlit as st

#Toma datos del archivo .csv y los almacena en el dataframe
#dataframe = pd.read_csv("Datos/house-price.csv", index_col=0)

with st.sidebar.form('price'):
    Casa = {
        'Bedrooms': st.number_input('Bedrooms', 3),
        'Bathrooms': st.number_input('Bathrooms',2),
        'Garage': st.number_input('Garage',2),
        'Build Year': st.number_input('Build Year',2011),
        'Floor Area': st.number_input('Floor Area',109)
    }

    submit = st.form_submit_button('Calcular')

name = "Wall street"

df_casa = pd.DataFrame(Casa, index=[name])
df_casa
#Importar modelo entrenado
with open("artifacts/model.pkl","rb") as ff:
    model = pickle.load(ff)

#Predecimos el valor de una casa
ValorSugerido = model.predict(df_casa)

st.write(f'Precio sugerido: ${ValorSugerido}')


