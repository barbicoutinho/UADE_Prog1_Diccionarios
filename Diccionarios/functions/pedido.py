from functions.stock import hayStock

def procesarPedido(carrito, stock):
    if not isinstance(carrito, dict) or not isinstance(stock, dict):
        raise TypeError("Carrito y stock deben ser diccionarios.")

    nuevo_stock = stock.copy()
    no_procesados = []

    for articulo, cantidad in carrito.items():

        if not isinstance(articulo, str):
            raise TypeError("Los nombres de artículos deben ser cadenas de texto.")

        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError(f"La cantidad de '{articulo}' no es válida.")

        if hayStock(articulo, cantidad, nuevo_stock):
            nuevo_stock[articulo] -= cantidad
        else:
            no_procesados.append(articulo)

    return nuevo_stock, no_procesados
