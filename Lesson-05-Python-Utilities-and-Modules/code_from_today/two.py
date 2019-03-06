import one
from one import greeting

import sys
import os
import subprocess
from urllib.request import urlopen
from urllib.error import HTTPError

while True:

    try:

        # 'https://github.com/python-elective-2-spring-2019/Lesson-05-Python-Utilities-and-Modules'
        url = input('Please specify the url you want to be downloaded : ')
        res = urlopen(url)
        html = res.read().decode('utf-8')

        file = open('kea.html', 'w')
        file.write(html)

        subprocess.run(['open', html])

        break

    except HTTPError as err:
        print('Url does not exist please type in a valid one! ', err)
        continue



sys.exit()


#print(html)


#file.write(html)

#print(html)


       






#os.mkdir('XXX')
os.chdir('XXX')

subprocess.run(['git', 'clone', 'https://github.com/python-elective-2-spring-2019/Lesson-05-Python-Utilities-and-Modules.git'])











print(greeting())



one.main()
