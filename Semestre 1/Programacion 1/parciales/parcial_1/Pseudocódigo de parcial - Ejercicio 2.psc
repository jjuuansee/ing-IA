Algoritmo STM
//DESCRIPCION: algoritmo utilizado para calcular el saldo restante de una STM segun el boleto a comprar
//ENTRADAS: Que viaje querra comprar (1 hora o 2 horas) y el saldo de la tarjeta
//SALIDAS: El saldo restante o saldo faltante
	//INICIO
	Escribir "Ingrese el saldo de la tarjeta"
	Leer saldo
	viaje_valido=Verdadero
Si Saldo<0
	Escribir "El saldo ingresado no es correcto"
Sino
	Escribir "Ingrese el numero de horas de boleto"
	Leer hora
	
	Si hora <>2 y hora<>1
		viaje_valido=Falso
	FinSi
	Si (hora =1 y saldo>=42) o (hora=1 y saldo<42)
		saldo=saldo-42
		viaje_valido=Verdadero
	FinSi
	Si (hora =2 y saldo>=62) o (hora=2 y saldo<62)
		viaje_valido=Verdadero
		saldo=saldo-62
	FinSi
	Si viaje_valido=Verdadero y saldo>=0
		Escribir "Saldo restante ",saldo
	Sino
		Si viaje_valido=Verdadero y saldo<0
			Escribir "Saldo a abonar ", saldo*(-1)
		SiNo
			Si viaje_valido=Falso
				Escribir "Viaje invalido"
			FinSi
		FinSi
	FinSi
FinSi

FinAlgoritmo
