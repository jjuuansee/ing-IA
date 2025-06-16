Algoritmo años_bisiestos_entre_dos_años
//DESCRIPCION: algoritmo utilizado para encontrar la cantidad de años bisiestos entre dos años
//ENTRADAS: dos años diferentes
//SALIDAS: la cantidad de años bisisestos entre los dos años
	//INICIO
	Escribir "Ingrese un año"
	Leer año1
	Escribir "Ingrese otro año mayor al ingresado anteriormente"
	Leer año2
	bisiesto=0
	
	Si año1 == año2
		Escribir "Los años ingresados son iguales"
	SiNo
		Si año1>año2
			Escribir "El primer año ingresado es más grande"
		SiNo
			Para var=año1 Hasta año2
				Si ((var mod 4 == 0) y (var mod 100 <>0)) o (var mod 400 == 0)
					bisiesto=bisiesto+1
				FinSi
			FinPara
		FinSi
	FinSi
	Escribir "La cantidad de años bisiestos entre los dos años ingresados son: ",bisiesto
	
	
FinAlgoritmo
