def SepararEntrada(numeros, matriz, filas,f):
    c = 0  
    cantidad = len(numeros)
    numero = ""
    
    for i in range(cantidad):
        if numeros[i] != " ":
            numero += numeros[i]
        else: 
            matriz[f][c] = numero
            numero = ""
            c += 1
    if i == cantidad-1:
        matriz[f][c] = numero
    f += 1
    return matriz, f

def MatrizTriangular(matriz, filas):
    #Abajo
    respuesta_1 = "SI"
    for i in range(1,filas,1):
        for j in range(0,i,1):
            if matriz[i][j] != "0":
                respuesta_1 = "NO" 
    #Arriba
    respuesta_2 = "SI" 
    k=1
    for i in range(0,filas-1,1):
        for j in range(k,filas,1):
            if matriz[i][j]!="0":
                respuesta_2 = "NO"
        k+=1 
    if respuesta_1 == "SI" or respuesta_2 == "SI":
        return "SI"
    else: 
        return "NO"
#Algoritmo
bandera = True
while bandera:
    filas = int(input())
    if (filas != 0 and filas < 50):
        matriz = [[""]*filas for i in range(filas)]
        f = 0
        for i in range(filas):
            numeros = input()
            matriz,f = SepararEntrada(numeros, matriz,filas, f)
        respuesta =  MatrizTriangular(matriz, filas)
        print(respuesta)
    else:
        bandera = False
