# GRÁFICOS DE BARRAS EN STREAMLIT:
# --------------------------------

import pandas as pd
import plotly.express as px

# =====================================
# GRÁFICO 1
# Ventas por Marca
# =====================================

def grafico_ventas(df):

    ventas = df.groupby("marca")["cantidad"].sum().reset_index()

    grafico01 = px.bar(
        ventas,
        x="marca",
        y="cantidad",
        title="Ventas por Marca",
        color="marca",
        color_discrete_sequence=px.colors.qualitative.Set1
    )

    return grafico01


# =====================================
# GRÁFICO 2
# Precio promedio por Marca
# =====================================

def grafico_promedio(df):

    promedio = df.groupby("marca")["precio_venta"].mean().reset_index()

    grafico02 = px.bar(
        promedio,
        x="marca",
        y="precio_venta",
        title="Precio promedio por Marca",
        color="marca",
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    return grafico02


# =====================================
# GRÁFICO 3
# Ventas por Sede
# =====================================

def grafico_sede(df):

    sede = df.groupby("tienda")["cantidad"].sum().reset_index()

    grafico03 = px.bar(
        sede,
        x="tienda",
        y="cantidad",
        title="Ventas por Sede",
        color="tienda",
        color_discrete_sequence=px.colors.qualitative.Bold
    )

    return grafico03


# =====================================
# GRÁFICO 4
# Ventas por Asesor Comercial
# =====================================

def grafico_asesor(df):

    asesor = df.groupby("asesor_comercial")["cantidad"].sum().reset_index()

    grafico04 = px.bar(
        asesor,
        x="asesor_comercial",
        y="cantidad",
        title="Ventas por Asesor Comercial",
        color="asesor_comercial",
        color_discrete_sequence=px.colors.qualitative.Dark24
    )

    return grafico04


# =====================================
# GRÁFICO 5
# Método de Pago
# =====================================

def grafico_metodo_pago(df):

    metodo = df.groupby("metodo_pago").size().reset_index(name="operaciones")

    grafico05 = px.pie(
        metodo,
        names="metodo_pago",
        values="operaciones",
        title="Distribución por Método de Pago",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )

    return grafico05


# =====================================
# GRÁFICO 6
# Ingresos por Marca
# =====================================

def grafico_ingresos(df):

    ingresos = df.copy()

    ingresos["ingreso"] = (
        ingresos["precio_venta"] *
        ingresos["cantidad"]
    )

    ingresos = ingresos.groupby("marca")["ingreso"].sum().reset_index()

    grafico06 = px.bar(
        ingresos,
        x="marca",
        y="ingreso",
        title="Ingresos por Marca",
        color="marca",
        color_discrete_sequence=px.colors.qualitative.Prism
    )

    return grafico06

# =====================================
# GRÁFICO 7
# TOP 5 MODELOS VENDIDOS
# =====================================

def grafico_top_modelos(df):

    modelos = (
        df.groupby("modelo")["cantidad"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    grafico07 = px.bar(
        modelos,
        x="modelo",
        y="cantidad",
        title="Top 10 Modelos Vendidos",
        color="modelo",
        color_discrete_sequence=px.colors.qualitative.Vivid
    )

    return grafico07

# =====================================
# GRÁFICO 8
# TENDENCIA MENSUAL DE VENTAS
# =====================================

def grafico_tendencia(df):

    tendencia = df.copy()

    tendencia["fecha"] = pd.to_datetime(tendencia["fecha"])

    tendencia = (
        tendencia
        .groupby(tendencia["fecha"].dt.to_period("M"))["precio_venta"]
        .sum()
        .reset_index()
    )

    tendencia["fecha"] = tendencia["fecha"].astype(str)

    grafico08 = px.line(
        tendencia,
        x="fecha",
        y="precio_venta",
        title="Tendencia Mensual de Ventas",
        markers=True
    )

    grafico08.update_traces(
        line=dict(color="green", width=3)
    )

    return grafico08
