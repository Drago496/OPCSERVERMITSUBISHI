----------HOW TO USE IF YOU HAVE A OPC SERVER------------
First 
You should verificate if you pc have windows and python.
If your computer don't have windows this package can't use.
If your computer dont have pythom, you should install this https://www.python.org/downloads/ 

Second
Now you should install cliente_excel.py in your computer and select where install in yours files.
Open the file with notepad and modify ip address and port, if only necessary.
  this your have: 
    url = "opc.tcp://localhost:4840/freeopcua/server/"
  this your modify
    url = "opc.tcp://192.168.1.x:port/freeopcua/server/"

And this your need modify var, modify this type and follow the sentence the code.

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
