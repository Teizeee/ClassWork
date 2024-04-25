from peewee import SqliteDatabase, Model, TextField, IntegerField, DateTimeField, ForeignKeyField
import datetime
import requests
from base64 import b64decode


response = requests.get('https://api.github.com/repos/y9NBA/Work-with-git-api/contents/1.docx.html')
print(response.status_code)

if response.status_code == 200:


    html = response.json()['content']
    html = (b64decode(html.encode('ascii'))).decode('ascii')

  
    with open('1.docx.html', 'w') as f:
        f.write(html)

db = SqliteDatabase('sqlite.db')

class DB(Model):
    class Meta:
        database = db


class User(DB):
    API = TextField(default = 'без имени')
    Description = TextField(default = 'без имени')
    Auth = TextField(default = 'без имени')
    HTTPS = TextField(default = 'без имени')
    Cors = TextField(default = 'без имени')
    Link = TextField(default = 'без имени')
    Category = TextField(default = 'без имени')



#a = User.get_or_create(name = f)
db.connect()
db.create_tables([User])
db.close()