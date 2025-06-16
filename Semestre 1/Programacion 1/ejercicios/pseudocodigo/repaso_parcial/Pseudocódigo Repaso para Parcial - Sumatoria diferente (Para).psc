Algoritmo sumatoria_diferente_para
	//DESCRIPCIÓN: algoritmo para saber si un numero es perfecto
	//ENTRADAS: un nuemro entero
	//SALIDAS: La cantidad de veces que aparece
	
	//Inicio
	Escribir "Ingrese un numero entero"
	Leer n
	Si n<0
		n=n*(-1)
	FinSi
	Para i=1 Hasta n
		Sumatoria= Sumatoria+3*(4*i-2)
	FinPara
	Mostrar Sumatoria
FinAlgoritmo
