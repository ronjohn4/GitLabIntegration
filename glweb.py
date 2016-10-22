from flask import Flask
from flask import render_template, render_template_string
from flask import flash
from gluserlist import gluserlist
from flask_menu import Menu, register_menu

app = Flask(__name__)
app.config.from_object(__name__)
Menu(app=app)


@app.route('/home')
@register_menu(app, '.home', 'Home', order=1)
def gl_dashboard():
    # flash('You selected home')
    return render_template('index.html')


@app.route('/users')
@register_menu(app, '.users', 'Users', order=2)
def gl_users():
    # return 'Gl User List'

    entries = gluserlist()
    # flash('You selected users')
    return render_template('userlist.html', entries=entries)


if __name__ == '__main__':
    app.debug = True

    # set the secret key.  keep this really secret:
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

    app.run()
