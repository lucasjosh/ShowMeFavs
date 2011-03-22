#!/usr/bin/env python

import httplib
import json
from StringIO import StringIO
import random
import sys

if len(sys.argv) != 2:
  sys.exit("You must specify your Twitter username...")
else:
  username = sys.argv[1]
  
http = httplib.HTTPConnection("api.twitter.com")
http.request('GET',"/1/users/show.json?screen_name=" + username)

u1 = http.getresponse()
user_data = u1.read()
uio = StringIO(user_data)
user_json = json.load(uio)
seed = user_json['favourites_count']
rng = seed / 20
page = random.randint(0,rng - 1) 

http.request("GET", "/1/favorites/{0}.json?page={1}".format(username,page))

r1 = http.getresponse()

data = r1.read()

io = StringIO(data)

favs =  json.load(io)

num = random.randint(0,19)
text = favs[num]['text']
by = favs[num]['user']['screen_name']
print '{0}\n\t\tfrom  {1}'.format(text, by)
