from dataclasses import replace
from itertools import count
import random
from tabulate import tabulate
import math
import numpy as np
from re import A

import time
import serial



def Descifrado(RafagaDeBits):
    TramaRecibida = RafagaDeBits
    TramaRecibidaArreglo = []
    for bit in TramaRecibida:
        TramaRecibidaArreglo.append(bit)
    ContadorBits = 0
    CaracterBit = ""
    CaracteresArreglo = []
    for i in range(0,len(TramaRecibida),1):
        CaracterBit = CaracterBit + TramaRecibidaArreglo[i]
        ContadorBits = ContadorBits + 1
        if(ContadorBits == 13):
            CaracteresArreglo.append(CaracterBit)
            CaracterBit = ""
            ContadorBits = 0
    mres = CaracteresArreglo



    c2 = 0
    decf = []
    strr = str()
    numm = []
    while c2 != len(mres):
        pt = []  # Posicion
        for w in range(len(mres)):
            ee = str(mres[w])
            
            for a in range(len(ee)):
                g = ee[a]
                pt.append(g)
            h = str(pt[0]) + str(pt[1]) + str(pt[2]) + str(pt[3]) + str(pt[5]) + str(pt[6]) + str(pt[7]) + str(pt[9])
            hhh = int(h, 2)
                
            numm.append(hhh)
            hh = chr(int(h, 2))
            
            decf.append(hh)
            strr = strr + str(hh)
            c2 = c2 + 1
            pt.clear()

    recibo = strr
    print(recibo)
    num = []
    #for a in range(len(recibo_serial)):#
    for a in range(len(recibo)):
                #n = recibo_serial[a]
                n = recibo[a]
                num.append(n)
                    #print("")
                    #print("Mensaje como arreglo: ")
                    #print(num)
                dec = []
                for a in range(len(num)):
                    n = ord(num[a])
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
                ms = []
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
                                    
                        ms.append(d)
                    n = n + 1
                    #print("")
                    #print("Cantidad de Caracteres: ", n)
                    #print("")
                    #print("Código Hamming")
                    #print(np.reshape(ms,(-1,1)))
                    #print("")
    # Error Aleatorio
                w = 0
                msr = []
                resp = []
                p = 0
                while w != len(ms):
                    for w in range(len(ms)):
                        t = str(ms[w])
                        tt = []
                        for a in range(len(t)):
                            g = t[a]
                            tt.append(g)
                        u = [0, 1]
                        i = random.choice(u)
                        ii = random.randrange(12)
                        tt[ii] = i
                    
                        tp = (str(tt[0]) + str(tt[1]) + str(tt[2]) + str(tt[3]) + str(tt[4]) + str(tt[5])
                            + str(tt[6]) + str(tt[7]) + str(tt[8]) + str(tt[9]) + str(tt[10]) + str(tt[11]) + str(tt[12]))
                
                        msr.append(tp)



                        resp.append([])

                        f = tp
                        resp[p].append(f)
                        p = p + 1
                    w = w + 1

                #print("Mensaje con error ", msr)
                #print("")
    # Detección y Corrección de Error
                # Primero comprobaremos el bit de pariedad P0
                # msr el mensaje con error
                # Se calcula P0 de nuevo
                # Validacion de Correccion
                ct = 0
                pp = 0

                mres = []
    #AQUI ES EL CAMBIO MSR=101010101011010#

                while ct != len(msr):
                    ps = []  # Posicion
                    for w in range(len(msr)):
                        t = str(msr[w])
                        
                        for a in range(len(t)):
                            g = t[a]
                            ps.append(g)
                        # Factor de Paridad 0
                        poc = (int(ps[0]) + int(ps[1]) + int(ps[2]) + int(ps[3]) + int(ps[4]) + int(ps[5]) + int(ps[6]) + int(ps[7]) +
                            int(ps[8]) + int(ps[9]) + int(ps[10]) + int(ps[11]))
                        # Verifica si Hay error o con al Factor de Pariedad 0
                        tmpor = 0
                    
                        if poc % 2 == 0:
                            # print("Par")
                            tmpor = 0
                        elif poc % 2 != 0:
                            # print("impar")
                            tmpor = 1
                        
                        if tmpor == int(ps[12]):
                            ct = ct + 1
                            mres.append(msr[w])
                            ps.clear()
                            resp[pp].append("No hay error")
                            resp[pp].append(t)
                            pp = pp + 1

                        elif tmpor != int(ps[12]):
                        
                            #print("")
                            #print("Error Encontrado Iniciando corrección")
                            
                            # Calculamos de nuevo los Factores de Pariedad 1, 2, 4, 8
                            p1c = int(ps[9]) + int(ps[7]) + int(ps[5]) + int(ps[3]) + int(ps[1])
                            p2c = int(ps[9]) + int(ps[6]) + int(ps[5]) + int(ps[2]) + int(ps[1])
                            p4c = int(ps[7]) + int(ps[6]) + int(ps[5]) + int(ps[0])
                            p8c = int(ps[3]) + int(ps[2]) + int(ps[1]) + int(ps[0])
                            # Les asignamos una matriz para mas facil trabajo
                            mem = [p8c, p4c, p2c, p1c]
                            # Creamos la matriz que si contendra el valor 0 u 1 del Factor de pariedad, Factorres de Pariedad calculados
                            memb = []
                            
                            for o in range(len(mem)):
                                if mem[o] % 2 == 0:
                                    k = 0
                                    memb.append(k)
                                elif mem[o] % 2 != 0:
                                    k = 1
                                    memb.append(k)

                            msrp = [int(ps[4]), int(ps[8]), int(ps[10]), int(ps[11])]
                            # Factores de pariedad enviados
                            
                            if memb[3] == int(ps[11]) and memb[2] == int(ps[10]) and memb[1] == int(ps[8]) and memb[0] == int(ps[4]):
                                print("el error se encuentre en P0, es decir posicion 0")
                            
                            else:
                                #Enumeramos los casos de error
                                #Error en la posicion 1
                                if msrp[3] != memb[3] and msrp[1] == memb[1] and msrp[2] == memb[2] and msrp[0] == memb[0]:
                                    #print("Error encontrado en la posicion 1")
                                    
                                    if ps[11] == "0":
                                        ps[11] = "1"
                                    else:
                                        ps[11] = "0"
                                    resp[pp].append("1")
                                # Error en la Posicion 2
                                elif msrp[2] != memb[2] and msrp[0] == memb[0] and msrp[1] == memb[1] and msrp[3] == memb[3]:
                                    
                                    if ps[10] == "0":
                                        ps[10] = "1"
                                    else:
                                        ps[10] = "0"
                                    resp[pp].append("2")
                                # Error en la Posicion 3
                                elif msrp[3] != memb[3] and msrp[2] != memb[2] and msrp[1] == memb[1] and msrp[0] == memb[0]:
                                    
                                    if ps[9] == "0":
                                        ps[9] = "1"
                                    else:
                                        ps[9] = "0"
                                    resp[pp].append("3")
                                # Error en la Posicion 4
                                elif msrp[1] != memb[1] and msrp[0] == memb[0] and msrp[2] == memb[2] and msrp[3] == memb[3]:
                                    #print("Error encontrado en la posicion 4")
                                    
                                    if ps[8] == "0":
                                        ps[8] = "1"
                                    else:
                                        ps[8] = "0"
                                    resp[pp].append("4")
                                # Error en la Posicion 5
                                elif msrp[3] != memb[3] and msrp[1] != memb[1] and msrp[2] == memb[2]:
                                    #print("Error encontrado en la posicion 5")
                                    if ps[7] == "0":
                                        ps[7] = "1"
                                    else:
                                        ps[7] = "0"
                                    resp[pp].append("5")
                                # Error en la Posicion 6
                                elif msrp[2] != memb[2] and msrp[1] != memb[1] and msrp[3] == memb[3]:
                                    #print("Error encontrado en la posicion 6")
                                    if ps[6] == "0":
                                        ps[6] = "1"
                                    else:
                                        ps[6] = "0"
                                    resp[pp].append("6")
                                # Error en la posicion 7
                                elif msrp[3] != memb[3] and msrp[2] != memb[2] and msrp[1] != memb[1]:
                                    #print("Error encontrado en la posicion 7")
                                    if ps[5] == "0":
                                        ps[5] = "1"
                                    else:
                                        ps[5] = "0"
                                    resp[pp].append("7")
                                # Error en posicion 8
                                elif msrp[0] != memb[0] and msrp[1] == memb[1] and msrp[2] == memb[2] and msrp[3] == memb[3]:
                                    #print("Error encontrado en la posicion 8")
                                    if ps[4] == "0":
                                        ps[4] = "1"
                                    else:
                                        ps[4] = "0"
                                    resp[pp].append("8")
                                # Error en la posicion 9
                                elif msrp[3] != memb[3] and msrp[0] != memb[0] and msrp[2] == memb[2] and msrp[1] == memb[1]:
                                    #print("Error encontrado en la posicion 9")
                                    if ps[3] == "0":
                                        ps[3] = "1"
                                    else:
                                        ps[3] = "0"
                                    resp[pp].append("9")
                                # Error en la posicion 10
                                elif msrp[2] != memb[2] and msrp[0] != memb[0] and msrp[3] == memb[3] and msrp[1] == memb[1]:
                                    #print("Error encontrado en la posicion 10")
                                    if ps[2] == "0":
                                        ps[2] = "1"
                                    else:
                                        ps[2] = "0"
                                    resp[pp].append("10")
                                # Error en la posicion 11
                                elif msrp[3] != memb[3] and msrp[2] != memb[2] and msrp[0] != memb[0]:
                                    #print("Error encontrado en la posicion 11")
                                    if ps[1] == "0":
                                        ps[1] = "1"
                                    else:
                                        ps[1] = "0"
                                    resp[pp].append("11")
                                # Error en la posicion 12
                                elif msrp[1] != memb[1] and msrp[0] != memb[0]:
                                    #print("Error encontrado en la posicion 12")
                                    if ps[0] == "0":
                                        ps[0] = "1"
                                    else:
                                        ps[0] = "0"
                                    resp[pp].append("12")
                                gg = (str(ps[0]) + str(ps[1]) + str(ps[2]) + str(ps[3]) + str(ps[4]) + str(ps[5])
                                    + str(ps[6]) + str(ps[7]) + str(ps[8]) + str(ps[9]) + str(ps[10]) + str(ps[11]) + str(ps[12]))
                                #print("Mensaje Corregido", gg)
                                mres.append(gg)
                                ps.clear()
                                resp[pp].append(gg)
                                ct = ct + 1
                                pp = pp + 1

    print(tabulate(resp, headers=['Hamming Enviada con Error', "Bit de Error", "Hamming Recibido y Corregido"], tablefmt='rst', showindex=True))
                
    c2 = 0
    decf = []
    strrDG2 = str()
    numm = []
    while c2 != len(mres):
        pt = []  # Posicion
        for w in range(len(mres)):
            ee = str(mres[w])
            for a in range(len(ee)):
                g = ee[a]
                pt.append(g)
            h = str(pt[0]) + str(pt[1]) + str(pt[2]) + str(pt[3]) + str(pt[5]) + str(pt[6]) + str(pt[7]) + str(pt[9])
                                        
            hhh = int(h, 2)
                        
            numm.append(hhh)
            hh = chr(int(h, 2))
                        
            decf.append(hh)
            strrDG2 = strrDG2 + str(hh)
            c2 = c2 + 1
            pt.clear()
        print("")
    textos = strrDG2
    def extraer_caracter(cadena,n=1):
        if n * 2 <= len(cadena):
            return cadena[:n]
        else:
            return ''       
    recibo=textos[1:]
    opcion_escogida = extraer_caracter(textos)

    #DESCIFRADO HILL--------------------------------------------------------------------------------------------------------------------------------------
            #en esta línea incia del descifrado
    if(opcion_escogida == "h"):
            s_numeros = ["0 ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10 ", "11 ", "12 ", "13 ", "14 ", "15 ", "16 ", "17 ", "18 ", "19 ", "20 ", "21 ", "22 ", "23 ", "24 ", "25 ", "26 ","27 ","28 "]
            s_letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","/","?"]   
            mensaje_codificado = recibo
            arreglo_llave = [1,2,3,0,4,5,1,0,6]
            matriz_llave = []
            longitud_matriz_llave = int((len(arreglo_llave))**(1/2))
            f = longitud_matriz_llave
            c = longitud_matriz_llave

            for i in range(f):
                        matriz_llave.append([0]*c) 
            contador1 = 0
            for filas in range(f):
                for columnas in range(c):
                    matriz_llave[filas][columnas] = arreglo_llave[contador1]
                    contador1 = contador1 + 1
            #print(matriz_llave)

            matriz_llave_inversa = np.linalg.inv(matriz_llave)
            #print(matriz_llave_inversa)
            determinante_inverso = int(np.linalg.det(matriz_llave_inversa)**(-1))
            #print(determinante_inverso)

            for numero in range(0,1000,1):
                if(numero*determinante_inverso%29 == 1):
                    numero_buscado = numero
                    break
            #print(numero_buscado)

            for filas in range(f):
                for columnas in range(c):
                    matriz_llave_inversa[filas][columnas] = round(matriz_llave_inversa[filas][columnas]*determinante_inverso*numero_buscado)
                    
            #print(matriz_llave_inversa)

            for filas in range(f):
                for columnas in range(c):
                    matriz_llave_inversa[filas][columnas] = matriz_llave_inversa[filas][columnas]%29

            #print(matriz_llave_inversa)

            def crypt(text): 
                        contador = 0
                        tex = text
                        while contador < 29:  
                            tex = tex.replace(s_letras[contador], s_numeros[contador])
                            contador = contador + 1 
                            text = tex.split(' ')
                            text.pop()         
                        return text

            texto_numerico_codificado = crypt(mensaje_codificado)
            for i in range(0,len(texto_numerico_codificado),1):
                texto_numerico_codificado[i] = int(texto_numerico_codificado[i])
            #print(texto_numerico_codificado)


            mensaje_numeros_matriz_codificado = []
            if(f == 2):
                filas_matriz_mensaje_codificado = 2
                if(len(texto_numerico_codificado)%2 != 0):
                    columnas_matriz_mensaje_codificado = int(len(texto_numerico_codificado)/2) + 1
                elif(len(texto_numerico_codificado)%2 == 0):
                    columnas_matriz_mensaje_codificado = int(len(texto_numerico_codificado)/2) 
            elif(f == 3):
                filas_matriz_mensaje_codificado = 3
                if(len(texto_numerico_codificado)%3 != 0):
                    columnas_matriz_mensaje_codificado = int(len(texto_numerico_codificado)/3) + 1
                elif(len(texto_numerico_codificado)%3 == 0):
                    columnas_matriz_mensaje_codificado = int(len(texto_numerico_codificado)/3) 

            mensaje_numeros_matriz_codificado = np.zeros((filas_matriz_mensaje_codificado,columnas_matriz_mensaje_codificado),dtype= int)
            #print(mensaje_numeros_matriz_codificado)

            co = 0
            for c in range(0,columnas_matriz_mensaje_codificado,1):
                for f in range(0,filas_matriz_mensaje_codificado,1):
                    if(co < len(texto_numerico_codificado)):
                        mensaje_numeros_matriz_codificado[f][c] = texto_numerico_codificado[co]
                        co = co + 1
                    else:
                        mensaje_numeros_matriz_codificado[f][c] = 0

            #print(mensaje_numeros_matriz_codificado)



            matrizresultado = []
            for k in range(0,len(texto_numerico_codificado),1):
                matrizresultado.append(0)
            #print(matrizresultado)

            t = 0
            for col in range(0,columnas_matriz_mensaje_codificado,1):
                        for f in range(0,longitud_matriz_llave,1):
                            if(t == len(texto_numerico_codificado)):
                                break
                            else:
                                for c in range(0,longitud_matriz_llave,1):
                                    matrizresultado[t] = int(matrizresultado[t] + mensaje_numeros_matriz_codificado[c][col]*matriz_llave_inversa[f][c])
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
            m = 0
            s_numeros2 = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28"]
            for x in range(0,len(matrizresultado),1):
                for m in range(0,29,1):
                    if(matrizresultado[x] == s_numeros2[m]):
                        matrizresultado[x] = s_letras[m]
                        if(matrizresultado[x] == "/"):
                            matrizresultado[x] = " "
                        else:
                            matrizresultado[x] = s_letras[m]
                #print(matrizresultado[x])


            resultado_textoDH = "".join(matrizresultado)
            
            MensajeDescifrado = resultado_textoDH
            
    #DESCIFRADO CESAR--------------------------------------------------------------------------------------------------------------------------------------
    elif(opcion_escogida == "c"):
            
            print(" ")
            desplazamiento = 3
            print(" ")
            abc="abcdefghijklmnñopqrstuvwxyz"

            def cifrado_genDC(cadena, accion, desplazamiento=3 ):
                if accion=="d":
                    desplazamiento=desplazamiento*-1
                texto_cifradoDC = ""
                for letra in cadena:
                    posicion=abc.find(letra)
                    if posicion==-1:
                        texto_cifradoDC=texto_cifradoDC+letra
                    else: 
                        posicion_final=(posicion+desplazamiento)% len(abc)
                        nueva_letra=abc[posicion_final]
                        texto_cifradoDC+=nueva_letra

                return texto_cifradoDC

            def descifreDC(cadena_cifrada, desplazamiento=3):
                return cifrado_genDC(cadena_cifrada,"d", desplazamiento)


            desplazamiento=desplazamiento
            frase= recibo
            texto_cifradoDC=" " 

            texto_cifradoDC = descifreDC(frase, desplazamiento)
            #print("")
            #print(f"Mensaje Recibido y Descifrado: {texto_cifradoDC}")
            #print("---------------------------------------------------------------------------------")
            MensajeDescifrado = texto_cifradoDC

    #DESCIFRADO GRUPO2--------------------------------------------------------------------------------------------------------------------------------------
    if(opcion_escogida == "p"):

            print(" ")
            desplazamiento2 = 5
            print(" ")
            def cifrado_genGRU(cadena1, accion1, desplazamiento1=3 ):
                                        if accion1=="d1":
                                            desplazamiento1=desplazamiento1*-1
                                        texto_cifrado1 = ""
                                        for letra1 in cadena1:
                                            posicion1=abc.find(letra1)
                                            if posicion1==-1:
                                                texto_cifrado1=texto_cifrado1+letra1
                                            else: 
                                                posicion_final1=(posicion1+desplazamiento1)% len(abc)
                                                nueva_letra1=abc[posicion_final1]
                                                texto_cifrado1+=nueva_letra1

                                        return texto_cifrado1
            def descifreGRU(cadena_cifrada1, desplazamiento1=3):
                    return cifrado_genGRU(cadena_cifrada1,"d1", desplazamiento1)
            k1=recibo
            desplazamiento1 = desplazamiento2
            txt = []
            rpl3 =  ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            rpln3 = ["f", "i", "j", "o", "g", "a", "n", "e", "m", "u", "s", "$", "%", "/", "5", "8", "!", "&", "_", "#", "7", "3", "4", "@", "°", "*", "+"]
            txtn =[]

            for a in range(len(k1)):
                u = k1[a]
                txtn.append(u)

            #print(txtn)
            ryu = []
            for x in range(len(txtn)):
                n = txtn[x]
                ryu.append(n)
                for y in range(len(rpln3)):
                    if txtn[x] == rpln3[y]:
                        z = rpl3[y]
                        ryu[x] = z
            #print(ryu)
            b = ""
            for rr in range(len(ryu)):
                b = b + str(ryu[rr])
            # Segunda parte D
            abc="abcdefghijklmnñopqrstuvwxyz"
            frase1=b
            texto_cifrado1=" "
            texto_cifrado1 = descifreGRU(frase1, desplazamiento1)

            #print("")
            #print(f"Mensaje Recibido y Descifrado: {texto_cifrado1}")
            MensajeDescifrado = texto_cifrado1
            #print("---------------------------------------------------------------------------------") 
    return MensajeDescifrado