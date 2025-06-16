Algoritmo cifras_impares
	//DESCRIPCIÓN: algoritmo para saber cuantos digitos tiene un numero n
	//ENTRADAS: n
	//SALIDAS: cuantos digitos tiene un numero n
	
	//Inicio
	Escribir  "Digite un número mayor a 0"
	Leer  n
	cantidad_de_cifras = 0
	cantidad_de_cifras_impares = 0
	Mientras n <> 0 
		cifra = n mod 10
		n= trunc(n/10)
		Si cifra mod 2 <> 0
			cantidad_de_cifras_impares=cantidad_de_cifras_impares+1
		FinSi
		cantidad_de_cifras = cantidad_de_cifras + 1 
	FinMientras 
	Escribir "El número: ", num, " tiene ", cantidad_de_cifras, " cifras y ",cantidad_de_cifras_impares," de esas cifras son impares"
	
FinAlgoritmo
