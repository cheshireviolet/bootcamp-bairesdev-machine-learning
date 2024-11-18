import json
import requests
import os

#Creates a CFV dataset with cards from the clans below
_clans = {'pale moon', 'kagero', 'narukami'}
_path = 'cfv/'

for a in _clans:
    response = requests.get("https://card-fight-vanguard-api.ue.r.appspot.com/api/v1/cards?pagesize=1000&clan="+a)
    response_dict = json.loads(response.text)
    _newpath = _path+a+'/'
    os.makedirs(_newpath)
    for i in response_dict['data']:
        if(i['format']=='Premium Standard'):
            img_data = requests.get(i['imageurljp']).content
            with open(_newpath + i['imageurljp'].split('/')[-1], 'wb') as handler:
                handler.write(img_data)
print('\nDone!')
