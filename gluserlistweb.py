from flask import Flask
from gitlab import *

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World"

# {'identities': [], 'state': 'active', 'skype': '', 'can_create_project': True, 'id': 277, 'can_create_group': True,
# 'linkedin': '', 'created_at': '2016-09-29T19:46:46.321Z', 'website_url': '', 'username': 'daveryan',
# 'projects_limit': 10, 'is_admin': False, 'bio': None, 'two_factor_enabled': True,
# 'web_url': 'https://gitlab.spectrumxg.com/u/daveryan', 'email': 'david.d.ryan@charter.com', 'external': False,
# 'color_scheme_id': 1, 'confirmed_at': '2016-09-29T19:47:02.992Z', 'location': None,
# 'last_sign_in_at': '2016-09-29T19:47:02.999Z', 'name': 'David Ryan',
# 'avatar_url': 'https://secure.gravatar.com/avatar/1c17ac50314193b70a3193d823a933a6?s=80&d=identicon',
# 'twitter': '', 'current_sign_in_at': '2016-09-29T19:47:02.999Z', 'theme_id': 2}
@app.route('/list')
def list():
    formatted_return = ''

    if not getToken() or not getURL():
        print('use glconfig to configure your GitLab instance.')
        exit(0)

    gld = glData(getURL(), getToken())
    gl_data = gld.data()

    for u in gl_data:
        formatted_return += '{0} {1}<br>'.format(u['name'], u['state'])

    return formatted_return


if __name__ == "__main__":
    app.debug = True
    app.run(debug=True)
