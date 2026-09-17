import asyncio
from asyncua import Server
import pymcprotocol

# Parámetros de red de tu PLC
PLC_IP = "192.168.1.30"
PLC_PORT = 5000

async def main():
    # --- PASO 1: Conexión al PLC ---
    # Creamos el cliente SLMP para hablar con Mitsubishi
    pymc = pymcprotocol.Type3E()
    pymc.setaccessopt(commtype="binary")

    # Nos conectamos al PLC
    try:    
        pymc.connect(PLC_IP, PLC_PORT)
        print("Conectado con éxito al PLC")
    except Exception as e:
        print(f"Error al conectar con el PLC: {e}")

    # --- PASO 2: Inicializar el Servidor OPC UA ---
    # Inicializamos el servidor OPC UA
    server = Server()
    await server.init()

    # Le decimos en qué IP y puerto escuchar dentro de tu PC
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")
    server.set_server_name("Servidor OPC UA FX5U")

    # Creamos un identificador único (Namespace) para nuestras variables
    uri = "http://mitsubishi.fx5u.opc"
    idx = await server.register_namespace(uri)

    # --- PASO 3: Crear la estructura de carpetas y Nodos ---
    # 1. Creamos la carpeta raíz "FX5U_PLC" dentro de la sección Objects
    objects = server.nodes.objects
    plc_folder = await objects.add_folder(idx, "FX5U_PLC")

    # 2. Registramos los Nodos (Nombre, Valor Inicial)
    node_my_int = await plc_folder.add_variable(idx, "My_INT", 0)
    node_mi_dint = await plc_folder.add_variable(idx, "Mi_DINT", 0)
    node_my_string = await plc_folder.add_variable(idx, "My_STRING", "")
    node_mi_byte = await plc_folder.add_variable(idx, "Mi_Byte", 0)
    node_boton_m0 = await plc_folder.add_variable(idx, "Boton_M0", False)
    node_foco_y0 = await plc_folder.add_variable(idx, "Foco_Y0", False)

    # 3. Permitimos escritura para las variables que se modificarán desde afuera
    await node_my_int.set_writable()
    await node_my_string.set_writable()
    await node_boton_m0.set_writable()

    print("Carpetas y Nodos OPC UA creados con éxito.")

    # --- PASO 4: Iniciar Servidor y Bucle de Lectura ---
    async with server:
        print("\nServidor OPC UA activo en opc.tcp://localhost:4840")
        print("Leyendo PLC en tiempo real... (Presiona Ctrl+C para salir)\n")

        while True:
            try:
                # 1. Leer D0 (Word 16 bits)
                val_d0 = pymc.batchread_wordunits(headdevice="D0", readsize=1)[0]

                # 2. Leer D1-D2 (Doble Word 32 bits sin signo)
                val_d1 = pymc.batchread_wordunits(headdevice="D1", readsize=2)

                # Convertir cada palabra de 16 bits a entero sin signo
                w0 = val_d1[0] & 0xFFFF
                w1 = val_d1[1] & 0xFFFF

                # Combinar ambas palabras (w1 desplaza 16 bits a la izquierda)
                dint_val = w0 | (w1 << 16)

                # 3. Leer String D4-D19 (16 words = 32 caracteres)
                words_string = pymc.batchread_wordunits(headdevice="D4", readsize=16)
                val_string = b''.join(w.to_bytes(2, byteorder='little') for w in words_string).decode('utf-8', errors='ignore').replace('\x00', '').strip()

                # 4. Leer Bits (M0 y Y0)
                val_m0 = pymc.batchread_bitunits(headdevice="M0", readsize=1)[0]
                val_y0 = pymc.batchread_bitunits(headdevice="Y0", readsize=1)[0]

                # 5. Leer byte(D3)
                val_d3 = pymc.batchread_wordunits(headdevice="D3",readsize=1)[0] & 0xFF

                # 6. Actualizar Nodos en OPC UA
                await node_my_int.write_value(int(val_d0))
                await node_mi_dint.write_value(int(dint_val))
                await node_my_string.write_value(str(val_string))
                await node_mi_byte.write_value(int(val_d3))
                await node_boton_m0.write_value(bool(val_m0))
                await node_foco_y0.write_value(bool(val_y0))

            except Exception as err:
                print(f"Error leyendo del PLC: {err}")

            # Pausa de 500 milisegundos entre lecturas
            await asyncio.sleep(.2)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("\nServidor OPC UA detenido por el usuario.")