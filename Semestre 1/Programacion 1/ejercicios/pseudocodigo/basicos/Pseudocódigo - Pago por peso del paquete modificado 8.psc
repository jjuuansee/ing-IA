Algoritmo pago_por_kilo
//Descripción: alogritmo para saber cuanto tengo que pagar por el peso de un paquete
//Entradas: peso del paquete
//Salida: total a pagar
	
 //INICIO
	Escribir "Ingrese el peso en gramos del paquete a enviar"
	Leer peso
	Si peso >= 1
		Si peso <900
			pago = 19.80
		SiNo
			si peso>= 900 y peso<5000
				pago=(peso/1000)*21.9
			SiNo
				si peso >=5000 y peso<20000
					pago=(peso/1000)*16.5
				SiNo
					si peso>=20000 y peso<40000
						pago=(peso/1000)*13.2
					SiNo
						si peso>= 40000
							Escribir "Cotizar carga"
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
		pago_total=(pago*1.1)+5
		Escribir pago_total
	SiNo
		Escribir "El peso ingresado no es valido"	
	FinSi

	
FinAlgoritmo