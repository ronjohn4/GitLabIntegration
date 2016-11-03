from flask import Flask, render_template, flash
from gitlab import *

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def home():
    # flash('New entry was successfully posted')
    # flash('This is a second flash')
    return render_template('home.html')


@app.route('/hello')
def hello():
    return "Hello World"


@app.route('/list')
def list():
    return_list = []

    if not getToken() or not getURL():
        print('use glconfig to configure your GitLab instance.')
    else:
        gld = glUserData(getURL(), getToken())
        gl_data = gld.data()

        for i, u in enumerate(gl_data):
            if u['state'] == 'active':
                return_list.append({
                    'name': u['name'],
                    'email': u['email'],
                    'state': u['state'],
                    'last_sign_in_at': u['last_sign_in_at'],
                    'seq': i
                })

    def getKey(item):
        return '{0}{1}'.format(item['last_sign_in_at'], item['name'])

    sorted_return_list = sorted(return_list, reverse=True, key=getKey)
    for i, item in enumerate(sorted_return_list):
        item['seq'] = i+1
    sorted_return_list = sorted(sorted_return_list, key=getKey)
    return render_template('show_users.html', entries=sorted_return_list)


if __name__ == '__main__':
    app.debug = True

    # set the secret key.  keep this really secret:
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

    app.run()

