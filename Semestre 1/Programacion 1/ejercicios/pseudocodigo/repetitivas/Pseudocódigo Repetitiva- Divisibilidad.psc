Algoritmo divisibilidad
	//DESCRIPCIÓN: algoritmo para saber si un numero es divisible entre otro
	//ENTRADAS: números x,n
	//SALIDAS: Saber si es divisible o no
	
	//Inicio
Escribir "Escriba un numero X natural"
Leer x // 12
Escribir "Escriba un numero I natural"
Leer i // 4
es_divisible=Falso
resultado=0
Si x<i
	es_divisible=Falso
SiNo
	Para multiplicador=1 hasta x
		resultado=multiplicador*i
		si resultado== x
			es_divisible=Verdadero
			multiplicador=x	
		FinSi
	FinPara
FinSi

Si es_divisible=Falso
	Escribir x," No es divisible entre ", i
SiNo
	Escribir x," Es divisible entre ", i
FinSi

FinAlgoritmo
