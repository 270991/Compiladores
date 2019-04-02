#Listas globales
simbolos= ["<=", "<>", ">=", "(", ")", "+", "-", ",", "*", "/", "{", "}", "[", "]", ":=", "="]
reservadas=["main", "integer","string", "variables", "decimal", "for", "if", "false", "while", "cycle","case", "cases","and", "or","not","variables"]
tabla_variables =[]
tablaDeTokens=[]
tabla_constantes=[]
inicio_palabras_reservadas = 500
inicio_simbolos_especiales = 600
inicio_constantes = 700
inicio_identificadores = 800
operadores_ascii = [60,62,40,41,43,45,44,42,47,123,125,91,93,58,46,61,32]
estado_asterisco = [200,201,202,203,204,205,206,207]	
estado_final =[200,201,202,203,204,205,206,207,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315]
def main():
	cadena=[]
	columna=0
	palabra=""
	edo=0
	posicion=0 #fin de linea
     
	lectura = open("datos.txt", "r") #Abriendo archivo para lectura
	while True:
		linea=lectura.readline() #Lectura por línea
		for char in (linea):     #Lectura por caracter
			if ord(char) == 10: # cambia un fin de linea por espacio
				cadena.append(32)  #Guarda el caracter en la lista "cadena" convertido en código ascii
			else:
				cadena.append(ord(char))  #Guarda el caracter en la lista "cadena" convertido en código ascii
		while posicion < len(cadena):
			caracter=cadena[posicion]
			columna=columnas(caracter,operadores_ascii)
			if edo == 0:
				palabra=""                                
			if edo in estado_final:
				edo=0
				palabra=""
			edo=matriz[edo][columna]
			if edo not in estado_asterisco:  
				palabra=palabra+chr(caracter)
				posicion+=1
			salidas(edo,palabra)

		if not linea:  #fin de lectura cuando no encuentra mas lineas
			break
	lectura.close()
	print('Tabla de variables:')
	print(tabla_variables)
	print('Tabla de Token:')
	print(tablaDeTokens)
	print('Tabla de Constantes:')
	print(tabla_constantes)

	
matriz = [     #      0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19       
	      #     dig  E/e  let   <    >    (    )    +    -    ,    *    /    {    }    [    ]    :    .    =   esp
	          [   1, 400,  10,  11,  12, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313,  13, 400, 315,   0], #0 
	          [   1,   2, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,   5, 200, 200], #1  
	          [ 400, 400, 400, 400, 400, 400, 400,   3,   3, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400], #2   
	          [   4, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400], #3  
	          [   4, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201], #4  
	          [   6, 400, 400, 400, 400, 400, 400, 500, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400], #5  
	          [   6,   7, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202], #6    
	          [ 400, 400, 400, 400, 400, 400, 400,   8,   8, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400], #7  
	          [   9, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 500, 400, 400, 400, 400, 400, 400, 400, 400], #8  
	          [   9, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203], #9  
	          [  10, 204,  10, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204], #10  
	          [ 205, 205, 205, 205, 301, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 300, 300], #11     
	          [ 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 302, 206], #12
	          [ 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 314, 207], #13
	         ]

def columnas(caracter,operadores_ascii):
	if caracter >=48 and caracter <=57:
		columna= 0
	else:
		if caracter >=97 and caracter <=122 or caracter >=65 and caracter <=90: #letras
			columna= 2
		else:
			if caracter in operadores_ascii:
				columna= operadores_ascii.index(caracter)+3
			else:
				print('Caracter no valido:'+str(caracter))

	return columna
	
def salidas(edo,palabra):   #función que te muestra la salida
		if edo>=200 and edo <=203: # Registra los numeros a la tabla de constantes
			tabla_constantes.append(palabra)
			ind = tabla_constantes.index(palabra) #obtiene el indice si la constante ya esta en la tabla
			tablaDeTokens.append([inicio_constantes,ind,palabra])
		if edo==204: # Registra los identificadores y las palabras reservadas
			if palabra in reservadas:
				tok= reservadas.index(palabra)+inicio_palabras_reservadas
				tablaDeTokens.append([inicio_palabras_reservadas,tok,palabra])
			else:
				if palabra not in tabla_variables:
					tabla_variables.append(palabra)
					ind = tabla_variables.index(palabra) #obtiene el indice si la variable ya esta en la tabla
					tablaDeTokens.append([inicio_identificadores,ind,palabra])
				else:
					ind  = tabla_variables.index(palabra)
					tablaDeTokens.append([inicio_identificadores,ind,palabra])

		if edo >=205 and edo <=315: #Registra los simbolos especiales
			if palabra in simbolos:
				ind =simbolos.index(palabra)+inicio_simbolos_especiales
				tablaDeTokens.append([inicio_simbolos_especiales,ind,palabra])

		return 0
		
if __name__ == '__main__':
	main()
