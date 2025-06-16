Algoritmo Hailstone
	//DESCRIPCIÓN: algoritmo para saber si un numero es divisible entre otro
	//ENTRADAS: números x,n
	//SALIDAS: Saber si es divisible o no
	
	//Inicio
Escribir "Escriba un numero N natural"
Leer n
Si n <0
	n=n*(-1)  
FinSi
Mientras n<>1
	Si n mod 2 = 0
		n=n/2
	SiNo
		n=(n*3)+1
	FinSi
Escribir n
FinMientras
Mostrar n
FinAlgoritmo
