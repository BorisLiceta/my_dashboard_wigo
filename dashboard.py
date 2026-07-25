
import streamlit as st 
from conexion import cargar_datos
from indicadores import *
from graficos import *

def login():
    if "autenticado" not in st.session_state:
        st.session_state.autenticado = False

    if st.session_state.autenticado:
        return  True
    
    st.title("Inicio de sesión")

    usuario = st.text_input("Usuario")
    password = st.text_input(
        "Contraseña",
        type="password"
    )
    if st.button("Ingresar"):
        if usuario == "admin" and password == "12345":

            st.session_state.autenticado = True
            st.rerun()

        else:
            st.error("Usuario o contraseña incorrecta")

    return False

st.set_page_config(
    page_title="Wigo Motors",
    layout="wide"
)

# Mostrar login
if not login():
    st.stop()


df = cargar_datos() # UTILIZANDO LA FUNCIÓN QUE NOS DEVUELVE EL DATAFRAME (DF)

# CONFIGURACIÓN DE DASHBOARD CON STREAMLIT:
# ----------------------------------------

st.set_page_config(page_title = "Wigo Motors", 
                   layout="wide")      

st.title("WIGO MOTORS S.A.C.")                      
st.subheader("Buscador comercial") 

st.sidebar.header("Buscador")

# FILTRO POR MARCA

marca = st.sidebar.selectbox(
    "Marca",
    ["Todas"] + sorted(df["marca"].unique().tolist())
)

# FILTRO POR SEDE

tienda = st.sidebar.selectbox(
    "Sede",
    ["Todas"] + sorted(df["tienda"].unique().tolist())
)

# FILTRO POR ASESOR COMERCIAL

asesor = st.sidebar.selectbox(
    "Asesor comercial",
    ["Todos"] + sorted(df["asesor_comercial"].unique().tolist())
)

# FILTRO POR MÉTODO DE PAGO

metodo = st.sidebar.selectbox(
    "Método de Pago",
    ["Todos"] + sorted(df["metodo_pago"].unique().tolist())
)

# FILTRO POR RANGO DE PRECIOS

precio_min = int(df["precio_venta"].min())
precio_max = int(df["precio_venta"].max())

rango = st.sidebar.slider(
    "Rango de precios",
    precio_min,
    precio_max,
    (precio_min, precio_max)
)

# FILTRO POR FECHAS

fecha_min = df["fecha"].min()
fecha_max = df["fecha"].max()

rango_fechas = st.sidebar.slider(
    "Rango de fechas",
    min_value=fecha_min,
    max_value=fecha_max,
    value=(fecha_min, fecha_max),
    format="DD/MM/YYYY"
)

# =====================================
# APLICAR FILTROS
# =====================================

df_filtrado = df.copy()

if marca != "Todas":
    df_filtrado = df_filtrado[df_filtrado["marca"] == marca]

if tienda != "Todas":
    df_filtrado = df_filtrado[df_filtrado["tienda"] == tienda]

if asesor != "Todos":
    df_filtrado = df_filtrado[
        df_filtrado["asesor_comercial"] == asesor
    ]

if metodo != "Todos":
    df_filtrado = df_filtrado[
        df_filtrado["metodo_pago"] == metodo
    ]

df_filtrado = df_filtrado[
    (df_filtrado["precio_venta"] >= rango[0]) &
    (df_filtrado["precio_venta"] <= rango[1])
]

df_filtrado = df_filtrado[
    (df_filtrado["fecha"] >= rango_fechas[0]) &
    (df_filtrado["fecha"] <= rango_fechas[1])
]

# MOSTRAR RESULTADOS (TABLA):

st.success(f"Registros encontrados: {len(df_filtrado)}")

with st.expander("Ver resultados de la búsqueda", expanded=True):
    st.dataframe(
        df_filtrado,
        use_container_width=True
    )


# INDICADORES GENERALES: 

st.subheader("Indicadores:")

c1, c2, c3, c4 = st.columns(4)        

c1.metric("Precio Total", f"S/{precio_total(df_filtrado):,.2f}")          
c2.metric("Unidades vendidas", f"{unidades_vendidas(df_filtrado)}")                
c3.metric("Precio promedio", f"S/{precio_promedio(df_filtrado):,.2f}")     
c4.metric("Operaciones", operaciones(df_filtrado))                                      



c5, c6, c7, c8 = st.columns(4)  

c5.metric("Precio más alto", f"S/{precio_maximo(df_filtrado):,.2f}")
c6.metric("Precio más bajo", f"S/{precio_minimo(df_filtrado):,.2f}")
# NUEVOS INDICADORES

c7.metric("Ingreso total", f"S/{ingreso_total(df_filtrado):,.2f}")
c8.metric("Ticket_promedio", f"S/{ticket_promedio(df_filtrado):,.2f}")

# GRÁFICOS - DASHBOARD 

cg1, cg2 = st.columns(2)

with cg1:
    st.plotly_chart(grafico_ventas(df_filtrado), use_container_width=True)

with cg2:
    st.plotly_chart(grafico_promedio(df_filtrado), use_container_width=True)


cg3, cg4 = st.columns(2)

with cg3:
    st.plotly_chart(grafico_sede(df_filtrado), use_container_width=True)

with cg4:
    st.plotly_chart(grafico_asesor(df_filtrado), use_container_width=True)


cg5, cg6 = st.columns(2)

with cg5:
    st.plotly_chart(grafico_metodo_pago(df_filtrado), use_container_width=True)

with cg6:
    st.plotly_chart(grafico_ingresos(df_filtrado), use_container_width=True)


cg7, cg8 = st.columns(2)

with cg7:
    st.plotly_chart(
        grafico_top_modelos(df_filtrado),
        use_container_width=True
    )

with cg8:
    st.plotly_chart(
        grafico_tendencia(df_filtrado),
        use_container_width=True
    )
    
# =====================================
# CERRAR SESIÓN
# =====================================

if st.sidebar.button("Cerrar sesión"):

    st.session_state.autenticado = False
    st.rerun()

