Algoritmo par_o_impar
	//DESCRIPCIÓN: algoritmo para saber si un numero es par o no
	//ENTRADAS: numero
	//SALIDAS: Si es par o impar
	
	//Inicio
	Escribir "Ingrese un numero entero"
	Leer n
	Si n <0 Entonces
		n=n*(-1)
	FinSi
	Si n mod 2 == 0
		Escribir n," Es un numero par"
	SiNo
		Escribir n," Es un numero impar"
	FinSi
FinAlgoritmo
