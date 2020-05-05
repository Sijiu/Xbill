from peewee import *
from playhouse.pool import PooledMySQLDatabase


database = PooledMySQLDatabase('account', max_connections=8, stale_timeout=300, host='127.0.0.1', user='root',
                                 passwd='', charset='utf8', port=3306)
# database = SqliteDatabase('account.db', pragmas={'journal_mode': 'wal', 'cache_size': -1024 * 64})


class UnknownField(object):
    def __init__(self, *_, **__):
        pass


class BaseModel(Model):
    class Meta:
        database = database


class BillModel(Model):
    class Meta:
        database = database

    def to_xbill(self) -> "XBill":
        raise NotImplementedError

    def is_exist(self) -> bool:
        raise NotImplementedError

    def save_if_no_exist(self) -> bool:
        if not self.is_exist():
            return self.save()
        else:
            return False

    @classmethod
    def create_from_row(cls, row) -> "BillModel":
        raise NotImplementedError
