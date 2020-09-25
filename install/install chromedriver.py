import requests
import zipfile
import os
import shutil

url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
url_file = 'https://chromedriver.storage.googleapis.com/'
file_name = 'chromedriver_win32.zip'

version_response = requests.get(url)

if version_response.text:
    file = requests.get(url_file + version_response.text + '/' + file_name)
    with open(file_name, "wb") as code:
        code.write(file.content)
        
with zipfile.ZipFile('chromedriver_win32.zip', 'r') as zip_ref:
    zip_ref.extractall()
    
shutil.copyfile('chromedriver.exe', 'C:\chromedriver.exe')
os.remove('chromedriver_win32.zip')
os.remove('chromedriver.exe')
