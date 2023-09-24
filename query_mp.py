#!/usr/bin/env python3
import os, sys, json
from mp_api.client import MPRester
from monty.json import MontyEncoder

key_helpstr="""==========================================================
You need to obtain a materials project API key!
Go to https://materialsproject.org
Click on 'Login' to login/create an account.
Then go to Dashboard and 'Generate API Key'.
Grab the character string an place it in an
environment variable MP_API_KEY like this:

  export MP_API_KEY="<string>"
==========================================================
"""

usagestr="""
Usage: query_mp.py <include one of> -- <must include>
"""

if 'MP_API_KEY' not in os.environ or os.environ['MP_API_KEY'] == "":
    print(key_helpstr)
    exit(1)
mp_api_key =  os.environ['MP_API_KEY']

if len(sys.argv) <= 1:
    print(usagestr)
    exit(1)

chemsys = []
j = 1
for i in range(1,len(sys.argv)):
    arg = sys.argv[i]
    if arg == "--":
        j = i+1
        break
    chemsys += [arg]
else:
    j = len(sys.argv)

elements = []
for i in range(j, len(sys.argv)):
    arg = sys.argv[i]
    elements += [arg]

if len(chemsys) > 0:
    chemsys = "-".join(chemsys)
else:
    chemsys = None

print("QUERY:",elements, chemsys,file=sys.stderr)

with MPRester(mp_api_key) as mpr:
    docs = mpr.summary.search(elements=elements,
                              chemsys=chemsys)

#print(type(docs[0]))
print(json.dumps(docs, cls=MontyEncoder))
#print(docs)
