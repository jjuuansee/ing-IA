Algoritmo poblacion
	//DESCRIPCIÓN: algoritmo para saber cual es la situacion de una zona poblada
	//ENTRADAS: poblacion y zona en km^2
	//SALIDAS: La densidad de poblacion
	
	//Inicio
	Escribir "Ingrese el total de habitantes que se encuentran en la zona"
	Leer habitantes
	Escribir "Ingrese el area en km^2 de la zona que quiere estudiar"
	Leer area
	densidad_de_poblacion=habitantes/area
	Si densidad_de_poblacion < 100
		Escribir "La densidad de poblacion en la zona es baja"
	Sino 
		Si densidad_de_poblacion>100 y densidad_de_poblacion<=150
			Escribir "La densidad de poblacion en la zona es media"
		SiNo
			Si densidad_de_poblacion>150
				Escribir "La densidad de poblacion en la zona es alta"
			FinSi
		FinSi
	FinSi
FinAlgoritmo
