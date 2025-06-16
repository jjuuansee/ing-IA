import asyncio

mensajes = ['Hola Mundo!', 'Hello World!', 'Olá mundo', 'こんにちは世界']

async def enviar_mensaje(mensaje, tiempo_espera):
    await asyncio.sleep(tiempo_espera)
    print(f'Mensaje enviado tras {tiempo_espera} segundos: {mensaje}')

async def main():
    tiempo = 1
    tareas = []
    for mensaje in mensajes:
        tareas.append(enviar_mensaje(mensaje,tiempo))
        tiempo +=1
    await asyncio.gather(*tareas)
asyncio.run(main())
