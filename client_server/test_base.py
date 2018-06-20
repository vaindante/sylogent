import random
import string

from tornado import gen


class TestBase(object):
    def __init__(self, db):
        self.db = db
        self.db.connect()

    def __del__(self):
        try:
            self.db.close()
        except:
            pass

    @staticmethod
    def _get_random_str(size=10):
        return ''.join(random.choice(string.ascii_uppercase + string.digits)
                       for _ in range(size))

    @gen.coroutine
    def get(self, id_):
        sql = """
                SELECT id, username, email, password
                FROM users_user
                WHERE id=%r
            """
        cursor = yield self.db.execute(sql % id_)
        desc = cursor.description
        result = tuple(dict(zip((col[0] for col in desc), row)) for row in cursor.fetchall())
        return result

    @gen.coroutine
    def get_list(self):
        sql = """
                SELECT *
                FROM users_user
            """
        cursor = yield self.db.execute(sql)
        desc = cursor.description
        result = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
        return result

    @gen.coroutine
    def get_list_with_params(self, params):
        sql = f"""
                SELECT *
                FROM users_user
                WHERE {', '.join("%s=%r" %(k,v) for k,v in params.items())}
            """
        cursor = yield self.db.execute(sql)
        desc = cursor.description
        result = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
        return result

    @gen.coroutine
    def create(self, json_args):
        sql = """
        insert into users_user (%s) VALUES (%s)
        """ % (', '.join(json_args.keys()), ', '.join('%r' % v for v in json_args.values()))
        yield self.db.execute(sql)

    @gen.coroutine
    def create_random(self):
        sql = """INSERT INTO users_user (username, email, password, url) VALUES (%r, %r, %r, %r)"""
        username = self._get_random_str()
        email = '{0}@{1}.com'.format(self._get_random_str(),
                                     self._get_random_str())
        password = self._get_random_str()
        url = '{0}.{1}.com'.format(self._get_random_str(),
                                   self._get_random_str())

        yield self.db.execute(sql % (username, email, password, url))

    @gen.coroutine
    def update(self, id_, data=None):
        sql = f"""
                UPDATE users_user
                SET {', '.join("%s=%r" %(k,v) for k,v in data.items())}
                WHERE id={id_}
            """
        cursor = yield self.db.execute(sql)
        return cursor

    @gen.coroutine
    def delete(self, id_):
        sql = """
                DELETE
                FROM users_user
                WHERE id=%s
            """
        yield self.db.execute(sql % (id_,))
        return 'user deleted\n'
