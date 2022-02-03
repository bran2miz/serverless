from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    url_path = self.path
    url_components = parse.urlsplit(url_path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)

    if "post code" in dic:
        url = 'https://api.zippopotam.us/'
        r = requests.get(url + dic['post code'])
        data = r.json()
        postal_code = []
        for zip_data in data:
            place_info = zip_data["places"][0]["place name"]
            postal_code.append(place_info)
        message = str(postal_code)        
    else:
        message = "Please give me a postal code to find"

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    self.wfile.write(message.encode())

    return