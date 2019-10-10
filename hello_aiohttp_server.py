from aiohttp import web

class Upper():
    def uppercase(self, string):
        return string.upper()


async def to_upper(string, worker):
    return worker.uppercase(string)

async def echo_loud(request):
    data = await request.json()
    data["name"] = await to_upper(data["name"], upper)
    return web.json_response(data=data)

upper = Upper()

app = web.Application()
app.add_routes([web.post('/', echo_loud)])
web.run_app(app)