import requests

TEQUILA_ENDPOINT = 'https://tequila-api.kiwi.com'
TEQUILA_API_KEY = 'API KEY'

class FlightSearch:
    
    def get_destination_code(self, city_name):
        loc_endpoint = f'{TEQUILA_ENDPOINT}/locations/query'
        headers = {'apikey': TEQUILA_API_KEY}
        query = {'term': city_name, 'location_types': 'city'}
        response = requests.get(url=loc_endpoint, headers=headers, params=query)
        result = response.json()['locations']
        code = result[0]['code']
        
        return code