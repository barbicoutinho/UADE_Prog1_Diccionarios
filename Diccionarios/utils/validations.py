def validate_article_name(name):
    if not isinstance(name, str):
        raise TypeError("El nombre del artículo debe ser una cadena (string).")


def validate_quantity(q):
    if not isinstance(q, int):
        raise TypeError("La cantidad debe ser un número entero.")
    if q < 0:
        raise ValueError("La cantidad no puede ser negativa.")


def validate_dict_structure(d):
    if not isinstance(d, dict):
        raise TypeError("Se esperaba un diccionario.")
    for key, value in d.items():
        validate_article_name(key)
        validate_quantity(value)
