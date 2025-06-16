Algoritmo aprender_a_contar
	// DESCRIPCIÓN: algoritmo para enseñarle a el usuario a contar
	// ENTRADAS: un numero maximo hasta el que quiero contar
	// SALIDAS: Si lo logro o no
	// Inicio
	Escribir 'Ingrese el numero maximo hasta el que quiere contar'
	Leer numero_maximo
	pudo <- Falso
	Si numero_maximo<0 Entonces
		Escribir 'El numero ingresado no es correcto'
	SiNo
		Para contador<-1 Hasta numero_maximo Hacer
			Escribir 'Ingrese un numero'
			Leer n
			Si n=contador Entonces
				pudo <- Verdadero
			SiNo
				Escribir 'Error!'
			FinSi
		FinPara
		Si pudo=Verdadero Entonces
			Escribir 'Felicitaciones!'
		FinSi
	FinSi
FinAlgoritmo
