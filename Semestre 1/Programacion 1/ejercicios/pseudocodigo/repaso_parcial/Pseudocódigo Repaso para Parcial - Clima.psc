Algoritmo clima
	//DESCRIPCIÓN: algoritmo para saber cual es la sensacion del clima
	//ENTRADAS: grados celcius
	//SALIDAS: La sensacion del clima
	
	//Inicio
	Escribir "Ingrese la temperatura en grados celsius (°C)"
	Leer temperatura
	Si temperatura<0
		Escribir "El clima es muy frio"
	SiNo
		Si temperatura>=0 y temperatura<=14
			Escribir "El clima es frio"
		SiNo
			Si temperatura>=15 y temperatura<=24
				Escribir "El clima es templado"
			SiNo
				Si temperatura >=25 y temperatura<=30
					Escribir "El clima es calido"
				SiNo
					Si temperatura>30
						Escribir "El clima es muy caliente"
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
