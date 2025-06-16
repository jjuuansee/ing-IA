Algoritmo Altura_Maxima
	//DESCRIPCIÓN: algoritmo para saber cual de todas las alturas ingresadas es la maxima
	//ENTRADAS: n numeros de alturas
	//SALIDAS: La altura maxima
	
	//Inicio
	Escribir "Ingrese la cantidad de alturas que va a ingresar:"
	Leer numero_de_alturas
	altura_max=0
	Si numero_de_alturas= 0 o numero_de_alturas<0
		Escribir "Ingrese un valor de alturas adecuado"
	SiNo
		Para contador=1 hasta numero_de_alturas
			Escribir "Ingrese el valor de una altura en metros:"
			Leer altura
			Si altura<0.1 y altura>9.9
				Escribir "Ingrese el valor de la altura en metros"
			SiNo 
				Si altura_max<altura
					altura_max=altura
				FinSi
			FinSi
		FinPara
		Escribir "La altura maxima ingresada es: ",altura_max	
	FinSi
	
FinAlgoritmo
