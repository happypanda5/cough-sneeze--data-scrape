import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re
from subprocess import run
import os.path
import wget


#D
def download(url, page):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find(id="node_sounds")

    pattern = re.compile(r'sound_url:\s*\"(.*?)\"', re.MULTILINE | re.DOTALL)
    all_scripts = table.findAll('script', text=pattern)

    for number, script in enumerate(all_scripts):
        link = pattern.search(script.text).group(1)[2:]
        run(['wget', link])
        time.sleep(1) #pause the code for a sec to avoid spam
        print(page, number+1, )

page = 0
while (page < 20):
    page = page + 1
    url = "https://annotator.freesound.org/fsd/explore/%252Fm%252F01hsr_/?page=" + str(page)
    download(url, page)
else:
    print("Finished")