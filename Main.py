import sys, os, subprocess, glob
from urllib.request import urlopen


def main():
   # getApi()
    #updateRepos()
    readmeFiles = glob.glob('**/readme.md', recursive=True)
    for readmeFile in readmeFiles:
        readme  = open(readmeFile[0:-10]+'\\readme.md', 'r')
        for line in readme:
            if "## Required reading" in line:
                print(line)

    





   
        
   
    

        
def updateRepos():
    urls = getRepoUrls()
    for repoUrl in urls:
        folderName = repoUrl[49:-4]
        if os.path.exists(folderName):
            os.chdir(folderName)
            subprocess.run('git pull ' + repoUrl)
            os.chdir('..')
        else:
            subprocess.run('git clone ' + repoUrl)

 
def getRepoUrls():
    input_file = open('api.txt', 'r')
    urls = []
    for line in input_file:
        words = line.split('"')
        index = 0
        for word in words:

            if "clone_url" in word:
                #print('Found ' + words[index +2])
                #print('URL : ' +     words[index+2])
                urls.append(words[index +2])
            index = index + 1
    return urls


def getApi():
 res = urlopen('https://api.github.com/orgs/python-elective-2-spring-2019/repos?per_page=100')  
 html = res.read().decode('utf-8')
 file = open('api.txt', 'w')
 file.write(html)
 file.close


 
if __name__ == '__main__':
    main()
