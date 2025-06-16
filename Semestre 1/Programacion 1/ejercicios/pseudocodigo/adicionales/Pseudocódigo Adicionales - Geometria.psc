Algoritmo geometria
	//DESCRIPCIÓN: algoritmo para determinar el area y perimetro de un cuadrado o rectangulo
	//ENTRADAS: Longitudes de los lados
	//SALIDAS: Area, perimetro y si es rectangulo o un cuadrado
	
	//Inicio
	Escribir "Ingrese la longitud de un lado en centimetros"
	Leer longitud1
	Escribir "Ingrese la longitud de otro lado en centimetros"
	Leer longitud2
	Si longitud1==longitud2
		Escribir "La figura a estudiar se trata de un cuadrado"
	SiNo
		Escribir "La figura a estudiar se trata de un rectangulo"
	FinSi
	area= longitud1*longitud2
	perimetro= 2*(longitud1+longitud2)
	Escribir "El area de la figura es: ", area, " cm^2"
	Escribir "El perimetro de la figura es:", perimetro, "cm"
FinAlgoritmo
