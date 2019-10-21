import asyncio
import random
from datetime import datetime

from aiohttp import web

from dummy.dummy_class import Upper


async def to_upper(string, worker):
    return worker.uppercase(string)


async def echo_loud(request):
    n = datetime.now().isoformat()
    delay = random.randint(0, 3)
    await asyncio.sleep(delay)
    response = {}
    data = await request.json()
    response["name"] = await to_upper(data["name"], upper)
    response["delay"] = delay
    print(f'Time: {n}, response: {response["name"]}, delay: {delay}')
    return web.json_response(data=response)

upper = Upper()

app = web.Application()
app.add_routes([web.post('/', echo_loud)])
web.run_app(app)
