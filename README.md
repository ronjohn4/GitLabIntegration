# GitLab Integration scripts

GitLab Integrations is a set of python scripts access a GitLab instance via token.  Use glconfig to set the GitLab access configuration used by all other scripts.  Scripts are command line Posix compliant commands and should give sufficient help.

`gitlab.py` - backend data access using the token saved by glconfig.py 

`glconfig.py` - sets the authentication and URL for your instance of GitLab.  Run glconfig -h to get the full details.

`gluserlist.py` - list of users in column format.

`gluserlistCSV.py` - same as gluserlist but outputs CSV data and all columns available

`gluserliststats.py` - count of users by month last signed in.  Helps finds users that can be removed.

`glweb.py` - web UI.  Work in progress.
