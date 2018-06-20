import json

from psycopg2 import Warning, Error
from tornado import web, gen
from tornado.escape import json_decode

from client_server.test_base import TestBase


class PostgresHandler(web.RequestHandler):
    def data_received(self, chunk):
        pass

    json_args = None
    SUPPORTED_METHODS = ("GET", "POST", "DELETE", "PUT")

    @gen.coroutine
    def prepare(self):
        if self.request.headers.get("Content-Type") == "application/json":
            try:
                self.json_args = json_decode(self.request.body)
            except Exception as error:
                self.write(error)
                self.finish('invalid request')

    @property
    def db(self):
        return self.application.db


class PostgresUserHandler(PostgresHandler):
    @gen.coroutine
    def get(self, id_):
        dao = TestBase(self.db)
        dict_result = yield (dao.get(id_))

        self.write(json.dumps(dict_result, indent=4))
        self.finish()

    @gen.coroutine
    def post(self, *args):
        dao = TestBase(self.db)
        if not getattr(self, 'json_args'):
            yield (dao.create_random())
        else:
            yield (dao.create(self.json_args))
        self.write('OK\n')
        self.finish()

    @gen.coroutine
    def put(self, id_=None):
        if not getattr(self, 'json_args'):
            self.write('invalid request')
            self.finish()
        else:
            try:
                dao = TestBase(self.db)
                if id_:
                    yield (dao.update(id_, data=self.json_args))
                    dict_result = yield (dao.get(id_))
                    self.write(json.dumps(dict_result))
                else:
                    self.write('invalid user')
            except (Warning, Error) as error:
                self.write(error)
            finally:
                self.finish()

    @gen.coroutine
    def delete(self, id_=None):
        if id_:
            dao = TestBase(self.db)
            yield (dao.delete(id_))
            self.write('user deleted')
        else:
            self.write('invalid user')
        self.finish()


class PostgresUsersHandler(PostgresHandler):
    SUPPORTED_METHODS = ("GET",)

    @gen.coroutine
    def get(self):
        dao = TestBase(self.db)
        if not getattr(self, 'json_args'):
            dict_result = yield dao.get_list()
        else:
            dict_result = yield dao.get_list_with_params(self.json_args)

        self.write(json.dumps(dict_result, indent=4))
        self.finish()
