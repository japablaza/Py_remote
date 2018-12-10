import json
import requests
import os
import  subprocess

# https://api.foursquare.com/v2/venues/explore?near=Chicago&query=coffee&
# client_id=AHEGEA3GLJIRXUBTHGCJSBZUGSNHBQMP4YUM1Z4HSJFYFDDP&
# client_secret=AYUTF5UIHM2CNLTXDQE0WBFMTXPBKYIKYC03GRIIUJR0MOR2&v=20181209

byte_current_date = subprocess.check_output(['date', '+%Y%m%d'])
current_date = byte_current_date.decode('utf-8').rstrip()

SQUARE_ID = os.environ.get('OPEN_4SQUARE_ID')
SQUARE_SEC = os.environ.get('OPEN_4SQUARE_SECRET')

url_base = 'https://api.foursquare.com/v2/venues/explore?'
url_near = 'near=' + 'Chicago'
url_query_cafe = '&query=coffee&'
url_client_id = 'client_id=' + str(SQUARE_ID)
url_client_secret = '&client_secret=' + str(SQUARE_SEC)
url_date = '&v=' + current_date
url_foursquare = url_base + url_near + url_query_cafe + url_client_id + url_client_secret + url_date

print(url_foursquare)
