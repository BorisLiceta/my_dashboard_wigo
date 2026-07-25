# OBTENIENDO INDICADORES GENERALES
# --------------------------------

def precio_total(df):
    return df["precio_venta"].sum() 

def unidades_vendidas(df):
    return df["cantidad"].sum()

def precio_promedio(df):
    return df["precio_venta"].mean()

def operaciones(df):
    return len(df)

def precio_maximo(df):
    return df["precio_venta"].max()

def precio_minimo(df):
    return df["precio_venta"].min()

def ingreso_total(df):
    return (df["precio_venta"] * df["cantidad"]).sum()

def ticket_promedio(df):

    if len(df) == 0:
        return 0

    return ingreso_total(df) / len(df)
