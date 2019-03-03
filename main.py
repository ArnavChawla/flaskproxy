import requests
import flask
from flask import Flask
from flask import request
from flask import Response
import base64
app = Flask(__name__)
from bs4 import BeautifulSoup as soup

@app.route("/")
def give():
  url = request.args.get('url')
  print(url)
  session = requests.Session()
  baseUrl = "http://127.0.0.1:5000/?url=http://w3schools.com/"
  linkUrl = "http://127.0.0.1:5000/link?url=http://w3schools.com/"
  imgUrl = "http:/127.0.0.1:5000/image?url=http://w3schools.com/"
  r = session.get(url)
  r.encoding = "utf-8-sig"
  bs = soup(r.content, "html.parser")
  for a in bs.findAll('a'):
        a['href'] = baseUrl + a['href']
  for link in bs.findAll('img'):
      try:
          link['src'] = imgUrl + "/" +link['src']
      except:
          pass
  for link in bs.findAll('script'):
      try:
          link['src'] = baseUrl + "/" +link['src']
      except:
          pass
  for link in bs.findAll('iframe'):
      try:
          link['src'] = baseUrl + "/" +link['src']
      except:
          pass
  for link in bs.findAll('link'):
    link['href'] = linkUrl + "/" +link['href']

  return " " +str(bs)
@app.route("/image")
def img():
  r = base64.b64encode(requests.get(request.args.get('url')).content)
  src = "data:image/png;base64," + r
  return src
@app.route("/link")
def pain():
    r = requests.get(request.args.get("url"))
    r.encoding = "utf-8-sig"
    return Response(r.text, mimetype='text/css')
if __name__ == "__main__":
  app.run("0.0.0.0",port=5000,debug=True)
