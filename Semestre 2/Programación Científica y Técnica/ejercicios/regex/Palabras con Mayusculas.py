import re
texto = """Peñarol participó del grupo 5, integrado por equipos uruguayos y peruanos. El debut fue ante Progreso con victoria 3 a 2 en el Estadio Centenario. Los próximos partidos se disputaron en tierras incaicas. El primer encuentro fue victoria 1 a 0 ante Alianza Lima y el segundo fue empate 1 a 1 ante Colegio San Agustín. El cuarto partido de la serie fue ante Progreso en Montevideo que culminó igualado 1 a 1. Luego derrotó 2 - 0 a los equipos peruanos, primero a Alianza Lima, luego a San Agustín y clasificó a segunda fase de forma invicta con 10 puntos.

Peñarol integró la llave de semifinales junto a Independiente y River Plate de Argentina. Este último era el campeón vigente de la Copa Libertadores. El primer encuentro el carbonero como local derrotó 3 a 0 a Independiente con goles de Aguirre, Cabrera y Viera. El segundo partido, también en el Centenario, fue empate 0 a 0 con River Plate. Las revanchas en Argentina fueron el 30 de setiembre ante Independiente y el 7 de octubre ante River Plate. El primero fue victoria uruguaya 4 a 2 en el Estadio de Avellaneda. Ante River Plate en el Monumental, Peñarol perdió 1 a 0 pero ya estaba clasificado para la final de la Copa Libertadores.

El primer encuentro ante América se jugó el 21 de octubre en el Pascual Guerrero de Cali. El técnico Oscar Tabárez formó el equipo con Eduardo Pereira, José Herrera, Marcelo Rotti, Obdulio Trasante, Alfonso Domínguez, José Perdomo, Gustavo Matosas, Daniel Vidal, Ricardo Viera, Jorge Cabrera y Diego Aguirre. El partido finalizó 2 a 0 con goles de Battaglia y Cabañas para el conjunto colombiano.

La revancha fue en Montevideo el 28 del mismo mes. Peñarol tenía que ganar para forzar una tercera final. El equipo fue similar, Tabárez solo ingresó una variante con respecto al equipo que jugó en Cali, Eduardo Da Silva subrogando a Gustavo Matosas.

América de Cali comenzó ganando con gol de Cabañas. No importaba la diferencia de goles, Peñarol solamente necesitaba ganar, sin que tuviera influencia el marcador final. Con goles de Diego Aguirre a los 68 minutos y de Jorge Villar a los 87 que había ingresado para el complemento, el carbonero lo dio vuelta y venció 2 a 1.

La tercer final se disputó en el Estadio Nacional de Santiago. Peñarol salió a la cancha con Eduardo Pereira, José Herrera, Marcelo Rotti, Obdulio Trasante, Alfonso Domínguez, José Perdomo, Eduardo Da Silva, Daniel Vidal, Ricardo Viera, Jorge Cabrera y Diego Aguirre. Los noventa minutos culminaron 0 a 0, debiéndose jugar un alargue de 30 minutos.

En caso que el suplementario finalizara empatado, América sería el campeón por diferencia de goles.
Sin embargo, llegando al minuto 120, Diego Aguirre realizó una gran jugada personal cuando le queda el balón al pie enviado desde la derecha anotando en arco de Falcioni, el 1 a 0 que fue el de la victoria. De esa manera, se desató en la tarde chilena la alegría de los peñarolenses que conquistaban su quinta Copa Libertadores la 3ª. ganada en el Estadio Nacional de Santiago.

 """
print(re.findall(r"([A-ZÁÉÍÓÚ]\w*)", texto))
