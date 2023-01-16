import random
import time
import platform
import os

DIFICIL = 5
NORMAL = 4
FACIL = 3
CANT_TIEMPOS_TOMADOS = 3
POS_NOMBRE = 0
POS_MOVIMIENTOS = 1
POS_TIEMPO = 2

def crear_matriz(n):
    fil = n
    col = n
    mat = [[0] * col for i in range(fil)]
    return mat

def llenar_matriz(n,mat):
    tope = n*n
    numeros = [i+1 for i in range(tope-1)]
    numeros.append("-")
    col = len(mat[0])
    fil = len(mat)
    cont = 0
    for f in range(fil):
        for c in range(col):
            mat[f][c] = str(numeros[cont])
            cont += 1
            
def imprimir_matriz(mat):
    col = len(mat[0])
    fil = len(mat)
    for f in range(fil):
        for c in range(col):
            print("%3s" %mat[f][c],end=" ")
        print()

def limpiar_pantalla():
   if platform.system() == "Windows":
       os.system("cls")
   else:
       os.system("clear")
        
def dar_fila_columna_con_numero(x,mat):
    col = len(mat[0])
    fil = len(mat)
    colre = -1
    filre = -1
    for f in range(fil):
        for c in range(col):
            if x == mat[f][c]:
                colre = c
                filre = f
    return filre, colre

def movimiento_valido(x,mat):
    es_valido = False
    filnum, colnum = dar_fila_columna_con_numero(x,mat)
    filvacio, colvacio = dar_fila_columna_con_numero("-",mat)
    if (filnum == filvacio - 1 and colnum == colvacio) or (filnum == filvacio + 1 and colnum == colvacio) or (filnum == filvacio and colnum == colvacio - 1) or (filnum == filvacio and colnum == colvacio + 1):
        es_valido = True
    return es_valido

def realizar_movimiento(x,mat):
    filnum, colnum = dar_fila_columna_con_numero(x,mat)
    filvacio, colvacio = dar_fila_columna_con_numero("-",mat)
    auxi = mat[filnum][colnum]
    mat[filnum][colnum] = mat[filvacio][colvacio]
    mat[filvacio][colvacio] = auxi

def verificar_victoria(mat_ver,mat):
    col = len(mat[0])
    fil = len(mat)
    gano_juego = True
    for f in range(fil):
        for c in range(col):
            if mat[f][c] != mat_ver[f][c]:
                gano_juego = False
                break
    return gano_juego

def realizar_movimientos_mezcla(mat,col,fil,mov):
    if mov == 0:
        pass
    else:
        film, colm = dar_fila_columna_con_numero("-",mat)
        mover  = random.choice([1,2,3,4])
        if mover == 1:
            film += 1
        elif mover == 2:
            film -= 1
        elif mover == 3:
            colm += 1
        elif mover == 4:
            colm -= 1
        if film >= 0 and film < fil and colm >= 0 and colm < col:
            realizar_movimiento(mat[film][colm],mat)
        realizar_movimientos_mezcla(mat,col,fil,mov-1)

def mezclar_matriz(mat):
    col = len(mat[0])
    fil = len(mat)
    movimientos = random.randint(150*col,175*col)
    auxi = 0
    realizar_movimientos_mezcla(mat,col,fil,movimientos)
    filvacio, colvacio = dar_fila_columna_con_numero("-",mat)
    while colvacio-1 >= 0:
        realizar_movimiento(mat[filvacio][colvacio-1],mat)
        filvacio, colvacio = dar_fila_columna_con_numero("-",mat)
    while filvacio+1 < fil:
        realizar_movimiento(mat[filvacio+1][colvacio],mat)
        filvacio, colvacio = dar_fila_columna_con_numero("-",mat)
    while colvacio+1 < col:
        realizar_movimiento(mat[filvacio][colvacio+1],mat)
        filvacio, colvacio = dar_fila_columna_con_numero("-",mat)

def pedir_jugada(m):
    while True:        
        try:
            jugada = input("ingrese la jugada:")
            col = len (m[0])
            fil = len (m)
            aux = jugada
            aux = float(aux)
            assert aux >= 1 and aux <= (col*fil) -1, "Error, fuera de rango."
            assert aux % 1 == 0, "No se permite numero con (.)"
            assert movimiento_valido (jugada, m), "Movimiento invalido."
            break
        except ValueError:
            print("No se ingreso un valor valido.")
        except AssertionError as mensaje:
            print (mensaje)
    return jugada        

def preguntar_continuar_jugando():
    while True:
        try:
            print("Ingrese si quiere volver a jugar nuevamente(c), volver a elgir una dificultad(v), o salir(e).")
            respuesta_usuario = input("ingrese lo que quiera hacer:")
            respuesta_usuario = respuesta_usuario.lower()
            opciones_de_teclado = ("c","v","e")
            assert respuesta_usuario in opciones_de_teclado, "No se ingreso un valor valido, intente nuevamente."
            break
        except ValueError:
            print("No se ingreso un valor valido, intente nuevamente.")
        except AssertionError as mensaje:
            print (mensaje)
    return respuesta_usuario

def jugar(mat,mat_ver, dif):
    contador = 0
    seg1 = time.time()
    mezclar_matriz(mat)
    while not verificar_victoria(mat_ver,mat):
        limpiar_pantalla()
        imprimir_matriz(mat)
        jugada = pedir_jugada (mat)
        realizar_movimiento (jugada,mat)
        contador += 1
    limpiar_pantalla()
    seg2 = time.time()
    tiempo = (((seg2-seg1)*100)//1)/100
    imprimir_matriz(mat)
    print("victoria")
    return tiempo,contador
    
def pedir_dificultad():
    while True:        
        try:
            print("Ingrese el tipo de dificultad en la que quiera jugar.")
            print("Facil(F), Normal(N), Dificil(D)")
            print("Info(i) para mostrar las instrucciones.")
            print("Imprimir(v) para mostrar los mejores tiempos")
            dificultad = input("ingrese la dificultad:")
            dificultad = dificultad.lower()
            opciones_de_teclado = ("d","dificil","n","normal","f","facil","info","i","v","imprimir")
            assert dificultad in opciones_de_teclado, "No se ingreso un valor valido, intente nuevamente."
            break
        except ValueError:
            print("No se ingreso un valor valido, intente nuevamente.")
        except AssertionError as mensaje:
            print (mensaje)
    return dificultad
    
def mostrar_instrucciones():
    print("El juego del 15 es un juego de deslizamiento de numeros que presentan un orden acendente dentro de una matriz. ")
    d = crear_matriz(DIFICIL)
    n = crear_matriz(NORMAL)
    f = crear_matriz(FACIL)
    llenar_matriz(DIFICIL,d)
    llenar_matriz(NORMAL,n)
    llenar_matriz(FACIL,f)
    print()
    print("Facil:")
    imprimir_matriz(f)
    print()
    print("Normal:")
    imprimir_matriz(n)
    print()
    print("Dificil:")
    imprimir_matriz(d)
    print()
    print("La matriz estara mezclada y el objetivo del juego es ordenarla en el orden mostrado arriba, para ello el jugador tendra que introducir que numero quiere mover.")
    print("Un ejemplo seria en la matriz facil, dos movimientos legales son (8) y (6). ")
    print("Una vez comenzado el juego, se toma el tiempo que tarda en completarlo, y la cantidad de movimientos. Los mejores tiempos, se guardaran en el archivo Mejores_Tiempos.txt")
    print()

def asignar_dificultad(dif):
    valor = 0
    if dif == "d" or dif == "dificil":
        valor = DIFICIL
    elif dif == "n" or dif == "normal":
        valor = NORMAL
    else:
        valor = FACIL
    return valor

def mostrar_tiempos():
    try:
        arch = open("tiempos.txt","rt")
        dificultad = ("Facil:","Normal:","Dificil:")
        for linea in arch:
            tiempo = 0
            lista = linea.split(";")
            nombre = lista[POS_NOMBRE]
            if len(lista) > 1:
                tiempo = lista[POS_TIEMPO]
                tiempo = tiempo.strip("\n")
                contador_mov = lista[POS_MOVIMIENTOS]
                contador_mov = contador_mov.strip("\n")
            nombre = nombre.strip("\n")
            nombre = nombre.strip(" ")
            if nombre in dificultad:
                print()
                print(nombre)
                print()
            elif nombre.isalnum():
                print(f"{nombre:<5} tiene un tiempo de: {tiempo:<8} segundos, que realizo en {contador_mov:<6} movimentos")
            else:
                print("-----------------------")
        print()
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:", mensaje)
    except OSError as mensaje:
        print("No se puede leer el archivo:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass
        
def pasar_lista_tiempos_dificultad(dif):
    estoy_dificultad = False
    contador = CANT_TIEMPOS_TOMADOS
    lista_tiempos = []
    try:
        arch = open("tiempos.txt","rt")
        dificultad = ("Facil:","Normal:","Dificil:")
        num_dificultad = (FACIL,NORMAL,DIFICIL)
        for linea in arch:
            tiempo = 0
            lista = linea.split(";")
            nombre = lista[POS_NOMBRE]
            if len(lista) > 1:
                tiempo = lista[POS_TIEMPO]
                tiempo = tiempo.strip("\n")
                contador_mov = lista[POS_MOVIMIENTOS]
                contador_mov = contador_mov.strip("\n")
            nombre = nombre.strip("\n")
            if estoy_dificultad and contador > 0:
                lista_tiempos += [nombre + ";" + contador_mov + ";" + tiempo]
                contador -= 1
            if nombre == dificultad[0] and dif == num_dificultad[0] and contador > 0:
                estoy_dificultad = True
            elif nombre == dificultad[1] and dif == num_dificultad[1] and contador > 0:
                estoy_dificultad = True
            elif nombre == dificultad[2] and dif == num_dificultad[2] and contador > 0:
                estoy_dificultad = True 
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:", mensaje)
    except OSError as mensaje:
        print("No se puede leer el archivo:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass
    return lista_tiempos

def verificar_tiempo(tiempo_p,dif):
    tiempo_nuevo = False
    lista_tiempos = pasar_lista_tiempos_dificultad(dif)
    for i in range(len(lista_tiempos)):
        tiempo_elemento = lista_tiempos[i]
        tiempo_elemento = tiempo_elemento.split(";")
        tiempo_elemento = tiempo_elemento[1]
        if tiempo_p < float(tiempo_elemento):
            tiempo_nuevo = True
            break
    return tiempo_nuevo

def ordenar_tiempos(elemento):
    elemento = elemento.split(";")
    elemento = float(elemento[2])
    return elemento

def poner_nuevo_tiempo(nombre,tiempo,cont_mov,dif):
    lista_tiempos = pasar_lista_tiempos_dificultad(dif)
    lista_tiempos += [nombre + ";" + str(cont_mov) + ";" + str(tiempo)]
    lista_tiempos.sort(key=ordenar_tiempos)
    lista_tiempos.pop(len(lista_tiempos)-1)
    contador = CANT_TIEMPOS_TOMADOS
    estoy_dificultad = False
    try:
        leer = open("tiempos.txt","rt")
        escribir = open("tiempos_auxi.txt","wt")
        dificultad = ("Facil:","Normal:","Dificil:")
        num_dificultad = (FACIL,NORMAL,DIFICIL)
        for linea in leer:
            tiempo = 0
            lista = linea.split(";")
            nombre = lista[POS_NOMBRE]
            if len(lista) > 1:
                tiempo = lista[POS_TIEMPO]
                tiempo = tiempo.strip("\n")
            nombre = nombre.strip("\n")
            nombre = nombre.strip(" ")
            if estoy_dificultad and contador > 0:
                elemento = lista_tiempos[CANT_TIEMPOS_TOMADOS-contador]
                escribir.write(elemento + "\n")
                contador -= 1
            else:
                escribir.write(linea)
            if nombre == dificultad[0] and dif == num_dificultad[0] and contador > 0:
                estoy_dificultad = True
            elif nombre == dificultad[1] and dif == num_dificultad[1] and contador > 0:
                estoy_dificultad = True
            elif nombre == dificultad[2] and dif == num_dificultad[2] and contador > 0:
                estoy_dificultad = True 
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:", mensaje)
    except OSError as mensaje:
        print("No se puede grabar el archivo:", mensaje)
    finally:
        
        try:
            leer.close()
            escribir.close()
        except NameError:
            pass
    try:
        escribir = open("tiempos.txt","wt")
        leer = open("tiempos_auxi.txt","rt")
        for linea in leer:
            escribir.write(linea)
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:", mensaje)
    except OSError as mensaje:
        print("No se puede grabar el archivo:", mensaje)
    finally:
        try:
            leer.close()
            escribir.close()
        except NameError:
            pass

def pedir_nombre():
    while True:        
        try:
            nombre = input("Ingrese su nombre (5 caracteres alphanumericos):")
            assert len(nombre) != 0, "Tiene que tener al menos 1 caracter."
            assert len(nombre) <= 5, "Error, fuera de rango, maximo de 5 caracteres."
            assert nombre.isalnum(), "No se permite caracteres que no sean letras o numeros."
            break
        except ValueError:
            print("No se ingreso un valor valido.")
        except AssertionError as mensaje:
            print (mensaje)
    nombre += " "*(5-len(nombre))
    return nombre

continuar_jugando = True
continua_menu = True
while continua_menu:
    dificultades = ("d","dificil","n","normal","f","facil")
    asesor = ("info","i")
    mostrar = ("v","imprimir")
    n = pedir_dificultad()
    if n in asesor:
        mostrar_instrucciones()
    elif n in mostrar:
        mostrar_tiempos()
    elif n in dificultades:
        continuar_jugando = True
        n = asignar_dificultad(n)
        mat = crear_matriz(n)
        matver = crear_matriz(n)
        llenar_matriz(n,matver)
        llenar_matriz(n,mat)
        while continuar_jugando:
            tiempo,cont_mov = jugar(mat,matver,n)
            if verificar_tiempo(tiempo,n):
                print(f"Felicitaciones tu tiempo de:{tiempo:} esta entre los 3 mejores.")
                nombre = pedir_nombre()
                poner_nuevo_tiempo(nombre,tiempo,cont_mov,n)
            else:
                print(f"Tu tiempo de:{tiempo:} no esta entre los 3 mejores.")
            respuesta_usuario = preguntar_continuar_jugando()
            if respuesta_usuario == "v" or respuesta_usuario == "e":
                continuar_jugando = False
            if respuesta_usuario == "v":
                continua_menu = True
            else:
                continua_menu = False
