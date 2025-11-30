import json
from functions.pedido import procesarPedido
from functions.stock import hayStock

DATA_CARRITO = "data/carrito.json"
DATA_STOCK = "data/stock.json"

def mostrar_diccionario(dic, titulo):
    print(f"\n{titulo}:")
    for articulo, cantidad in dic.items():
        print(f"  {articulo}: {cantidad}")

def main():
    # Cargar datos
    with open(DATA_STOCK, "r") as f:
        stock = json.load(f)

    carrito = {}
    
    print("="*50)
    print("BIENVENIDO AL SISTEMA DE VENTAS ONLINE")
    print("="*50)

    # Mostrar stock inicial
    mostrar_diccionario(stock, "Stock disponible")

    # Interacción: el usuario agrega productos al carrito
    while True:
        articulo = input("\nIngrese el nombre del artículo a agregar al carrito (o 'fin' para terminar): ").strip()
        if articulo.lower() == "fin":
            break
        try:
            cantidad = int(input(f"Ingrese la cantidad de '{articulo}': "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Intente de nuevo.")
                continue
        except ValueError:
            print("Cantidad inválida. Debe ser un número entero.")
            continue

        if articulo in carrito:
            carrito[articulo] += cantidad
        else:
            carrito[articulo] = cantidad

        print(f"Artículo '{articulo}' agregado al carrito. Cantidad total: {carrito[articulo]}")

    if not carrito:
        print("\nEl carrito está vacío. Finalizando programa.")
        return

    # Mostrar carrito cargado
    mostrar_diccionario(carrito, "Carrito cargado")

    # Confirmación de pedido
    confirmacion = input("\n¿Desea confirmar el pedido? (s/n): ").strip().lower()
    if confirmacion != "s":
        print("Pedido cancelado.")
        return

    # Guardar carrito actualizado
    with open(DATA_CARRITO, "w") as f:
        json.dump(carrito, f, indent=4)

    print("\nEl carrito actualizado fue guardado en carrito.json")

    # Procesar pedido
    nuevo_stock, no_procesados = procesarPedido(carrito, stock)

    # Mostrar resultados
    mostrar_diccionario(nuevo_stock, "Stock actualizado después de procesar el pedido")
    if no_procesados:
        print("\nLos siguientes artículos no se pudieron procesar por falta de stock:")
        for art in no_procesados:
            print(f"  {art}")

    # Guardar stock actualizado
    with open(DATA_STOCK, "w") as f:
        json.dump(nuevo_stock, f, indent=4)

    print("\nEl stock actualizado fue guardado en stock.json")
    print("="*50)
    input("\nPresione ENTER para salir...")

if __name__ == "__main__":
    main()
