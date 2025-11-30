import json

def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el archivo: {path}")
    except json.JSONDecodeError:
        raise ValueError(f"El archivo JSON tiene un formato inválido: {path}")


def save_json(path, data):
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        raise RuntimeError(f"No se pudo guardar el archivo {path}: {e}")
