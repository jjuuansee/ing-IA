Algoritmo fecha
//DESCRIPCION: algoritmo utilizado para comparar dos fechas y decir la diferencia en dias meses y anios
//ENTRADAS: Dos fechas diferentes
//SALIDAS: La diferencia entre ellas
	//INICIO
	Escribir "Ingrese el dia de la primer fecha"
	Leer dia1 
	Escribir "Ingrese el mes de la primer fecha"
	Leer mes1 
	Escribir "Ingrese el anio de la primer fecha"
	Leer a�o1
	Escribir "Ingrese el dia de la segunda fecha"
	Leer dia2
	Escribir "Ingrese el mes de la segunda fecha"
	Leer mes2 
	Escribir "Ingrese el anio de la segunda fecha"
	Leer a�o2
	Si dia1>dia2
		diferencia_dia= dia1-dia2
	SiNo
		diferencia_dia= dia2-dia1
	FinSi
	
	Si mes1>mes2
		diferencia_mes= mes1-mes2
	SiNo
		diferencia_mes= mes2-mes1
	FinSi
	
	Si a�o1>a�o2
		diferencia_a�o= a�o1-a�o2
	SiNo
		diferencia_a�o= a�o2-a�o1
	FinSi
	Escribir "La diferencia de entre las dos fechas es de: ",diferencia_a�o," a�os con ",diferencia_mes," meses y ",diferencia_dia," dias"
FinAlgoritmo
