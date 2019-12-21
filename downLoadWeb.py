# The requests.get() function takes a
# string of a URL to download.

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# You can tell that the request for this web page succeeded
# by checking the status_code attribute of the Response object.
# If it is equal to the value of requests.codes.ok, then everything
# went fine
# Incidentally, the status code for “OK” in the HTTP
# protocol is 200. You may already be familiar with the 404 status
# code for “Not Found.”

type(res)

res.status_code == requests.codes.ok

len(res.text)

# ensure that a program halts if a bad download occurs

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

# save the web page to a file on your hard drive with the standard open()
# function and write() method.

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
        playFile.write(chunk)

playFile.close()
