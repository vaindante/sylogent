# -*- coding: utf-8 -*-

from os import getenv

import momoko
from tornado import web, httpserver
from tornado.ioloop import IOLoop
from tornado.options import define, options

from client_server.psql_handlers import PostgresUserHandler

DBHOST = getenv('DBHOST')
DATABASE = getenv('DATABASE')
USER = getenv('USER')
PORT = getenv('PORT', 5432)
PASSWORD = getenv('PASSWORD')

define("port", default=8888, help="run on the given port", type=int)


class Application(web.Application):
    def __init__(self):
        handlers = [
            (r"/user/(\d+)", PostgresUserHandler)
        ]
        web.Application.__init__(self, handlers)
        self.dsn = f'dbname={DATABASE} user={USER} password={PASSWORD} host={DBHOST} port={PORT}'
        # self.db = momoko.Pool(dsn=dsn, size=5)


def main():
    options.parse_command_line()

    application = Application()
    ioloop = IOLoop.instance()

    application.db = momoko.Pool(
        application.dsn,
        size=5,
        ioloop=ioloop,
        raise_connect_errors=False
    )
    future = application.db.connect()

    ioloop.add_future(future, lambda f: ioloop.stop())
    ioloop.start()
    future.result()

    http_server = httpserver.HTTPServer(application)
    http_server.listen(options.port)
    ioloop.start()


if __name__ == '__main__':
    main()
