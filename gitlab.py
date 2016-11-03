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


class glUserData():
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
        self._data = []

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
                # break    #use for shorter dev cycles

    def data(self):
        return self._data

    def headers(self):
        return self._headers

# {'identities': [], 'state': 'active', 'skype': '', 'can_create_project': True, 'id': 277, 'can_create_group': True,
# 'linkedin': '', 'created_at': '2016-09-29T19:46:46.321Z', 'website_url': '', 'username': 'daveryan',
# 'projects_limit': 10, 'is_admin': False, 'bio': None, 'two_factor_enabled': True,
# 'web_url': 'https://gitlab.spectrumxg.com/u/daveryan', 'email': 'david.d.ryan@charter.com', 'external': False,
# 'color_scheme_id': 1, 'confirmed_at': '2016-09-29T19:47:02.992Z', 'location': None,
# 'last_sign_in_at': '2016-09-29T19:47:02.999Z', 'name': 'David Ryan',
# 'avatar_url': 'https://secure.gravatar.com/avatar/1c17ac50314193b70a3193d823a933a6?s=80&d=identicon',
# 'twitter': '', 'current_sign_in_at': '2016-09-29T19:47:02.999Z', 'theme_id': 2}
