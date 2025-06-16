Algoritmo sumatoria
//DESCRIPCION: algoritmo utilizado para calcular el valor especifico de una sumatoria
//ENTRADAS: numero entero
//SALIDAS: el resultado de la sumatoria
	//INICIO
	Escribir "Ingrese un numero entero"
	Leer n
	Si n<0
		n=n*(-1)
	FinSi
	Para i=1 hasta n
		sum=sum+(3*i^2)
	FinPara
	Escribir sum
FinAlgoritmo
