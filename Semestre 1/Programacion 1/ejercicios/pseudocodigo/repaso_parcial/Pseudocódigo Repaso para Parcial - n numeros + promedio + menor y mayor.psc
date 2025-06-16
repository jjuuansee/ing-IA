Algoritmo promedio_de_numeros
	//DESCRIPCIÓN: algoritmo para almacenar varios numeros y luego calcular su promedio.
	//ENTRADAS: números n
	//SALIDAS: Resultado del promedio
	
	//Inicio
	seguir_leyendo=Verdadero
	contador=0
	promedio=0
	sumatoria=0
	Mientras seguir_leyendo
		Escribir "Ingrese un numero natural n"
		Leer n
		Si contador==0
			n_menor=n
		FinSi
		Si n == 0
			seguir_leyendo= Falso
		SiNo
			Si n<n_menor
				n_menor=n
			FinSi
			Si n_mayor<n
				n_mayor=n
			FinSi
			contador=contador+1
			sumatoria=sumatoria+n
			promedio=sumatoria/contador
		FinSi
	FinMientras
	Escribir "La cantidad de numeros ingresados fueron: ",contador
	Escribir "El menor numero ingresado fue: ",n_menor
	Escribir "El mayor numero ingresado fue: ",n_mayor
	Escribir "El promedio total es de: ",promedio
	
	
FinAlgoritmo
