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
         


def CifradoHill(TextoParaCifrar):      
            TextH=TextoParaCifrar
            TextH = TextH.replace(' ','/')  
            s_numeros = ["0 ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10 ", "11 ", "12 ", "13 ", "14 ", "15 ", "16 ", "17 ", "18 ", "19 ", "20 ", "21 ", "22 ", "23 ", "24 ", "25 ", "26 ","27 ","28 "]
            s_letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","/","?"]  
            
            def crypt(text): 
                contador = 0
                tex = text
                while contador <29:  
                    tex = tex.replace(s_letras[contador], s_numeros[contador])
                    contador = contador + 1 
                    text = tex.split(' ')
                    text.pop()         
                return text
            
            texto_numerico = crypt(TextH)
            for i in range(0,len(texto_numerico),1):
                texto_numerico[i] = int(texto_numerico[i])
            #print(texto_numerico)
            
            matriz1 = []    
        
            filas_llave = 3
            columnas_llave = 3
            arreglo_llave = []
            
            for i in range(filas_llave):
                matriz1.append([0]*columnas_llave)  
            
            matriz1 = [[1,2,3],[0,4,5],[1,0,6]]
            
            mensaje_numeros_matriz = []
            if(filas_llave == 2):
                filas_matriz_mensaje = 2
                if(len(texto_numerico)%2 != 0):
                    columnas_matriz_mensaje = int(len(texto_numerico)/2) + 1
                elif(len(texto_numerico)%2 == 0):
                    columnas_matriz_mensaje = int(len(texto_numerico)/2) 
            elif(filas_llave == 3):
                filas_matriz_mensaje = 3
                if(len(texto_numerico)%3 != 0):
                    columnas_matriz_mensaje = int(len(texto_numerico)/3) + 1
                elif(len(texto_numerico)%3 == 0):
                    columnas_matriz_mensaje = int(len(texto_numerico)/3) 

            mensaje_numeros_matriz = np.zeros((filas_matriz_mensaje,columnas_matriz_mensaje),dtype= int)
            #print(mensaje_numeros_matriz)

            co = 0
            for c in range(0,columnas_matriz_mensaje,1):
                for f in range(0,filas_matriz_mensaje,1):
                    if(co < len(texto_numerico)):
                        mensaje_numeros_matriz[f][c] = texto_numerico[co]
                        co = co + 1
                    else:
                        mensaje_numeros_matriz[f][c] = 27

            #print(mensaje_numeros_matriz)
            
            posiciones_requeridas = -10
            numero = 0
            
            while(posiciones_requeridas < 0):
                numero*3 - len(texto_numerico)
                posiciones_requeridas = numero*3 - len(texto_numerico)
                numero = numero + 1
                #print(posiciones_requeridas)
                

        
            filas_texto = filas_llave

            filas = filas_texto

            matrizresultado = []
            for k in range(0,len(texto_numerico) + posiciones_requeridas,1):
                matrizresultado.append(0)
            #print(matrizresultado)

        
            t = 0
            for col in range(0,columnas_matriz_mensaje,1):
                for f in range(0,filas_llave,1):
                    for c in range(0,columnas_llave,1):
                        matrizresultado[t] = int(matrizresultado[t] + mensaje_numeros_matriz[c][col]*matriz1[f][c])
                    t = t + 1
            
            #print(matrizresultado)
            j = 0
            for n in matrizresultado:
                residuo = n%29
                if(n < 29):
                    n = str(n)
                else:
                    n = str(n%29)
                matrizresultado[j] = n
                j = j + 1
            #print(matrizresultado)

            contador = 0
            s_numeros2 = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28"]
            for x in range(0,len(matrizresultado),1):
                for t in range(0,29,1):
                    if(matrizresultado[x] == s_numeros2[t]):
                        matrizresultado[x] = s_letras[t]
                #print(matrizresultado[x])

            
            resultado_textoCH = "".join(matrizresultado)
            resnuev="h"+resultado_textoCH
            '''print(resultado_texto)
            print("")
            print("Mensaje Cifrado: ", resnuev)
            print("")'''
            numCH = []
            for a in range(len(resnuev)):
                n = resnuev[a]
                numCH.append(n)
                    #print("")
                    #print("Mensaje como arreglo: ")
                    #print(num)
                dec = []
                for a in range(len(numCH)):
                    n = ord(numCH[a])
                    dec.append(n)
                bn = []
                for a in range(len(dec)):
                    n = np.binary_repr(dec[a], width=8)
                    bn.append(n)
                msCH = []
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
                                    
                        msCH.append(d)
                    n = n + 1
                    
            StrHamming_cad="".join(msCH)
                            # print("")
                            # print("Cantidad de Caracteres: ", n)
                            # print("")
                            # print("Código Hamming")
                            # print(np.reshape(ms,(-1,1)))
                            # print("")
            #print(StrHamming_cad)
            
            ser = serial.Serial('COM3', 57600, timeout=1)  # open serial port
            print(ser.name)         # check which port was really used
            try:
                ser.write(StrHamming_cad.encode())
                print("sent \n")
                #time.sleep(0.2)
            except (SystemExit, KeyboardInterrupt) :
                ser.close()             # close port
                sys.exit(0)