Algoritmo a�os_bisiestos_entre_dos_a�os
//DESCRIPCION: algoritmo utilizado para encontrar la cantidad de a�os bisiestos entre dos a�os
//ENTRADAS: dos a�os diferentes
//SALIDAS: la cantidad de a�os bisisestos entre los dos a�os
	//INICIO
	Escribir "Ingrese un a�o"
	Leer a�o1
	Escribir "Ingrese otro a�o mayor al ingresado anteriormente"
	Leer a�o2
	bisiesto=0
	
	Si a�o1 == a�o2
		Escribir "Los a�os ingresados son iguales"
	SiNo
		Si a�o1>a�o2
			Escribir "El primer a�o ingresado es m�s grande"
		SiNo
			Para var=a�o1 Hasta a�o2
				Si ((var mod 4 == 0) y (var mod 100 <>0)) o (var mod 400 == 0)
					bisiesto=bisiesto+1
				FinSi
			FinPara
		FinSi
	FinSi
	Escribir "La cantidad de a�os bisiestos entre los dos a�os ingresados son: ",bisiesto
	
	
FinAlgoritmo
