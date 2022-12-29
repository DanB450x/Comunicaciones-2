from cProfile import label
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from CifradoHill import CifradoHill
from CifradoCesar import CifradoCesar
from CifradoPropio import CifradoPropio
from Descifrado import Descifrado
import random
import os
import time
import serial
import sys

raiz = Tk()

raiz.title("DISPOSITIVO 2")

raiz.iconbitmap("C:\\Users\\YASMIN\\Desktop\\ProyectoComunicaciones2\\img_proyecto.ico")


#Boton para refrescar la pantalla---------------------------------------------------------------------------------------------------------------------   


def Refrescar():  

        ser = serial.Serial('COM3', 57600, timeout=1)
        timeout = time.time() + 10   # 5 minutes from now
        while True:
            test = 0        
            try:
                d=ser.read(57600)
                d=d.decode('utf-8')
                if d != "":
                    recibo_serial = d
                print(d)
            except (SystemExit, KeyboardInterrupt):
                ser.close()
                sys.exit(0)  
            if test == 10 or time.time() > timeout:
                break
            test = test - 1

        #!/usr/bin/env python           
        print(recibo_serial)

        MensajeMostrado = Descifrado(recibo_serial)
        #print(MensajeMostrado)
        Label(raiz,text = MensajeMostrado ,bg = "red", font=("Comic Sans MS", 15)).grid(column=3, row=3, padx=50, pady=5)
        NombreArchivo = "ArchivoRecibido"
        identificador = len(MensajeMostrado)
        file = open(NombreArchivo+str(identificador), "w")
        file.write(MensajeMostrado +os.linesep)
    
BotonRefrescar = Button (raiz, text = "Recepcion de mensaje",font=("Comic Sans MS", 10), command=Refrescar)
BotonRefrescar.grid(column=4, row=0, padx=50, pady=5)



def Encriptacion(OpcionEscogida, MensajeParaEnviar):
    if OpcionEscogida == "1":
        CifradoCesar(MensajeParaEnviar)
    elif OpcionEscogida == "2":
        CifradoHill(MensajeParaEnviar)
    elif OpcionEscogida == "3":
        CifradoPropio(MensajeParaEnviar)
    else:
        print("No escogio un metodo de encriptacion valido")


#Marco dentro de la vista inicial------------------------------------------------------------------------------------------------------------------

Marco = Frame(raiz, width=1000, height=680)

Marco.config(bg="white")

#Titulo de mensaje recibido-----------------------------------------------------------------------------------------------------------------------

Label(raiz,text = "Mensaje recibido", font=("Comic Sans MS", 15)).grid(column=3, row=2, padx=50, pady=5)


#Area donde se muestra el texto del mensaje recibido-----------------------------------------------------------------------------------------------------------------------

Label(raiz,text = " " , font=("Comic Sans MS", 15)).grid(column=3, row=3, padx=50, pady=5)


def Escoger():
    global EscogerOpcionBox
    Label(raiz,text = "Metodos:", font=("Comic Sans MS", 15)).grid(column=3, row=7, padx=50, pady=5)
    Label(raiz,text = "1. Metodo Cesar", font=("Comic Sans MS", 10)).grid(column=3, row=8, padx=50, pady=5)
    Label(raiz,text = "2. Metodo Hill", font=("Comic Sans MS", 10)).grid(column=3, row=9, padx=50, pady=5)
    Label(raiz,text = "3. Metodo propio", font=("Comic Sans MS", 10)).grid(column=3, row=10, padx=50, pady=5)
    Label(raiz,text = "Escoga una opcion: ", font=("Comic Sans MS", 8)).grid(column=3, row=11, padx=2, pady=5)
    EscogerOpcionBox = Text(raiz, font=("Comic Sans MS", 12), width=10, height=1)
    EscogerOpcionBox.grid(column=3, row=12, padx=2, pady=5)

    #Titulo para enviar un archivo----------------------------------------------------------------------------------------------------------------------

    Label(raiz,text = "Enviar archivo de texto", font=("Comic Sans MS", 15)).grid(column=0, row=6, padx=50, pady=5)

    #Boton para seleccionar archivos y enviarlos--------------------------------------------------------------------------------------------------------
    texto = []
    def ObtenerTexto():
        files_select_event = filedialog.askopenfilename()
        with open(files_select_event,"r") as archivo:
            for linea in archivo:
                texto.append(linea)
            resultado = ' '.join(texto) 
            texto.clear()   
        Opcion = EscogerOpcionBox.get("1.0",'end-1c')
        MensajeParaEnviar = resultado    
        return Encriptacion(Opcion, MensajeParaEnviar)

    def EnviarArchivos():
        Contenido = messagebox.showinfo("Mensaje enviado", "Se envio el documento")

    BotonEnviarArchivo = Button (raiz, text = "Seleccionar archivo",font=("Comic Sans MS", 10), command=ObtenerTexto)
    BotonEnviarArchivo.grid(column=0, row=7, padx=50, pady=20)


    def IngresarMensaje():
        global EscogerOpcionBox
#Titulo de enviar mensaje-------------------------------------------------------------------------------------------------------------------------

        Label(raiz,text = "Enviar mensaje", font=("Comic Sans MS", 15)).grid(column=4, row=7, padx=50, pady=5)

#Cuadro de texto para ingresar el mensaje que se quiere enviar-------------------------------------------------------------------------------------

        MensajeParaEnviarBox = Text(raiz, font=("Comic Sans MS", 12), width=30, height=5)
        MensajeParaEnviarBox.grid(column=4, row=8, padx=50, pady=5)

#Boton para enviar un mensaje-----------------------------------------------------------------------------------------------------------------------

        def EnviarMensaje():
            Opcion = EscogerOpcionBox.get("1.0",'end-1c')
            MensajeParaEnviar = MensajeParaEnviarBox.get("1.0",'end-1c')
            return Encriptacion(Opcion, MensajeParaEnviar)

#Boton para ingresar el texto que se desea enviar----------------------------------------------------------------------------------------------------------------- 

        BotonEnviarMensaje = Button (raiz, text = "Enviar",font=("Comic Sans MS", 10), command=EnviarMensaje)
        BotonEnviarMensaje.grid(column=4, row=9, padx=50, pady=5)

#Boton para ingresar la opcion de encriptacion---------------------------------------------------------------------------------------------------------------------

    BotonEscogerOpcion = Button (raiz, text = "Escoger",font=("Comic Sans MS", 10), command=IngresarMensaje)
    BotonEscogerOpcion.grid(column=3, row=13, padx=50, pady=5)

#Boton para responder mensaje recibido-------------------------------------------------------------------------------------------------------------

BotonResponderMensaje = Button (raiz, text = "Responder/Enviar archivo",font=("Comic Sans MS", 10), command=Escoger)
BotonResponderMensaje.grid(column=3, row=6, padx=50, pady=5)


#Notificacion si se ha recibido un archivo----------------------------------------------------------------------------------------------------------

Label(raiz,text = "Ver archivos recibidos",fg="blue", font=("Comic Sans MS", 15)).grid(column=0, row=2, padx=50, pady=20)

#Ver contenido de archivos recibidos--------------------------------------------------------------------------------------------------------
def MostrarContenido(TextoDelArchivo):
    Contenido = messagebox.showinfo("Contenido del documento", TextoDelArchivo)   
texto = []

def ObtenerTexto():
    files_select_event = filedialog.askopenfilename()
    with open(files_select_event,"r") as archivo:
        for linea in archivo:
            texto.append(linea)
        resultado = ' '.join(texto) 
        texto.clear()   
    return MostrarContenido(resultado)  


#Si se ha recibido un archivo, se podra ver el texto dentro de el--------------------------------------------------------------------------------

BotonVerArchivoRecibido = Button (raiz, text = "Seleccionar archivo",font=("Comic Sans MS", 10), command=ObtenerTexto)
BotonVerArchivoRecibido.grid(column=0, row=3, padx=50, pady=20)


#Ciclo para mantener la aplicacion funcionando-------------------------------------------------------------------------------------------------------

raiz.mainloop()

