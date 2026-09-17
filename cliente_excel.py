import asyncio
from datetime import datetime
from asyncua import Client
import xlwings as xw  # <-- 1. Importamos la librería para controlar Excel

async def main():
    url = "opc.tcp://localhost:4840/freeopcua/server/"
    
    # --- 2. ABRIR EXCEL Y CREAR LOS ENCABEZADOS ---
    app = xw.App(visible=True)  # Abre la ventana de Excel en pantalla
    wb = app.books.add()        # Crea un libro nuevo sin título
    ws = wb.sheets[0]           # Selecciona la Hoja 1

    # Títulos fijos en la primera fila (Horizontal)
    ws.range("A1").value = "Hora"
    ws.range("B1").value = "My_INT (D0)"
    ws.range("C1").value = "My_STRING (D4)"
    ws.range("D1").value = "Foco_Y0 (Y0)"
    ws.range("E1").value = "Byte_D3"
    ws.range("F1").value = "Mi_DINT"

    row_index = 2        # Empezaremos a escribir en la Fila 2
    ultimo_estado = None # Variable para comparar si los datos cambiaron

    # Abrimos conexión con el Servidor OPC UA
    async with Client(url=url) as client:
        # 1. Obtenemos el ID del espacio de nombres
        ns_idx = await client.get_namespace_index("http://mitsubishi.fx5u.opc")
        
        # 2. Apuntamos a los nodos navegando por el árbol de carpetas
        root = client.nodes.root
        node_my_int = await root.get_child(["0:Objects", f"{ns_idx}:FX5U_PLC", f"{ns_idx}:My_INT"])
        node_my_string = await root.get_child(["0:Objects", f"{ns_idx}:FX5U_PLC", f"{ns_idx}:My_STRING"])
        node_foco_y0 = await root.get_child(["0:Objects", f"{ns_idx}:FX5U_PLC", f"{ns_idx}:Foco_Y0"])
        node_mi_byte = await root.get_child(["0:Objects", f"{ns_idx}:FX5U_PLC", f"{ns_idx}:Mi_Byte"])
        node_mi_Dint = await root.get_child(["0:Objects", f"{ns_idx}:FX5U_PLC", f"{ns_idx}:Mi_DINT"])

        while True:
            # 3. Leemos los valores actuales guardados en la memoria del Servidor OPC UA
            val_int = await node_my_int.read_value()
            val_str = await node_my_string.read_value()
            val_foco = await node_foco_y0.read_value()
            val_d3 = await node_mi_byte.read_value()
            val_dint = await node_mi_Dint.read_value()

            estado_actual = (val_int, val_str, val_foco, val_d3, val_dint)

            # --- 3. ESCRIBIR EN EXCEL SOLO SI CAMBIÓ ALGÚN DATO ---
            if estado_actual != ultimo_estado:
                hora = datetime.now().strftime("%H:%M:%S")

                # Llenamos las celdas de la fila actual (A, B, C, D, E)
                ws.cells(row_index, 1).value = hora
                ws.cells(row_index, 2).value = val_int
                ws.cells(row_index, 3).value = val_str
                ws.cells(row_index, 4).value = val_foco
                ws.cells(row_index, 5).value = val_d3
                ws.cells(row_index, 6).value = val_dint

                print(f"[EXCEL] Nueva Fila")
                
                # Guardamos este estado y pasamos al siguiente renglón
                ultimo_estado = estado_actual
                row_index += 1
            else:
                print("[OMITIDO]")

            await asyncio.sleep(10)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("\nServidor OPC UA detenido por el usuario.")