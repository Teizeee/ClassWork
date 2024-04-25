import requests
from models import Info, Category

responce = requests.get("https://api.publicapis.org/entries")

json = responce.json()

for row in json["entries"]:
    category, _ = Category.get_or_create(name=row['Category'])
    row['Category'] = category
    Info.get_or_create(**row)

    