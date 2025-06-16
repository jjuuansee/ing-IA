Algoritmo raices_polinomio
//Descripción: alogritmo para hayar las raices de un polinomio
//Entradas: polinomio de segundo grado
//Salida: Sus raices
	
 //INICIO
	Escribir "Escribir coeficiente de la x con grado 2"
	Leer a
	
	Si a<>0
		Escribir "Escribir coeficiente de la x con grado 1"
		Leer b
		Escribir "Escribir el termino independiente"
		Leer c
		
		Discrimintante=(b^2)-4*a*c
		
		Si Discrimintante< 0
			Escribir "No hay raices reales"
		SiNo
			Si Discrimintante = 0
				x1 = -b/2*a
				x2 = -b/2*a
				Escribir "Raíz 1 = ", x1, " y Raíz 2 = ", x2	
			SiNo
				x1= (-b+(((b^2)-4*a*c))^(1/2))/2*a
				x2= (-b-(((b^2)-4*a*c))^(1/2))/2*a
				Escribir "Raiz 1= ", x1,"y Raiz 2= ",x2
			FinSi
		FinSi
		
	SiNo
			
		Escribir "No es una ecuacion de segundo grado"
	FinSi

	
FinAlgoritmo