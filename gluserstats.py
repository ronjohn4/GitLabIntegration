# Ron Johnson
# 9/25/2016

"""
GitLab User Stats.

Usage:
  gluserstats  [-b]
  gluserstats  (-h | --help | -v | --version)

Options:
  -b --blocked  Include blocked users.
  -h --help     Show this screen.
  -v --version  Show version.
"""

from docopt import docopt
import operator
from gitlab import *
import dataprint

if __name__ == '__main__':
    arguments = docopt(__doc__, version='GitLab User Stats 1.0')

if not getToken() or not getURL():
    print('use glconfig to configure your GitLab instance.')
    exit(0)

gl_data = glUserData(getURL(), getToken())
gl_data = gl_data.data()
total_active = 0
stats = {}
data = []
output_table = []

# set header
if arguments['--blocked']:
    output_table.append(["Last Sign In Month", "Active", "Blocked", "Total", "Total Active%", "Running Active Total"])
else:
    output_table.append(["Last Sign In Month", "Active", "Total Active%", "Running Active Total"])

# gather stats
for person in gl_data:
    m = person['last_sign_in_at']
    if m:  # person has signed into GitLab
        m = m[0:7]
    else:
        m = 'never'

    stats[m] = stats.get(m, {})  # create month if not already added

    if person['state'] == 'blocked':
        stats[m]['blocked'] = stats[m].get('blocked', 0) + 1
    else:
        stats[m]['active'] = stats[m].get('active', 0) + 1
        total_active += 1


# preprocess status
stats_sorted = sorted(stats.items(), reverse=True, key=operator.itemgetter(0))
running_total = 0
for s in stats_sorted:
    running_total += s[1].get('active', 0)

    if arguments['--blocked']:
        output_table.append([str(s[0]),
                            str(s[1].get('active', 0)),
                            str(s[1].get('blocked', 0)),
                            str(s[1].get('active', 0) + s[1].get('blocked', 0)),
                            str('{0:.2f}%'.format(((s[1].get('active', 0) / total_active)*100))),
                            str(running_total)])
    else:
        if s[1].get('active', 0) > 0:
            output_table.append([str(s[0]),
                                str(s[1].get('active', 0)),
                                str('{0:.2f}%'.format(((s[1].get('active', 0) / total_active)*100))),
                                str(running_total)])

# output status table
print(dataprint.to_string(output_table, comments=None, comment_lead=''))
