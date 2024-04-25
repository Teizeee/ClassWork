from peewee import SqliteDatabase, Model, ForeignKeyField, TextField, BooleanField 

db = SqliteDatabase('db.db')

class Table(Model):

    class Meta:
        database = db


class Category(Table):
    name = TextField()

class Info(Table):
    API = TextField()
    Description = TextField()
    Auth = TextField()
    HTTPS = BooleanField()
    Cors = TextField()
    Link = TextField()
    Category = ForeignKeyField(Category)


db.connect()
db.create_tables([Category, Info])
db.close()
