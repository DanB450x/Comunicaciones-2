from dataclasses import replace
from itertools import count
import random
import sys
from urllib.request import HTTPPasswordMgrWithDefaultRealm
from tabulate import tabulate
import math
import numpy as np
from re import A
import time
import serial

def CifradoCesar(TextoParaCifrar):
            abc="abcdefghijklmnñopqrstuvwxyz"
            def cifrado_genCC(cadena, accion, desplazamiento=3 ):
                if accion=="d":
                    desplazamiento=desplazamiento*-1
                texto_cifradoCC = ""
                for letra in cadena:
                    posicion=abc.find(letra)
                    if posicion==-1:
                        texto_cifradoCC=texto_cifradoCC+letra
                        
                    else: 
                        posicion_final=(posicion+desplazamiento)% len(abc)
                        nueva_letra=abc[posicion_final]
                        texto_cifradoCC+=nueva_letra

                return texto_cifradoCC


            def cifreCC(cadena, desplazamiento=3):
                return cifrado_genCC(cadena,"cifrado", desplazamiento)
            print(" ")
            desplazamiento = 3
            print(" ")
            frase=TextoParaCifrar
            texto_cifradoCC=" " 

            texto_cifradoCC = cifreCC(frase, desplazamiento)
            texto_cifradoCC="c"+texto_cifradoCC

            #print(f"Mensaje Cifrado: {texto_cifrado}")   
    #INICIO DE MENSAJE CIFRADO A CODIGO HAMMING
            numCCS = []
            for a in range(len(texto_cifradoCC)):
                n = texto_cifradoCC[a]
                numCCS.append(n)
                    #print("")
                    #print("Mensaje como arreglo: ")
                    #print(num)
                dec = []
                for a in range(len(numCCS)):
                    n = ord(numCCS[a])
                    dec.append(n)
                    #print("")
                    #print("Código ASCII: ")
                    #print(dec)
                bn = []
                for a in range(len(dec)):
                    n = np.binary_repr(dec[a], width=8)
                    bn.append(n)
                    #print("")
                    #print("Código ASCII a Binario: ")
                    #print(bn)
                    # bits de paridad
                msCCS = []
                n = 0
                oe = int(0)
                while n != len(bn):
                    for n in range(len(bn)):
                        y = str(bn[n])
                        d = str()
                        tp = []
                        for a in range(len(y)):
                            w = y[a]
                            tp.append(w)
                        for c in range(0, 13, 1):
                            if c == 4:
                                f = int(tp[3]) + int(tp[2]) + int(tp[1]) + int(tp[0])

                                if f % 2 != 0:
                                        d = d + str(1)
                                elif f % 2 == 0:
                                        d = d + str(0)
            
                            elif c == 8:
                                f = int(tp[6]) + int(tp[5]) + int(tp[4]) + int(tp[0])
                                if f % 2 != 0:
                                    d = d + str(1)
                                elif f % 2 == 0:
                                    d = d + str(0)

                            elif c == 10:

                                f = int(tp[7]) + int(tp[5]) + int(tp[4]) + int(tp[2]) + int(tp[1])
                                if f % 2 != 0:
                                        
                                    d = d + str(1)
                                elif f % 2 == 0:
                                    d = d + str(0)


                            elif c == 11:
                                f = int(tp[7]) + int(tp[6]) + int(tp[4]) + int(tp[3]) + int(tp[1])
                                if f % 2 != 0:
                                        
                                    d = d + str(1)
                                elif f % 2 == 0:
                                    d = d + str(0)
                                
                            elif c == 12:
                                f = (int(tp[0]) + int(tp[1]) + int(tp[2]) + int(tp[3]) + int(tp[4]) + int(tp[5]) + int(tp[6])
                                        + int(tp[7]) + int(d[4]) + int(d[8]) + int(d[10]) + int(d[11]))
                                if f % 2 != 0:
                                        
                                    d = d + str(1)
                                elif f % 2 == 0:
                                    d = d + str(0)
                                    

                            elif c == 5:
                                d = d + str(tp[4])
                                    
                            elif c == 6:
                                d = d + str(tp[5])
                                    

                            elif c == 7:
                                d = d + str(tp[6])
                                    

                            elif c == 9:
                                d = d + str(tp[7])
                                    
                            elif c <= 3:
                                d = d + str(tp[c])
                                    
                        msCCS.append(d)
                    n = n + 1
                    
            StrCesar_cad="".join(msCCS)
                            # print("")
                            # print("Cantidad de Caracteres: ", n)
                            # print("")
                            # print("Código Hamming")
                            # print(np.reshape(ms,(-1,1)))
                            # print("")
            #print(StrCesar_cad)

            ser = serial.Serial('COM3', 57600, timeout=1)  # open serial port
            print(ser.name)         # check which port was really used
            try:
                ser.write(StrCesar_cad.encode())
                print("sent \n")
                #time.sleep(0.2)
            except (SystemExit, KeyboardInterrupt) :
                ser.close()             # close port
                sys.exit(0)
