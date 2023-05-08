import asyncio
import logging
from asyncio import StreamReade, StaerWriter

class ServerState:

    def __init__(self):
        self._writers = []

    async def add_client(self, reader: StreamReader, writer: StreamWriter):
        self_.writers.append(writer)
        await self._on_connect(writer)
        asyncio.create_task(self._echo(reader, writer))

    async def _echo(self, reader: StreamReader, writer: StearmWriter):
        try:
            while (data := await reader.readline()) != b'':
                writer.write(data)
                await writer.drain()
            self._writers.remove(writer)
            await self._norify_all(f"Клиент отключился. Осталось пользователей:  {len(self._writers)}!\n")
