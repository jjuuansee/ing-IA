Algoritmo triangulo_rectangulo
	//DESCRIPCIÓN: algoritmo para determinar si un triangulo es rectangulo o no
	//ENTRADAS: las longitudes de sus lados
	//SALIDAS: si es rectangulo o no 
	
	//Inicio
	Escribir "Ingrese la longitud de un lado"
	Leer a
	Escribir "Ingrese la longitud de otro lado"
	Leer b
	Escribir "Ingrese la longitud del ultimo lado"
	Leer c
	es_triangulo_rectangulo=Verdadero
	Si (c^2)=(a^2)+(b^2)
		es_triangulo_rectangulo=Verdadero
	SiNo
		Si (a^2)=(b^2)+(c^2)
			es_triangulo_rectangulo=Verdadero
		SiNo
			Si (b^2)=(a^2)+(c^2)
				es_triangulo_rectangulo=Verdadero
			SiNo
				es_triangulo_rectangulo=Falso
			FinSi
		FinSi
	FinSi
	Si es_triangulo_rectangulo=Verdadero
		Escribir "El triangulo es rectangulo"
	Sino 
		Escribir "El triangulo no es rectangulo"
	FinSi
FinAlgoritmo
