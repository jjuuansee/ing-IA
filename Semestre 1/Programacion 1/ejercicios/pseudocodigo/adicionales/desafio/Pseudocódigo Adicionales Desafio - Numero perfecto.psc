Algoritmo numero_perfecto
	//DESCRIPCIÓN: algoritmo para determinar si un numero es perfecto
	//ENTRADAS: un numero entero
	//SALIDAS: si es perfecto o no
	
	//Inicio
	Escribir "Ingrese un numero entero"
	Leer n
	es_perfecto=Falso
	sumatoria=0
	Si n <0
		n=n*(-1)
	FinSi
	Para divisor=1 hasta n-1
		Si n mod divisor==0
			sumatoria=sumatoria+divisor
		FinSi
		Si sumatoria==n
			es_perfecto=Verdadero
		SiNo
			es_perfecto=Falso
		FinSi
	FinPara
	Si es_perfecto==Verdadero
		Escribir "El numero ",n," es un numero perfecto"
	SiNo
		Escribir "El numero ",n," no es un numero perfecto"
	FinSi
FinAlgoritmo
