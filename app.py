import servicios
import archivos

def menu():
    inventario = []
    while True:
        print("\n--- SISTEMA DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Estadísticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("0. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            n = input("Nombre: ")
            p = input("Precio: ")
            c = input("Cantidad: ")
            servicios.agregar_producto(inventario, n, p, c)

        elif opcion == "2":
            servicios.mostrar_inventario(inventario)

        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            res = servicios.buscar_producto(inventario, nombre)
            print(res if res else "No encontrado.")

        elif opcion == "4":
            nombre = input("Nombre del producto a actualizar: ")
            p = input("Nuevo precio (dejar vacío para omitir): ")
            c = input("Nueva cantidad (dejar vacío para omitir): ")
            servicios.actualizar_producto(
                inventario, nombre, 
                nuevo_precio=p if p else None, 
                nueva_cantidad=c if c else None
            )

        elif opcion == "5":
            nombre = input("Nombre a eliminar: ")
            servicios.eliminar_producto(inventario, nombre)

        elif opcion == "6":
            stats = servicios.calcular_estadisticas(inventario)
            if stats:
                print(f"\n--- ESTADÍSTICAS ---")
                print(f"Unidades totales: {stats['unidades_totales']}")
                print(f"Valor total: ${stats['valor_total']:.2f}")
                print(f"Más caro: {stats['mas_caro']['nombre']} (${stats['mas_caro']['precio']})")
                print(f"Mayor stock: {stats['mayor_stock']['nombre']} ({stats['mayor_stock']['cantidad']} und)")
            else:
                print("No hay datos para estadísticas.")

        elif opcion == "7":
            archivos.guardar_csv(inventario, "inventario.csv")

        elif opcion == "8":
            resultado = archivos.cargar_csv("inventario.csv")
            if resultado:
                nuevos_prods, errores = resultado
                print(f"Se encontraron {len(nuevos_prods)} productos válidos y {errores} errores.")
                
                modo = input("¿Sobrescribir inventario actual? (S/N): ").upper()
                if modo == 'S':
                    inventario[:] = nuevos_prods
                    print("Inventario reemplazado.")
                else:
                    # Política de fusión: Sumar cantidad y actualizar precio
                    for np in nuevos_prods:
                        existente = servicios.buscar_producto(inventario, np["nombre"])
                        if existente:
                            existente["cantidad"] += np["cantidad"]
                            existente["precio"] = np["precio"]
                        else:
                            inventario.append(np)
                    print("Inventario fusionado (Cantidades sumadas, precios actualizados).")

        elif opcion == "0":
            break

if __name__ == "__main__":
    menu()