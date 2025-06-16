import asyncio
async def envio_notificacion(ID, tiempo):
    await asyncio.sleep(tiempo)
    print(f'Estudiante {ID} envio notifiacin')

async def main():
    await asyncio.gather(
        envio_notificacion('69',2),
        envio_notificacion('2', 3),
        envio_notificacion('100', 1)
    )

asyncio.run(main())