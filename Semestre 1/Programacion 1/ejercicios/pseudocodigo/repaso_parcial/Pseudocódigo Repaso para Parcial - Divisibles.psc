Algoritmo cantidad_de_divisibilidad
	//DESCRIPCIÓN: algoritmo para saber cuales de los numeros ingresados son divisibles entre 3 y entre 2, y los que no tambien
	//ENTRADAS: numeros
	//SALIDAS: cuales de los nombres son divisibles entre 2 y 3
	
	//Inicio
	seguir_leyendo=Verdadero
	cantidad_de_divisibles_de_2=0
	cantidad_de_divisibles_de_3=0
	cantidad_de_no_divisibles=0
	
	Mientras seguir_leyendo
		Escribir "Ingrese un numero entero"
		Leer n
		Si n <> 0
			Si n mod 2 ==0
				cantidad_de_divisibles_de_2=cantidad_de_divisibles_de_2+1
			SiNo
				Si n mod 3 == 0
					cantidad_de_divisibles_de_3=cantidad_de_divisibles_de_3+1
				SiNo
					cantidad_de_no_divisibles = cantidad_de_no_divisibles+1			
				FinSi
			FinSi
		SiNo
			seguir_leyendo=Falso
		FinSi
	FinMientras
	Escribir "La cantidad de numeros divisbles entre 2 son: ", cantidad_de_divisibles_de_2
	Escribir "La cantidad de numeros divisbles entre 3 son: ", cantidad_de_divisibles_de_3
	Escribir "La cantidad de numeros que no son divisibles entre 2 y 3 son: ", cantidad_de_no_divisibles
FinAlgoritmo
