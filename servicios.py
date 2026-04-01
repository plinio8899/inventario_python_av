def agregar_producto(inventario, nombre, precio, cantidad):
    """Agrega un producto al inventario."""
    producto = {"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)}
    inventario.append(producto)
    print(f"✅ Producto '{nombre}' agregado correctamente.")

def mostrar_inventario(inventario):
    """Muestra todos los productos en formato de tabla simple."""
    if not inventario:
        print("⚠️ El inventario está vacío.")
        return
    print("\n--- INVENTARIO ACTUAL ---")
    for p in inventario:
        print(f"Nombre: {p['nombre']:<15} | Precio: ${p['precio']:>8.2f} | Stock: {p['cantidad']}")

def buscar_producto(inventario, nombre):
    """Busca un producto por nombre y retorna el diccionario o None."""
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """Actualiza precio y/o cantidad de un producto existente."""
    p = buscar_producto(inventario, nombre)
    if p:
        if nuevo_precio is not None: p["precio"] = float(nuevo_precio)
        if nueva_cantidad is not None: p["cantidad"] = int(nueva_cantidad)
        print(f"🔄 Producto '{nombre}' actualizado.")
    else:
        print("❌ Producto no encontrado.")

def eliminar_producto(inventario, nombre):
    """Elimina un producto del inventario por su nombre."""
    p = buscar_producto(inventario, nombre)
    if p:
        inventario.remove(p)
        print(f"🗑️ Producto '{nombre}' eliminado.")
    else:
        print("❌ No se pudo eliminar: producto no encontrado.")

def calcular_estadisticas(inventario):
    """Calcula métricas del inventario y las retorna en un diccionario."""
    if not inventario:
        return None
    
    # Uso de lambda para subtotal (Tarea 3)
    subtotal_func = lambda p: p["precio"] * p["cantidad"]
    
    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(subtotal_func(p) for p in inventario)
    
    producto_mas_caro = max(inventario, key=lambda x: x["precio"])
    producto_mayor_stock = max(inventario, key=lambda x: x["cantidad"])
    
    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "mas_caro": producto_mas_caro,
        "mayor_stock": producto_mayor_stock
    }