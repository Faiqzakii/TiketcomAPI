from six.moves import urllib
from io import BytesIO
import logging
import gzip
import json

from .search import SearchRequest

logger = logging.getLogger(__name__)

class Client(SearchRequest):
    def __init__(self):
        self.endpoint = 'https://gql.tiket.com/v1/hotel/graphql'

    def execute(self, query, variables=None):
        return self._send(query, variables)

    def inject_token(self, token, headername='Authorization'):
        self.token = token
        self.headername = headername

    def search(self, types='REGION', city='bali-108001534490276212', startdate='2020-10-13', page=1):
        query = self.search_hotel()

        variable = {
            "adult":1,"night":1,"page":int(page),"room":1,
            "searchType":str(types),"searchValue":str(city),"sort":"popularity",
            "startDate":str(startdate),"filter":{'propertyTypes' : ['HOTEL']}
        }

        return self.execute(query, variable)

    @staticmethod
    def _read_response(response):
        if response.info().get('Content-Encoding') == 'gzip':
            buf = BytesIO(response.read())
            res = gzip.GzipFile(fileobj=buf).read().decode('utf8')
        else:
            res = response.read().decode('utf8')
        return res

    def _send(self, query, variables):
        data = {'query': query,
                'variables': variables}
        headers = {'accept': '*/*',
                   'content-Type': 'application/json',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
                   'cookie':'__cfduid=d03e4d75bed4711efa92f47c507c389d81602339787; PHPSESSID=c7b0641c-70c8-45a9-94ce-7166d9848391; userlang=id; usercurrency=IDR; _gcl_au=1.1.553021804.1602339788; GTMUserInformation={ "userId": undefined, "email": "undefined", "fullName": "undefined undefined", "firstName": "undefined", "lastName": "undefined"}; ab.storage.deviceId.3a9cb405-9ac0-4c31-a856-3183ef998519=%7B%22g%22%3A%227912ea4d-6bef-4513-7fe5-62da911f170a%22%2C%22c%22%3A1602339788314%2C%22l%22%3A1602339788314%7D; _gid=GA1.2.664410739.1602339788; __auc=03747e9717512e4d6871c43f6b2; afUserId=9d5c45f0-b48d-47eb-9d4f-d6e8575fb92e-p; source=hotel; _uetsid=1e7c3a900b0411eba47f418c0b22b69e; _uetvid=1e7cd4c00b0411eb9ce74b3c65a26de2; _ga=GA1.1.1707321018.1602339788; amplitude_id_4232616a7b142f5eea26902a508b5860tiket.com=eyJkZXZpY2VJZCI6IjA3MWY2MzE5LTUzMTgtNGQwMS04NTc1LTdlZjFjMmI5YTYwY1IiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYwMjM0MTc0OTU1NiwibGFzdEV2ZW50VGltZSI6MTYwMjM0MTc0OTU2MSwiZXZlbnRJZCI6MywiaWRlbnRpZnlJZCI6Niwic2VxdWVuY2VOdW1iZXIiOjl9; ab.storage.sessionId.3a9cb405-9ac0-4c31-a856-3183ef998519=%7B%22g%22%3A%22af286104-a3a1-a5fe-773b-80f7edfe0c72%22%2C%22e%22%3A1602343549616%2C%22c%22%3A1602341749617%2C%22l%22%3A1602341749617%7D; _ga_VKZD5SC6KN=GS1.1.1602341747.2.1.1602341749.58'
                   }

        req = urllib.request.Request(self.endpoint, json.dumps(data).encode('utf-8'), headers)

        try:
            response = urllib.request.urlopen(req)

            response_content = self._read_response(response)

            json_response = json.loads(response_content)

            return json_response
        except urllib.error.HTTPError as e:
            print((e.read()))
            print('')
            raise e
