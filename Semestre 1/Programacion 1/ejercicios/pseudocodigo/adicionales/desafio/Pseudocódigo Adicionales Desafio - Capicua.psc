Algoritmo capicua
//DESCRIPCION: algoritmo utilizado para derminar si un numero de 5 digitos es capicúa
//ENTRADAS: Número de 5 cifras
//SALIDAS: Si es capicúa o no
	//INICIO
	Escribir "Digite un numero de cinco cifras"
	Leer n //1001
	num_original=n
	inversion_de_num=0
	digito=0
	mientras n>0
		digito=n mod 10 //se queda con el digito 1
		inversion_de_num=inversion_de_num*10+digito //1
		n=trunc(n/10)
	FinMientras
	Si inversion_de_num==num_original
		Escribir "El numero es capicua"
	SiNo
		Escribir "El numero no es capicua"
	FinSi
FinAlgoritmo
