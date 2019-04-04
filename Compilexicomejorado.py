#Listas globales
simbolos= ["<=", "<>", ">=", "(", ")", "+", "-", ",", "*", "/", "{", "}", "[", "]", ":=", "=", "<", ">", "."] #lista que almacena los simbolos que puede identificar el automata.
#edos_simbolos=[300,301,302,303, 304,305,306,307,308,309,310,311,312,313,314,315,205,206,207,208,209]
reservadas=["main", "integer","string", "variables", "decimal", "for", "if", "false", "while", "cycle","case", "cases","and", "or","not"] #lista de palabras reservadas que identifica, de acuerdo ala gramatica.
#----tablas necesarias para la separación de tokens.
tabla_variables =[]
tablaDeTokens=[]
tabla_constantes=[]
tabla_comentarios=[]
#----se inicia un indice para cada conjunto que se utiliza para defenir la clasificación de los token.
inicio_palabras_reservadas = 500
inicio_simbolos_especiales = 600
inicio_constantes = 700
inicio_identificadores = 800
inicio_comentarios = 900
#----se clasifican para una mejor manipulación de estados
operadores_ascii = [60,62,40,41,43,45,44,42,47,123,125,91,93,58,46,61,34,32] # lista que guarda los operadoress en codigo ascii
estado_asterisco = [200,201,202,203,204,205,206,207,208]	#Lista que almacena los estados con asterisco
estado_final =[200,201,202,203,204,205,206,207,208,209,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,400] #lista que guarda los estados finales
#---------------------inicio de main.-----------------------------
def main():
	cadena=[] # se utliza uns lista para ir formando el conjunto de caracteres.
	columna=0 # variable que guarda el número de columna
	palabra="" #variable que guarda caracter por caracter para formar una palabra final.
	edo=0     	#variable que itera la matriz.
	posicion=0 #fin de linea
     
	lectura = open("Gramatica.txt", "r") #Abriendo archivo para lectura

	while True:   
		linea=lectura.readline() #Lectura por línea
		for char in (linea):     #Lectura por caracter
			if ord(char) == 10: # cambia un fin de linea por espacio
				cadena.append(32)  #Agrega un espacio al final de la cadena formada para que no se pierda el ultimo caracter leido.
			else:
				cadena.append(ord(char))  #Guarda los caracteres en la lista cadena convertido en código ascii
		while posicion < len(cadena):   #entra al ciclo while mientras la posición está dentro del tamñano de la cadena formada.
			caracter=cadena[posicion]   #se asigna una variable para obtener la posición de la lectura en la cadena.
			columna=columnas(caracter,operadores_ascii)  #obtiene el número de columna, entrando a la función "columnas"
			if edo == 0:   #limpia el estado en cada iteración
				palabra=""   #limpia la variable "palabra" cada que cambia de estado, y después de haber formado una palabra.                         
			if edo in estado_final: #se cumple cuando se encuentra un estado final.
				edo=0
				palabra=""  #limpia la variable nuevamente, después del estado final.
			edo=matriz[edo][columna]  #cambia el estado,  por medio de la columna obtenida.

			if edo not in estado_asterisco:  #entra es condicional si los estados son finales.  
				palabra=palabra+chr(caracter) #concatenación de caracteres para formar la palabra final.
				posicion+=1 #aumentos del número de posición.
			salidas(edo,palabra) #devuelve el resultado utlizando la función salidas.

		if not linea:  #sale del ciclo cuando terminas las lineas de archivo
			break #rompe el ciclo while
	lectura.close() #fin de lectura.

#----------Impresion de resultados.--------------	
	print('Tabla de variables:') 
	print(tabla_variables)
	print('Tabla de Token:')
	print(tablaDeTokens)
	print('Tabla de Constantes:')
	print(tabla_constantes)
	print('Tabla de comentarios:')
	print(tabla_comentarios)
#------------------------------------------------
matriz = [    #      0    1    2    3    4    5    6    7    8    9    10   11   12 13   14   15   16   17   18   19   20      
	      #     dig  E/e  let   <    >    (     )   +    -    ,    *    /   {    }    [    ]    :    .    =    "    esp
	          [   1,  10,  10,  11,  12, 303, 304, 305, 306, 307, 308, 14, 310, 311, 312,  313, 13, 400,  314,  17,   0], #0 
	          [   1,   2, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,200,   5,  200, 200, 200], #1  
	          [ 400, 400, 400, 400, 400, 400, 400,   3,   3, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400], #2   
	          [   4, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400], #3  
	          [   4, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201], #4  
	          [   6, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400], #5  
	          [   6,   7, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202], #6    
	          [ 400, 400, 400, 400, 400, 400, 400,   8,   8, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400], #7  
	          [   9, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 500, 400, 400, 400, 400, 400, 400, 400, 400], #8  
	          [   9, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203, 203], #9  
	          [  10, 204,  10, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204, 204], #10  
	          [ 205, 205, 205, 205, 301, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 205, 300, 205, 205, 205], #11     
	          [ 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 206, 302, 206, 206, 206], #12
	          [ 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 207, 313, 207, 207, 207], #13
	          [ 208, 208, 208, 208, 208, 208, 208, 208, 208, 208,  15, 208, 208, 208, 208, 208, 208, 208, 208, 208, 208], #14
	          [  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  16,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15], #15
	          [  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  15,  315,  15,  15,  15,  15,  15,  15, 15,  15,  15], #16
	          [  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17, 209,  17]  #17
	         ]

def columnas(caracter,operadores_ascii):  #inicio de funsión para ubicar el número de columna dentro de la matriz
	if caracter >=48 and caracter <=57: 
		columna= 0 #define a la columna número de acuerdo a ese rango de codigo ascii que son números del 0-9
	else:   #si no entra en ese rango pasa a la siguiente condición.
		if caracter >=97 and caracter <=122 or caracter >=65 and caracter <=90: #Condicional que define el rango para las letras minusculas y mayusculas.
			columna= 2  #se le asigna la columna número dos a los caracteres que son letras.
		else: # 
			if caracter in operadores_ascii: # entra a condicional cuando el caracter esta dentro de la lista de codigo ascii
				columna= operadores_ascii.index(caracter)+3 #se obtiene un indice de la matriz a partir de los simbolos diferentes a la columna letra y digito.
			else: # sale de la condición si el caracter es desconocido.
				print('Caracter no valido:'+str(caracter))
	return columna  #la funsión devuelve el indice obtenido de la columna.
	
def salidas(edo,palabra):   #función que devuelve las salidas del programa.
		if (edo >=200 and edo <=203) or (edo ==209): #condicional para registrar en tabla de constantes
			if palabra not in tabla_constantes:# pasa al siguiente estatuto si la palabra no está en la tabla.
				tabla_constantes.append(palabra) #guarda la palabra final en la tabla de constantes.
				ind = tabla_constantes.index(palabra)+inicio_constantes #obtiene el indice de la tabla constantes e inicia en el numéro asignado de la variable "inicio de constantes"
				tablaDeTokens.append([inicio_constantes,ind,palabra]) #guarda la palabra en la tabla de token, junto con el indice obtenido, como una constante
			else:
				ind = tabla_constantes.index(palabra) #obtiene el indice si la constante ya esta en la tabla de constantes.
				tablaDeTokens.append([inicio_constantes,ind,palabra]) #almacena la palabra en la tabla de tokens anexando su idice que obtuvo de la tabla constantes.

		if edo==204: # Condicional que registra los identificadores y las palabras reservadas
			if palabra in reservadas: # entra a la condición cuando la palabra existe en la lista de las palbras reservadas.
				tok= reservadas.index(palabra)+inicio_palabras_reservadas #genera el indice de la lista de palabras reservadas más el inicio de la variable "palabras reservadas".
				tablaDeTokens.append([inicio_palabras_reservadas,tok,palabra]) #guarda en la tabla de tokens junto con indice obtenido y palabra, como una palabra reservada.
			else:
				if palabra not in tabla_variables: #entra a condicional si la palabra no esta en la tabla de variables.
					tabla_variables.append(palabra) #guarda la palabra en la tabla de variables siempre y cuando no este registrada antes.
					ind = tabla_variables.index(palabra) #obtiene el indice si la variable ya esta en la tabla
					tablaDeTokens.append([inicio_identificadores,ind,palabra]) #guarda en la tabla de token como un identificador.
				else:
					ind  = tabla_variables.index(palabra) #obtiene el indice de de la tabla de variables, siempre y cuando ya exista.
					tablaDeTokens.append([inicio_identificadores,ind,palabra]) #guarda en la tabla de token como un identificador, junto con indice obtenido.

		if (edo >=205 and edo <=208) or (edo >=300 and edo <=314): #Registra los simbolos especiales
			if palabra in simbolos: #condicional para todos los simbolos.
				ind =simbolos.index(palabra)+inicio_simbolos_especiales #obtiene el indice cuando ya se encuentra registrada la palabra. 
				tablaDeTokens.append([inicio_simbolos_especiales,ind,palabra]) #guarda el token en la tabla como un simbolo especial, seguido de su indice e inicio de variable "simbolos especiales".

		if edo==315: #condicional para registro de comentarios
			tabla_comentarios.append([palabra]) #guarda los comentarios en la tabla de comentarios.

		return 0
		
if __name__ == '__main__':
	main()
