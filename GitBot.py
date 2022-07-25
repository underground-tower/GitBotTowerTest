#pip3 install GitPython
#pip3 install PyGithub requests
#python -m pip install --upgrade pip
from github import Github
import time
import bs4, requests
g = Github('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

def CreateFile(filename="file_name.txt",filedata="filedata",commit="",userName="underground-tower",repoName="GitBotTowerTest"):
	global g
	user = g.get_user(userName)
	repo = user.get_repo(repoName)
	repo.create_file(filename, commit, filedata)

def DeleteFile(filename="file_name.txt",userName="underground-tower",repoName="GitBotTowerTest"):
	global g
	user = g.get_user(userName)
	repo = user.get_repo(repoName)
	contents = repo.get_contents(filename, ref="main")
	repo.delete_file(contents.path, filename, contents.sha, branch="main")

while 0:
	try:
		DeleteFile()
	except Exception as e:
		print("EROR Delite:    ",e)
	
	time.sleep(10)
	try:
		CreateFile()
	except Exception as e:
		print("EROR Create:    ",e)	
	time.sleep(60)

	print("Update : ",time.time())

while 1:

	s = requests.get('https://2ip.ua/ru/')
	b = bs4.BeautifulSoup(s.text, "html.parser")
	a = b.select(" .ipblockgradient .ip")[0].getText()
	print(a)
	time.sleep(1)
