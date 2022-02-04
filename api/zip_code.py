from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    url_path = self.path
    url_components = parse.urlsplit(url_path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)
    
    url = 'https://api.zippopotam.us/us/'
    print(dic)
    r = requests.get(url + dic['post_code'])
    
    data = r.json()

    print(data)
 
    message = f"State: {data['places'][0]['state']} City: {data['places'][0]['place name']}"       
    print(message)


    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    self.wfile.write(message.encode())

    return
