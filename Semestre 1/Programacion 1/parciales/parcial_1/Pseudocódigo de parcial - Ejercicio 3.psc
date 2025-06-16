Algoritmo compuesto
	//DESCRIPCIÓN: algoritmo para saber si un numero es compuesto
	//ENTRADAS: un numero natural
	//SALIDAS: Si es compuesto o no
	
	//Inicio
Escribir "Escriba un numero natural"
Leer n
es_primo=Verdadero
Si n<0
	Escribir "El numero ingresado no es correcto"
Sino	
divisor=2
Mientras divisor<n
	Si n mod divisor=0
		es_primo=Falso
	FinSi
	divisor=divisor+1
FinMientras
Si es_primo=Falso
	Escribir "El numero ingresado SI es un numero compuesto"
SiNo
	Escribir "El numero ingresado NO es un numero compuesto"
FinSi
FinSi

FinAlgoritmo
