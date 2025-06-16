Algoritmo persona_en_coma
//DESCRIPCION: algoritmo utilizado para el estado general de un paciente en coma
//ENTRADAS: apertura ocular,  respuesta verbal y respuesta motora
//SALIDAS: el nivel del coma
	//INICIO
	Escribir "Ingrese el valor de apertura ocular (1 a 4)"
	Leer apertura_ocular
	Escribir "Ingrese el valor de respuesta verbal (1 a 5)"
	Leer respuesta_verbal
	Escribir "Ingrese el valor de respuesta motora"
	Leer respuesta_motora
	Si apertura_ocular <1 y apertura_ocular>4
		Escribir "Ingrese el valor correcto de apertura ocular"
	FinSi
	Si respuesta_verbal <1 y respuesta_verbal>5
		Escribir "Ingrese el valor correcto de apertura ocular"
	FinSi
	Si respuesta_motora <1 y respuesta_motora>6
		Escribir "Ingrese el valor correcto de apertura ocular"
	FinSi
	score=apertura_ocular+respuesta_motora+respuesta_verbal
	Si score>=13 y score <=15
		Escribir "La situacion del paciente es: Leve"
	SiNo
		Si score>=9 y score <=12
			Escribir "La situacion del paciente es: Moderado"
		Sino
			Si score<9
				Escribir "La situacion del paciente es: Grave"
			FinSi
		FinSi
	FinSi
	
	
	
FinAlgoritmo