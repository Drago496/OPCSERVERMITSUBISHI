----------HOW TO USE IF YOU HAVE A OPC SERVER------------
First 
You should verify if you PC has windows and python.
If your computer doesn't have windows this package cannot be use.
If your computer doesn't have python, you should install this https://www.python.org/downloads/ 

Second
You need install next library, open cmd and write next code.
  code:
    py -m pip install asyncua xlwings pywin32

Now, when you finish to installing the libreries you should install cliente_excel.py in your computer and save it in your desired folder.
Open the file with notepad and modify ip address and port, if only necessary.
  Default: 
    url = "opc.tcp://localhost:4840/freeopcua/server/"
  Modified:
    url = "opc.tcp://192.168.1.x:port/freeopcua/server/"

Modify the variables and their data types following the example in the code

Third
Open cmd and select directory the cliente_excel.py 
  with:
      cd C:directory

Fourth
execute code 
  with:
    py cliente_excel.py

Now this file should open new excel and your can view the var in real time.

If you save the .xlsx, you should save this different name because if you open the file again, it will overwrite the file and you will lose your daily report.


----------HOW TO USE IF YOU DON'T HAVE AN OPC SERVER----------
You should have install python, GX works3(if not necessary but is a visual reference ) and VSC(if not necessary but is a visual reference).

First
Install library for the use file.
open cmd or terminal and write next line code.
  code:
  py -m pip install asyncua pymcprotocol

Second
Open the file OPCSERVER.PY and modify the variables, IP address, and port that the PLC uses.
and this your like modify the port with you'll use.
  address plc:
    PLC_IP = "192.168.1.x"
    PLC_PORT = port

  Port OPC(if you don't like port):
    server.set_endpoint("opc.tcp://0.0.0.0:port/freeopcua/server/")

Modify the variables and their data types following the example in the code

Third
If you are communicating over Wi-Fi / LAN. Your computer need open the create port in the file.
you should research in your computer 
  Firewall de Windows Defender

1. Entry in advance configuration.
2. In "Reglas de entrada" you create "Nueva regla".
3. Select "puerto" y next
5. Select connection  TCP and in "Puerto locales específicos" you write port created by the file.
6. Select "Permitir la conexión" and next, You give a name for example: "OPC UA SERVER"

Execute file in VSC terminal or your terminal prefer.
