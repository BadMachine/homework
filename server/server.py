import tornado.ioloop
import tornado.web
import asyncio
from datetime import datetime

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.write('{ "name": "Roman", "secondname": "Volf", "date": "'f'{now}''", "server": "tornado v.' f'{tornado.version}''" }')

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    app = tornado.web.Application([
    (r"/", basicRequestHandler)
    ])
    port = 8882
    app.listen(port)
    print(f"Application is ready and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()