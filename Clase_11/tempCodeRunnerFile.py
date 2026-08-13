def mostrar_top_10(datos: pd.DataFrame) -> str: 
    """Muestra las primeras 10 entidades limpias."""
    seleccion = ["ENTIDAD", "COMPRA", "VENTA", "DIFERENCIAL"]
    top_10 = datos[seleccion].head(10).to_string(index=False)
    return top_10