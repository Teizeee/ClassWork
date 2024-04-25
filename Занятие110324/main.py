import requests
from base64 import b64decode


# написать URL получение файла через API GitHub
response = requests.get('https://api.github.com/repos/y9NBA/Work-with-git-api/contents/1.docx.html')
print(response.status_code)

if response.status_code == 200:


    html = response.json()['content']
    html = (b64decode(html.encode('ascii'))).decode('ascii')

    # Получить расписание согласно выданного варианта

    with open('1.docx.html', 'w') as f:
        f.write(html)
        


