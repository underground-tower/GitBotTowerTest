#pip3 install GitPython
#pip3 install PyGithub requests
#python -m pip install --upgrade pip
from github import Github
import time,github
import bs4, requests
g = Github('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
#github.enable_console_debug_logging()
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

def UpdateFile(filedata="Filedata",commit="",filename="file_name.txt",userName="underground-tower",repoName="GitBotTowerTest"):
	global g
	user = g.get_user(userName)
	
	repo = user.get_repo(repoName)
	contents = repo.get_contents(filename, ref="main")

	repo.update_file(contents.path, commit, filedata, contents.sha, branch="main")

#UpdateFile()

ip="0.0.0.0"
while 1:

	s = requests.get('https://ifconfig.me/')
	b = bs4.BeautifulSoup(s.text, "html.parser")

	if(ip!=b):
		print(end='\r')
		print("New ip  ",b)
		UpdateFile(filedata=str(b))
		ip=b
	time.sleep(10)


