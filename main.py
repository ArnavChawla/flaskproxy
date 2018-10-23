
from flask import Flask
from requests import get

app = Flask('__main__')
SITE_NAME = 'https://reddit.com/'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
  header={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
  }
  return get(f'{SITE_NAME}{path}',headers=header).content

app.run(host='0.0.0.0', port=8080)