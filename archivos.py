import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    """Guarda el inventario en un archivo CSV."""
    if not inventario:
        print("⚠️ Error: El inventario está vacío. No hay nada que guardar.")
        return

    try:
        with open(ruta, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["nombre", "precio", "cantidad"])
            if incluir_header:
                writer.writeheader()
            writer.writerows(inventario)
        print(f"💾 Inventario guardado en: {ruta}")
    except PermissionError:
        print("❌ Error: No tienes permisos para escribir en esta ubicación.")
    except Exception as e:
        print(f"❌ Error inesperado al guardar: {e}")

def cargar_csv(ruta):
    """Carga productos desde un CSV con validaciones estrictas."""
    productos_cargados = []
    errores = 0
    
    try:
        with open(ruta, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            # Validar encabezado
            if reader.fieldnames != ["nombre", "precio", "cantidad"]:
                print("❌ Error: El formato del encabezado CSV es inválido.")
                return None

            for fila in reader:
                try:
                    # Validar exactamente 3 columnas y valores no negativos
                    nombre = fila["nombre"].strip()
                    precio = float(fila["precio"])
                    cantidad = int(fila["cantidad"])
                    
                    if precio < 0 or cantidad < 0 or not nombre:
                        raise ValueError
                    
                    productos_cargados.append({
                        "nombre": nombre, "precio": precio, "cantidad": cantidad
                    })
                except (ValueError, TypeError, KeyError):
                    errores += 1
                    
        return productos_cargados, errores
    except FileNotFoundError:
        print("❌ Error: El archivo no existe.")
    except UnicodeDecodeError:
        print("❌ Error: Problema de codificación al leer el archivo.")
    return None