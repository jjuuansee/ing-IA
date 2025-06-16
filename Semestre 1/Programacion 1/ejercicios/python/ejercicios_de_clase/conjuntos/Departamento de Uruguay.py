departamentos = {"Montevideo", "Artigas", "Canelones", "Lavalleja", "Maldonado", "San Jose", "Colonia", "Florida",
                 "Flores", "Durazno", "Tacuarembo", "Paysandu", "Cerro largo", "Salto", "Rivera", "Rocha", "Rio negro",
                 "Treinta y Tres", "Soriano"}
departamentos_fronteras = {"Salto", "Artigas", "Rivera", "Cerro Largo", "Rocha", "Paysandu", "Rio Negro"}
departamentos_serranos = {"Maldonado", "Lavalleja", "Rocha", "Treinta y Tres", "Cerro Largo"}
departamentos_playas = {"Maldonado", "Rocha"}

caso_a = departamentos - departamentos_fronteras
print(f"Los departamentos sin fronteras son: {caso_a}")

caso_b = caso_a - departamentos_serranos
print(f"Los departamentos que no tienen fronteras ni sierras son: {caso_b}")

caso_c = departamentos_playas & departamentos_serranos
print(f"Los departamentos con sierras y playas son: {caso_c}")

caso_d = departamentos_playas | departamentos_serranos
print(f"Los departamentos con atracciones turisticas son: {caso_d}")

caso_e = departamentos - caso_d
print(f"Los departamentos mas aburridos son: {caso_e}")
