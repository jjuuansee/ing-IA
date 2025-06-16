Algoritmo cantidad_de_numeros_pares_e_impares
	//DESCRIPCIÓN: algoritmo para saber cuantos numeros pares e impares fueron ingresados por el usuario
	//ENTRADAS: numeros pares e impares
	//SALIDAS: cantidad de numeros pares e impares
	
	//Inicio
	seguir_leyendo=Verdadero
	numeros_pares=0
	numeros_impares=0
	Mientras seguir_leyendo
		Escribir "Ingrese un numero postivo, (ingrese -1 para cerrar el algoritmo)"
		Leer n
		Si n=-1
			seguir_leyendo=Falso
		SiNo
			si n mod 2 ==0
			numeros_pares=numeros_pares+1
		SiNo
			numeros_impares= numeros_impares+1
		FinSi
	FinSi
	FinMientras
	Escribir "La cantidad de numeros impares fueron: ", numeros_impares
	Escribir "La cantidad de numeros pares fueron: ", numeros_pares
FinAlgoritmo
