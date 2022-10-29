from github import Github
from cfg import config as cfg
import requests

# Get API Key from config file
apiKey = cfg["apiKey"]
#print(apiKey)

#Create Github instance
g = Github(apiKey)
#print(g)

#Get private repo
repo = g.get_repo("katemcg93/TestPrivateRepo")
#print(repo.clone_url)

#Get download url for text file, use requests to access text within file
file_info = repo.get_contents("test.txt")
print(file_info)
url_of_file = file_info.download_url
response = requests.get(url_of_file)
data = response.text

#Use string.replace function to replace Andrew in text with Kate
new_contents = data.replace("Andrew", "Kate")
#print(new_contents)

#Commit updates to repository using path for text file
response = repo.update_file(file_info.path, "prog update file", new_contents, file_info.sha)
#print(response)