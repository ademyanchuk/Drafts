import asyncio

from aiohttp import ClientSession


async def fetch(url, session, req):
    async with session.post(url, json=req) as response:
        return await response.read()


async def run(r):
    url = "http://localhost:8080/"
    tasks = []
    req = {"name": "alex"}

    # Fetch all responses within one Client session,
    # keep connection alive for all requests.
    async with ClientSession() as session:
        for _ in range(r):
            task = asyncio.ensure_future(fetch(url, session, req))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        # you now have all response bodies in this variable
        # print(responses)



loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(10000))
loop.run_until_complete(future)
