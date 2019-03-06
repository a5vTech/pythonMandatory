import sys
import os
import subprocess
from urllib.request import urlopen

res = urlopen('https://kea.dk')
html = res.read().decode('utf-8')

file = open('kea.html', 'w')
file.write(html)
file.close
subprocess.run('start kea.html')

#print(res)
