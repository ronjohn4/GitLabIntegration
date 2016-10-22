# Ron Johnson
# 10/20/2016

import requests
import pickle

def getToken():
    file_name = "config"
    return_val = ''

    try:
        file_object = open(file_name, 'rb')
        c = pickle.load(file_object)
        return_val = c['token']
    except:
        pass

    return return_val

def getURL():
    file_name = "config"
    return_val = ''

    try:
        file_object = open(file_name, 'rb')
        c = pickle.load(file_object)
        return_val = c['URL']
    except:
        pass

    return return_val


class glData():
    _data = []
    _headers = []
    _payload = ''
    _url = ''
    _token = ''

    def __init__(self, url, token):
        self._url = url + 'users'
        self._token = token
        self._payload = {'private_token': self._token, 'page': 1}
        self._pull_data()

    def _pull_data(self):
        r = requests.get(self._url, params=self._payload)

        # set headers
        if int(r.headers['Content-Length']) > 2:
            d = r.json()
            person = d[0]
            for key, value in person.items():
                self._headers.append(key)

            # set data
            while True:
                for person in d:
                    self._data.append(person)

                self._payload['page'] += 1
                r = requests.get(self._url, params=self._payload)
                if int(r.headers['Content-Length']) <= 2:
                    break
                d = r.json()

    def data(self):
        return self._data

    def headers(self):
        return self._headers
