Algoritmo suma_y_resta_de_inversos_de_n
	//DESCRIPCIÓN: algoritmo para calcular la y resta de inversos hasta n
	//ENTRADAS: n
	//SALIDAS: valor de la operacion
	
	//Inicio
	Escribir "Ingrese un numero entero positivo y distinto de 0"
	leer n
	Si n <0 o n=0
		Escribir "Ingrese un numero adecuado"
	SiNo
		resultado=0
		Para divisor=1 hasta n
			sucesion=1/divisor
			si divisor mod 2 == 0
				resultado=resultado-sucesion
			SiNo
				resultado=resultado+sucesion
			FinSi
		FinPara
		Escribir "El valor de la operacion es: ", resultado
	FinSi
	
FinAlgoritmo
