import requests  
from bs4 import BeautifulSoup 
import re  
import sys  


if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the TED Talk URL")

# url = "https://www.ted.com/talks/jia_jiang_what_i_learned_from_100_days_of_rejection"

# url = "https://www.ted.com/talks/ken_robinson_says_schools_kill_creativity"

r = requests.get(url, timeout=10)

print("Download about to start")

soup = BeautifulSoup(r.content, features="lxml")

for val in soup.findAll("script"):
    if (re.search("talkPage.init", str(val))) is not None:
        RESULT = str(val)

result_mp4 = re.search(r"(?P<url>https?://[^\s]+)(mp4)", RESULT).group("url")
mp4_url = result_mp4.split('"')[0]

print("Downloading video from ..... " + mp4_url)

file_name = mp4_url.split("/")[len(mp4_url.split("/")) - 1].split("?")[0]

print("Storing video in ..... " + file_name)


r = requests.get(mp4_url, timeout=10)

with open(file_name, "wb") as f:
    f.write(r.content)


print("Download Process finished")
