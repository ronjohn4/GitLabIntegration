import requests


class glData():
    _data = []
    _headers = []
    _payload = ''
    _url = ''
    _token = ''

    def __init__(self):
        self._url = 'https://gitlab.spectrumxg.com/api/v3/users'
        self._token = '4mS2Mkoo8gRfnT83zP6t'  # Created in GitLab
        self._payload = {'private_token': self._token, 'page': 1}
        self._pull_data()
        print('url:{0}'.format(self._url))

    def _pull_data(self):
        r = requests.get(self._url, params=self._payload)

        # set headerz
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
                if int(r.headers['Content-Length']) > 2:
                    break
                d = r.json()

    def data(self):
        return(self._data)

    def headers(self):
        return(self._headers)