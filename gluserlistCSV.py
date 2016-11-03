# Ron Johnson
# 9/25/2016

"""
GitLab User List to CSV.

Usage:
  gluserlistCSV  [-b]
  gluserlistCSV  (-h | --help | -v | --version)

Options:
  -b --blocked  Include blocked users.
  -h --help     Show this screen.
  -v --version  Show version.
"""

from docopt import docopt
from gitlab import *

if __name__ == '__main__':
    arguments = docopt(__doc__, version='GitLab User List CSV 1.0')

if not getToken() or not getURL():
    print('use glconfig to configure your GitLab instance.')
    exit(0)

total_active = 0
stats = {}
gld = glUserData(getURL(), getToken())
gl_data = gld.data()
headers = gld.headers()

# output header
for value in headers:
    print('"{0}",'.format(value), end="")
print()

# output CSV
for person in gl_data:
    if person['state'] == 'active' or arguments['--blocked'] is True:
        for key, value in person.items():
            print('"{0}",'.format(value), end="")
        print()
