from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    url_path = self.path
    url_components = parse.urlsplit(url_path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)

    if "zip" in dic:
        url = 'http://api.zippopotam.us/us/'
        r = requests.get(url + dic['zip'])
        data = r.json()
        postal_code = []
        for zip_code in data:
            zip_code_location = zip_code["places"][0]["place name"]
            postal_code.append(zip_code_location)
        message = str(postal_code)        
    else:
        message = "Please enter a postal code to find"

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    self.wfile.write(message.encode())

    return