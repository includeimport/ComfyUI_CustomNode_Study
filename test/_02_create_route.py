from aiohttp import web
from server import PromptServer

server_instance = PromptServer.instance
routes = server_instance.routes

class WebTest:

    def add_routes(self, routes):
        @routes.get("/test02")
        async def hello_route(request):
            return web.Response(text="Hello")
