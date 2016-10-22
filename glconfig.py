# Ron Johnson
# 10/20/2016

"""
GitLab Config.

Usage:
  glconfig.py  --url <newURL>
  glconfig.py  --token <newtoken>
  glconfig.py  --show
  glconfig.py  (-h | --help | -v | --version)

Options:
  -s --show     Show current configuration.
  -u --url      Set url to GitLab.
  -t --token    Set token for GitLab.
  -h --help     Show this screen.
  -v --version  Show version.
"""

from docopt import docopt
import pickle

if __name__ == '__main__':
    arguments = docopt(__doc__, version='GitLab Config 1.0')

c = {}
file_Name = "config"

try:
    fileObject = open(file_Name, 'rb')
    c = pickle.load(fileObject)
except:
    pass

if arguments['--show']:
    for key, value in c.items():
        print('{0}: {1}'.format(key, value))
if arguments['--token']:
    c['token'] = arguments['<newtoken>']
if arguments['--url']:
    c['URL'] = arguments['<newURL>']

fileObject = open(file_Name, 'wb')
pickle.dump(c, fileObject)
fileObject.close()


