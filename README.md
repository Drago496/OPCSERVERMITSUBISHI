----------HOW TO USE IF YOU HAVE A OPC SERVER------------
First 
You should verificate if you pc have windows and python.
If your computer don't have windows this package can't use.
If your computer dont have pythom, you should install this https://www.python.org/downloads/ 

Second
You need install next library, open cmd and write next code.
  code:
    py -m pip install asyncua xlwings pywin32

Now, when you finish to install library you should install cliente_excel.py in your computer and select where install in yours files.
Open the file with notepad and modify ip address and port, if only necessary.
  this your have: 
    url = "opc.tcp://localhost:4840/freeopcua/server/"
  this your modify
    url = "opc.tcp://192.168.1.x:port/freeopcua/server/"

And this your need modify var, modify this type, your should the follow sentence the code.

Third
Open cmd and select direction the cliente_excel.py 
  with:
      cd C:direction

Fourth
execute code 
  with:
    py cliente_excel.py

Now this file should open new excel and your can view the var in real time.

If you save the .xlsx, you should save this diferent name because if you open the file again this overwrite .xlsx 
and you lost you report of day.


----------HOW TO USE IF YOU HAVEN'T A OPC SERVER----------
You should have install python, GX works3(if don't necessary but is a visual reference ) and VSC(if don't necessary but is a visual reference).

First
Install library for the use file.
open cmd or terminal and write next line code.
  code:
  py -m pip install asyncua pymcprotocol

Second
Open the file OPCSERVER.PY and modify var, ip address and port what plc use,
and this your like modify the port with you'll use.
  adress plc:
    PLC_IP = "192.168.1.x"
    PLC_PORT = port

  Port OPC(if you don't like port):
    server.set_endpoint("opc.tcp://0.0.0.0:port/freeopcua/server/")

And this your need modify var, modify this type, your should the follow sentence the code.

Third
If you communication this for wifi lan your computer need open the create port in the file.
you should research in your computer 
  Firewall de Windows Defender

1. Entry in advance configuration.
2. In "Reglas de entrada" you create "Nueva regla".
3. Select "puerto" y next
5. Select connection  TCP and in "Puerto locales específicos" you write port created by the file.
6. Select "Permitir la conexión" and next, You give a name for example: "OPC UA SERVER"

Execute file in VSC terminal or your terminal prefer.

Now this code mark error, your need fix the bug 

