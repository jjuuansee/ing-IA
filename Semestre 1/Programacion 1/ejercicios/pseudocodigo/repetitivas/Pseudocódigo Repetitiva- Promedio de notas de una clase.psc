Algoritmo Promedio_de_Notas
	//DESCRIPCIÓN: algoritmo para calcular el promedio de notas 
	//ENTRADAS: 32 notas de 32 alumnos
	//SALIDAS: El promedio de las notas
	
	//Inicio
	acumulador=0
	Para contador=1 hasta 32
		Escribir "Ingrese una nota de un alumno"
		Leer nota
		acumulador=acumulador+nota
		Si contador==32
			promedio=acumulador/32
			Mostrar "El promedio de notas de la clase fue de: ",promedio
		FinSi
	FinPara
FinAlgoritmo
