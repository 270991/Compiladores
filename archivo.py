def main():

	matriz = [# num  let   >    <    =    +    -    /    !    %    #   .    ''
			 [   1,   4,   5,   6,   9,   7,   8,  11,  10, 30,  300,  2,   0 ], 
        	 [   1, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,  2,  200],   
          	 [   3, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300],   
             [   3, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201, 201],   
          	 [   4,   4, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202, 202],  
          	 [ 204, 204, 204, 204, 203, 204, 204, 204, 204, 204, 204, 204, 204], 
          	 [ 207, 207, 206, 207, 205, 207, 207, 207, 207, 207, 207, 207, 207],
          	 [ 209, 209, 209, 209, 209, 208, 209, 209, 209, 209, 209, 209, 209], 
          	 [ 211, 211, 211, 211, 211, 211, 210, 211, 211, 211, 211, 211, 211], 
          	 [ 213, 213, 213, 213, 212, 213, 213, 213, 213, 213, 213, 213, 213], 
          	 [ 215, 215, 215, 215, 214, 215, 215, 215, 215, 215, 215, 215, 215],
          	 [ 217, 217, 217, 217, 217, 217, 217, 217, 216, 217, 217, 217, 217]
        	]	 


#cadena=[]
	word=''
	with open("archivo.txt", "r") as f:	
		while True:
			edo=0
			for line in f:
				for indice in range(len(line)):
					caracter= ord(line[indice])
					word=word+chr(caracter)
					#print(caracter)
					#print (word)

				#valor=ord(caracter)
				#cadena.append(caracter)

					if caracter >=48 and caracter <=57: #numeros
						columna= 0

					elif caracter >=97 and caracter <=122: #letras
						columna= 1

					elif caracter == 62: #mayor que
						columna= 2

					elif caracter == 60: #menor que
						columna= 3

					elif caracter == 61: 
						columna= 4

					if caracter == 43:
						columna=5

					if caracter == 45:
						columna=6

					if caracter == 47:
						columna=7

					if caracter == 33:
						columna=8
					
					if caracter == 37:
						columna=9 

					if caracter == 35:
						columna=10

					if caracter == 46:
						columna=11

					if caracter == 32: #espacio
						columna=12

					print('estado:'+str(edo) + 'column:' + str(columna))
					edo=matriz[edo][columna]
					#print(edo)

					#if edo > 11:
					if edo==200:
						print('Encontre un numero entero')
						edo=0
					if edo==201:
						print('encontre un numero decimal')
						edo=0

					if edo==204:
						print('encontre un signo de mayor que')
						edo=0
							
							#word=''
					#else:
						#edo=0
						#word=''
					#
			break
			
	f.close()
if __name__ == "__main__":
	main()


