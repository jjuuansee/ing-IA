print("HORARIO hh:mm:ss")
print("================")


def hh_mm_ss(hora, minuto, segundo):
    horario = f"{hora}:{minuto}:{segundo}"
    return horario


hora = input("Ingrese la hora:")
minutos = input("Ingrese los minutos:")
segundos = input("Ingrese los segundos:")
print(hh_mm_ss(hora, minutos, segundos))
