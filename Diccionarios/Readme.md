## Resumen del Proyecto

Este proyecto simula un sistema básico de ventas online utilizando Python y diccionarios. Los usuarios pueden armar un carrito de compras, y el programa verifica la disponibilidad de los artículos en el stock antes de procesar el pedido. Los datos se almacenan en archivos JSON (carrito.json y stock.json), permitiendo persistencia y actualización de la información.

El proyecto aplica buenas prácticas de programación:

  Uso de diccionarios para representar artículos y cantidades, respetando la relación clave–valor.
  Funciones modulares (hayStock y procesarPedido) que separan la lógica de validación y actualización del stock.
  Validaciones de entrada y manejo de errores para garantizar datos consistentes y seguros.
  Persistencia histórica del carrito y del stock, asegurando que la información se mantenga entre sesiones.

## Propuestas de mejora implementables

Validación de artículos: asegurar que los productos ingresados en el carrito existan en el stock, evitando claves inválidas.

Preservación del historial del carrito: actualizar carrito.json de manera acumulativa en lugar de sobrescribirlo, manteniendo registros de compras anteriores y mejorando la trazabilidad del sistema.

Estas mejoras alinean el proyecto con la teoría de diccionarios en Python y fortalecen la coherencia, integridad y robustez del sistema de ventas.
