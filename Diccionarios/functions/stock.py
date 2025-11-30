def hayStock(articulo, cantidad, stock):
    # Validaciones básicas
    if not isinstance(articulo, str):
        raise TypeError("El nombre del artículo debe ser una cadena de texto.")

    if not isinstance(cantidad, int):
        raise TypeError("La cantidad debe ser un número entero.")

    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa.")

    if not isinstance(stock, dict):
        raise TypeError("El stock debe ser un diccionario.")

    # Verificar existencia del artículo
    if articulo not in stock:
        return False

    # Verificar integridad del stock
    if not isinstance(stock[articulo], int) or stock[articulo] < 0:
        raise ValueError(f"El stock del artículo '{articulo}' es inválido.")

    # Verificar disponibilidad
    return stock[articulo] >= cantidad
