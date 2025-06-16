Algoritmo imc
	//MODULO: Algoritnmo para saber el imc de una usuario
	//ENTRADAS: Peso y Altura
	//SALIDA: imc
	
	Escribir"Digite su peso en kilogramos"
	Leer peso
	Escribir"Digite su altura en metros"
	Leer altura
	Si altura>0.01 y altura<3.99
		indice= peso/(altura*altura)
		Si indice < 18.5
			Escribir "Bajo Peso"
		Sino
			Si indice >= 18.5 y indice <= 24.9
				Escribir "Peso adecuado"
			Sino	
				Si indice >=25 y indice <= 29.9
					Escribir "Sobrepeso"
				Sino
					Escribir "Obesidad"	
				FinSi
			FinSi
		FinSi
		Escribir "Su imc= ",indice	
	Sino
		Escribir "Escriba su altura en metros"
	FinSi
FinAlgoritmo
