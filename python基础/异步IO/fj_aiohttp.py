import asyncio
from aiohttp import web

# aiohttp最新用法
# https://aiohttp.readthedocs.io/en/stable/web_quickstart.html#run-a-simple-web-server
routes = web.RouteTableDef()

@routes.get('/')
async def index(request):
	await asyncio.sleep(0.5)
	return web.Response(body=b'<h1>index page</h1>', content_type='text/html')

@routes.get('/hello/{name}')
async def hello(request):
	await asyncio.sleep(0.5)
	text = '<h1>hello, %s!</h1>' % request.match_info['name']
	return web.Response(body=text.encode('utf-8'),content_type='text/html')

#  https://aiohttp.readthedocs.io/en/stable/web_advanced.html#aiohttp-web-app-runners
async def init():
	app = web.Application()
	app.router.add_routes(routes)
	runner = web.AppRunner(app)
	await runner.setup()
	site = web.TCPSite(runner, 'localhost',8000)
	await site.start()
	print('服务器已经启动')
	

loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()
