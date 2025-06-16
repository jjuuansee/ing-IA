Algoritmo capicua
//DESCRIPCION: algoritmo utilizado para derminar si un numero de 5 digitos es capicúa
//ENTRADAS: Número de 5 cifras
//SALIDAS: Si es capicúa o no
	//INICIO
	Escribir "Digite un numero de cinco cifras"
	Leer n //12345
	auxiliar=0
	digito5=0
	digito4=0
	digito3=0
	digito2=0
	digito1=0
	Si n>9999 y n<99999
		Si n <0
			n=n*(-1)
		FinSi
		digito5= n mod 10 //5 
		auxiliar= (n-digito5)/10 //1234
		digito4= auxiliar mod 10 //4
		auxiliar= (auxiliar-digito4)/10 //123
		digito3= auxiliar mod 10 //3
		auxiliar= (auxiliar-digito3)/10 //12
		digito2= auxiliar mod 10 //2
		auxiliar= (auxiliar - digito2 ) //10
		digito1= auxiliar/10
		Si digito1 == digito5 y digito2 == digito4
			Escribir "Es capicúa"
		Sino 
			Escribir "No es capicúa"
		FinSi
		
		
	SiNo
		Escribir "Digite otro numero"
	FinSi
FinAlgoritmo
