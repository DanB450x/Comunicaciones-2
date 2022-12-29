from dataclasses import replace
from itertools import count
import random
from urllib.request import HTTPPasswordMgrWithDefaultRealm
from tabulate import tabulate
import math
import numpy as np
from re import A
import time
import serial    
import sys      
           
           
def CifradoPropio(TextoParaCifrar):

    def cifrado_genPRO(cadena2, accion2, desplazamiento2=3 ):
        if accion2=="d":
            desplazamiento2=desplazamiento2*-1
        texto_cifrado2 = ""
        for letra2 in cadena2:
            posicion2=abc.find(letra2)
            if posicion2==-1:
                texto_cifrado2=texto_cifrado2+letra2
            else: 
                posicion_final2=(posicion2+desplazamiento2)% len(abc)
                nueva_letra2=abc[posicion_final2]
                texto_cifrado2+=nueva_letra2

        return texto_cifrado2

    def cifrePRO(cadena2, desplazamiento2=3):
            return cifrado_genPRO(cadena2,"cifrado", desplazamiento2)
    abc="abcdefghijklmnñopqrstuvwxyz"
    frase2=TextoParaCifrar
    print(" ")
    desplazamiento2 = 5
    print(" ")
    texto_cifrado2=" "
    texto_cifrado2 = cifrePRO(frase2, desplazamiento2)
    texto_cifrado2="p"+texto_cifrado2
    # Segunda parte C

    ms_clean2 = texto_cifrado2.replace(".", " ").replace(",", " ").replace(";", " ").replace(":", " ").\
        replace("-", " ").replace("'", " ").replace('"', " ").replace("?", " ").replace("¿", " ").replace("¡", " ")\
        .replace("!", " ").replace("(", " ").replace(")", " ")
    txt2 = []
    for a2 in range(len(ms_clean2)):
        n2 = ms_clean2[a2]
        txt2.append(n2)

    #print(txt2)

    rpl2 =  ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    rpln2 = ["f", "i", "j", "o", "g", "a", "n", "e", "m", "u", "s", "$", "%", "/", "5", "!", "&", "_", "#", "7", "3", "4", "@", "°", "*", "+"]

    chg2 = []

    for x2 in range(len(txt2)):
        n2 = txt2[x2]
        chg2.append(n2)
        
        for y2 in range(len(rpl2)):
            if txt2[x2] == rpl2[y2]:
                z2 = rpln2[y2]
                chg2[x2]= z2

    #print(chg2)

    k2 = ""
    for rr2 in range(len(chg2)):
        k2 = k2 + str(chg2[rr2])

    #print(f"La frase cifrada es: {k2}")
    print("")
#INICIO DE MENSAJE CIFRADO A CODIGO HAMMING
    numCG2 = []
    for a in range(len(k2)):
        n = k2[a]
        numCG2.append(n)
            #print("")
            #print("Mensaje como arreglo: ")
            #print(num)
        dec = []
        for a in range(len(numCG2)):
            n = ord(numCG2[a])
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
        msCG2 = []
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
                            
                msCG2.append(d)
            n = n + 1
            
    StrGrupo2_cad="".join(msCG2)
                    # print("")
                    # print("Cantidad de Caracteres: ", n)
                    # print("")
                    # print("Código Hamming")
                    # print(np.reshape(ms,(-1,1)))
                    # print("")
    #print(StrGrupo2_cad)

    ser = serial.Serial('COM3', 57600, timeout=1)  # open serial port
    print(ser.name)         # check which port was really used
    try:
        ser.write(StrGrupo2_cad.encode())
        print("sent \n")
        #time.sleep(0.2)
    except (SystemExit, KeyboardInterrupt) :
        ser.close()             # close port
        sys.exit(0)