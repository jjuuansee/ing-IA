Algoritmo Factores
	//DESCRIPCIÓN: algoritmo para mostrar todos los factores de un numero
	//ENTRADAS: número n
	//SALIDAS: Sus factores
	
	//Inicio
Escribir "Escriba un numero N natural"
Leer n 
Si n <0
	n=n*(-1)
FinSi
contador=1
Mientras contador<n
	Si n mod contador == 0
		resultado= n/contador
		Escribir resultado, "x",contador
	FinSi
	Contador=contador+1
FinMientras


FinAlgoritmo
