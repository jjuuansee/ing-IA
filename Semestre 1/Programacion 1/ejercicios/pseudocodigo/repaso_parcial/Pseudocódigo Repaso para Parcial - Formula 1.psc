Algoritmo formula1
	//DESCRIPCIÓN: algoritmo para saber cual es la vuelta rapida de una carrera.
	//ENTRADAS: tiempos de cada vuelta
	//SALIDAS: Vuelta mas rapida y en que fuelta fue
	
	//Inicio
	total_vueltas=1
	tiempo_total=0
	tiempo_vuelta=0
	mejor_tiempo=0
	numero_de_vuelta_de_mejor_tiempo=1
	tiempo_promedio=0
	Mientras total_vueltas<=30 y tiempo_total<=3000
		Escribir "Ingrese los minutos que tardo en dar la vuelta"
		Leer min
		Escribir "Ingrese los segundos que tardo en dar la vuelta"
		Leer seg
		Si seg<=60
			tiempo_vuelta=(min*60)+seg
			tiempo_total=tiempo_total+tiempo_vuelta
			Si total_vueltas==1
				mejor_tiempo=tiempo_vuelta
			FinSi
			Si tiempo_vuelta<mejor_tiempo
				mejor_tiempo=tiempo_vuelta
				numero_de_vuelta_de_mejor_tiempo=total_vueltas
			FinSi
			tiempo_promedio=tiempo_total/total_vueltas
			total_vueltas=total_vueltas+1
		SiNo
			Escribir "Ingrese el tiempo en segundos"
		FinSi
	FinMientras
	Escribir "La vuelta mas rapida fue: ",numero_de_vuelta_de_mejor_tiempo
	Escribir "El tiempo de la vuelta mas rapida fue de: " mejor_tiempo/60
	Escribir "El tiempo promedio fue: ", tiempo_promedio/60
	Escribir "El tiempo total de la carrera fue de: ",tiempo_total/60
	
FinAlgoritmo
