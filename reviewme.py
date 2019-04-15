
import sys
import webbrowser

import bs4
import requests


def _read_blacklist():
    with open('blacklist.txt') as bl:
        blackurls = bl.read().splitlines()
    return blackurls


def handle (anchors):
    blacklist = _read_blacklist()
    for anchor in anchors:
        href = anchor.attrs['href']
        if href not in blacklist and href.startswith('http'):
            webbrowser.open_new_tab(href)


def run(url):
    resp = requests.get(url)
    if resp:
        soup = bs4.BeautifulSoup(resp.content, features='html5lib')
        anchors = soup.find_all('a')
        handle(anchors)
        sys.exit(0)
    else:
        sys.stderr.write('%s: %s' % (resp.status, resp.content))
        sys.exit(1)


if __name__ == '__main__':
    run(sys.argv[1])
