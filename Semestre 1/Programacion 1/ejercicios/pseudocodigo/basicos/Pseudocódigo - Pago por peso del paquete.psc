Algoritmo pago_por_kilo
//Descripción: alogritmo para saber cuanto tengo que pagar por el peso de un paquete
//Entradas: peso del paquete
//Salida: total a pagar
	
 //INICIO
	Escribir "Ingrese el peso en kg del paquete a enviar"
	Leer peso
	Si peso < 3
		total_pago= peso*21.99
	SiNo
		si peso>=3 y peso<5
			total_pago= peso*21.99*0.70
		SiNo
			Si peso >=5
 			total_pago= peso*21.99*0.50
			Escribir "Su total a pagar es: ",total_pago	
		FinSi
		FinSi
	FinSi

	
FinAlgoritmo