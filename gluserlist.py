# Ron Johnson
# 9/25/2016

"""
GitLab User List.

Usage:
  gluserlist.py  [-b]
  gluserlist.py  (-h | --help | -v | --version)

Options:
  -b --blocked  Include blocked users.
  -h --help     Show this screen.
  -v --version  Show version.
"""

from docopt import docopt
from gitlab import *
import dataprint

if __name__ == '__main__':
    arguments = docopt(__doc__, version='GitLab User List 1.0')

total_active = 0
stats = {}
headers = []
data = []

if not getToken() or not getURL():
    print('use glconfig to configure your GitLab instance.')
    exit(0)

gld = glData(getURL(), getToken())
gl_data = gld.data()

# set header
output_table = [["Name", "State", "Username", "email", "Last sign in at", "is admin"]]

# gather data
for person in gl_data:
    if person['state'] == 'active' or arguments['--blocked'] == True:
        output_table.append([person['name'],
                             person['state'],
                             person['username'],
                             person['email'],
                             person['last_sign_in_at'],
                             person['is_admin']
                             ])

print(dataprint.to_string(output_table, comments=None, comment_lead=''))
