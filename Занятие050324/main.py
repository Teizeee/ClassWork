from peewee import SqliteDatabase, Model, TextField, IntegerField, DateTimeField, ForeignKeyField
import datetime


db = SqliteDatabase('sqlite.db')

class DB(Model):
    class Meta:
        database = db


class User(DB):
    name = TextField(default = 'без имени')
    create_at = DateTimeField(default = datetime.datetime.now)

class Subscription(DB):
    name = TextField(default = 'без имени')
    time = IntegerField(default=0)
    user = ForeignKeyField(User, backref="subscriptions")


db.connect()
db.create_tables([User, Subscription], safe=True)
db.close()
