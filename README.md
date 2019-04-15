
This is a quick script to make it easier to review or think about
all the stuff listed in the weekly placement updates. Given a
URL it uses the `webbrowser` modules to open all the `https` and
`http` links on that URL which are not listed in the `blacklist.txt`
file.

First install the requirements (use whatever variation on this you
prefer, there are many):

```
python -m virtualenv -p python3 .venv
. .venv/bin/activate
pip install -r requirements.txt
```

Pick a URL for a pupdate (or anything else) and run the script:

```
python reviewme.py https://anticdent.org/placement-update-19-14.html
```
