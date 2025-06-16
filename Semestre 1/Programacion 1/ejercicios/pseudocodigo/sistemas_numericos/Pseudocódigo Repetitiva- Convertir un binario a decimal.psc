Algoritmo convertidor_de_binario_a_decimal
	//DESCRIPCIÓN: algoritmo para convertir un numero binario a decimal
	//ENTRADAS: número binario
	//SALIDAS: Su forma en decimal
	
	//Inicio
Escribir "Escriba un numero binario"
Leer n
num_original=n
binario= ConvertirATexto(n)
n=Longitud(binario)
potencia=0
decimal=0
Si n < 0
	Escribir "Ingrese un valor valido"
SiNo
	Mientras n>0
		Si Subcadena(binario,n,n)=="1"
			decimal=decimal+2^potencia
		FinSi
		n=n-1
		potencia=potencia+1
	FinMientras
	Escribir "El numero binario ",num_original," en decimal es: ",decimal
FinSi
FinAlgoritmo
