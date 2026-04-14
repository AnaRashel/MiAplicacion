import streamlit as st
import libreria_funciones as lf

st.title("Mi primera app")

st.sidebar.title("Datos")
st.image("logo.png",width=100)
st.sidebar.image("DMClogo.png")
st.title("clase 5 funciones")


p=st.number_input("Ingrese el monto principal",value=12000)
t=st.number_input("Ingresa la tasa anual", value=0.05)
a=st.slider("Seleccione el números de años del prestamo",min_value=1,max_value=5)
pa=st.number_input("Cantidad de pagos por año",value=12)
cuota=lf.cuota_prestamo(p,t,a,pa)
st.write(cuota)


