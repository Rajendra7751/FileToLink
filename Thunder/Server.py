from aiohttp import web
from Thunder.utils.stream_handler import stream_handler  # Adjust this if needed

def patch_stream_routes(app):
    app.router.add_get("/{file_id}", stream_handler)
    app.router.add_get("/{file_id}/{file_name}", stream_handler)

async def web_server():
    app = web.Application()
    patch_stream_routes(app)
    return app
