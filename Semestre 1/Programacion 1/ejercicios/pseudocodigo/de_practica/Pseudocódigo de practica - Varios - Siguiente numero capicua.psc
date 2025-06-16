Algoritmo numero_capicua_siguiente
	//DESCRIPCION: algoritmo utilizado para encontrar la cantidad de años bisiestos entre dos años
	//ENTRADAS: un numero de tres cifras
	//SALIDAS: el siguiente numero capicua
	
	//INICIO
	Escribir "Digite un numero entero de 3 cifras"
	Leer n // 103
	contador= n 
	digito3=contador MOD 10 // 3
	digito1=trunc (contador/100) // 1
	Mientras digito1<>digito3 // 1 <> 3
		contador=contador+1 // 104
		digito3= contador MOD 10 // 4
		digito1= trunc(contador/100) // 1
	FinMientras
	Si digito1=digito3
		Escribir "El numero capicua mas cercano a ",n, " es ",contador
	FinSi
	
FinAlgoritmo
