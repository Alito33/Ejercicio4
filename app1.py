import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime

sns.set_style("darkgrid")
st.title("Visualización de ventiladores mecanicos por COVID-19 en Chile")

st.markdown("### Bienvenido al visualizador")

df = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto20/NumeroVentiladores.csv")

st.dataframe(df)
ventiladores = st.radio("Ventiladores", df.Ventiladores.unique())


st.markdown("Su selección es: "+ventiladores)

ilocs=df.iloc[:,2:-1]
superfiltro=df[(df.Ventiladores==ventiladores)]
primerafecha=datetime.strptime(df.columns[1], '%Y-%m-%d')
ultimafecha=datetime.strptime(df.columns[-1], '%Y-%m-%d')

#st.table(ilocs.head(10))
start_time = st.slider(
   "Elija el rango de fecha",
value=[primerafecha,ultimafecha],
min_value=primerafecha,
max_value=ultimafecha,
format="YYYY-MM-DD")

index_of_primera_fecha=df.columns.get_loc(start_time[0].strftime('%Y-%m-%d'))
index_of_ultima_fecha=df.columns.get_loc(start_time[1].strftime('%Y-%m-%d'))

fig,ax= plt.subplots()

to_plot=superfiltro.iloc[:,index_of_primera_fecha:index_of_ultima_fecha]
ax.plot(to_plot.T)
ax.set_title("Ventiladores mecanicos por casos COVID-19")
ax.set_ylabel(ventiladores)
ax.set_xlabel("Fecha")

xs=np.arange(0,index_of_ultima_fecha-index_of_primera_fecha+1)
plt.xticks(xs,rotation=90)
st.pyplot(fig)

