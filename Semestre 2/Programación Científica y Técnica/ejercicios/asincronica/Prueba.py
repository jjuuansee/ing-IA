import asyncio
async def tarea(nombre, tiempo):
    await asyncio.sleep(tiempo)
    print(f'Tarea {nombre} completada en {tiempo} segundos')

async def main():
    await asyncio.gather(
        tarea('A',2),
        tarea('B', 3),
        tarea('C', 1)
    )

asyncio.run(main())