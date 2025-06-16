Algoritmo convertidor_de_decimal_a_binario
	//DESCRIPCIÓN: algoritmo para convertir un numero decimal a binario
	//ENTRADAS: número n
	//SALIDAS: Su forma en binario
	
	//Inicio
Escribir "Escriba un numero decimal"
Leer decimal // 33
num_original=decimal
digito=1
binario=0
si decimal<0
	Escribir "Ingrese un numero decimal valido"
SiNo
	Mientras decimal>=1
		Si decimal mod 2 == 1 // 33 mod 2 = 1
			binario=binario+digito // a binario se le agrega 1
		FinSi
		decimal=trunc(decimal/2) // 16
		digito= digito*10 // 1*10=10
	FinMientras
	Escribir "El numero decimal ",num_original," en binario es: ",binario
FinSi
FinAlgoritmo
