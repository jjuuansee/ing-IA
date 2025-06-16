Algoritmo fecha
//DESCRIPCION: algoritmo utilizado para comparar dos fechas y decir la diferencia en dias meses y anios
//ENTRADAS: Dos fechas diferentes
//SALIDAS: La diferencia entre ellas
	//INICIO
	Escribir "Ingrese la hora del primer reloj"
	Leer hora1 
	Escribir "Ingrese el minuto del primer reloj"
	Leer minuto1 
	Escribir "Ingrese los segundos del primer reloj"
	Leer segundo1
	Escribir "Ingrese la hora del segundo reloj"
	Leer hora2 
	Escribir "Ingrese el minuto del segundo reloj"
	Leer minuto2
	Escribir "Ingrese los segundos del segundo reloj"
	Leer segundo2
	Si hora1>hora2 o (hora1=hora2 y minuto1>minuto2 o (minuto1=minuto2 y segundo1>segundo2 ))
		Escribir "La hora 2 es anterior al reloj 2"
	SiNo
		Escribir "La hora 1 es anterior al reloj 2"
	FinSi
FinAlgoritmo