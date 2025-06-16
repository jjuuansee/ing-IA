print("CAMBIAR FORMATO DE FECHA aaaa-mm-dd")
print("===================================")

fecha = input("Ingrese la fecha en formato dd/mm/aaaa: ")
anio = fecha[6:]
mes = fecha[3:5]
dia = fecha[:2]
print(f"{anio}-{mes}-{dia}")