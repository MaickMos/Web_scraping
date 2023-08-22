from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

def downloadVideo(link, id):
    print(f"Downloading video {id} from: {link}")
    cookies = {
    '_gid': 'GA1.2.161418294.1690068274',
    '_gat_UA-3524196-6': '1',
    '__gads': 'ID=3281be1f74ab44d0-2266a3fee3e20018:T=1690068274:RT=1690068274:S=ALNI_MZODM4KH8UYK4ohXGU93iRDHgL_ig',
    '__gpi': 'UID=00000d041539819a:T=1690068274:RT=1690068274:S=ALNI_MZIvkdEiRLqePSycCVe-15roIaZuA',
    '_ga': 'GA1.2.1833992876.1690068274',
    '_ga_ZSF3D6YSLC': 'GS1.1.1690068273.1.0.1690068288.0.0.0',

    }

    headers = {
    'authority': 'ssstik.io',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,es-US;q=0.8,es;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_gid=GA1.2.161418294.1690068274; _gat_UA-3524196-6=1; __gads=ID=3281be1f74ab44d0-2266a3fee3e20018:T=1690068274:RT=1690068274:S=ALNI_MZODM4KH8UYK4ohXGU93iRDHgL_ig; __gpi=UID=00000d041539819a:T=1690068274:RT=1690068274:S=ALNI_MZIvkdEiRLqePSycCVe-15roIaZuA; _ga=GA1.2.1833992876.1690068274; _ga_ZSF3D6YSLC=GS1.1.1690068273.1.0.1690068288.0.0.0',
    'hx-current-url': 'https://ssstik.io/en',
    'hx-request': 'true',
    'hx-target': 'target',
    'hx-trigger': '_gcaptcha_pt',
    'origin': 'https://ssstik.io',
    'referer': 'https://ssstik.io/en',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',

    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': link,
        'locale': 'en',
        'tt': 'a2lQWjZl', # NOTE: This value gets changed, please use the value that you get when you copy the curl command from the network console
    }
    
    #print("STEP 4: Getting the download link")
    #print("If this step fails, PLEASE read the steps above")
    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    downloadSoup = BeautifulSoup(response.text, "html.parser")

    downloadLink = downloadSoup.a["href"]
    videoTitle = downloadSoup.p.getText().strip()
    collection = "Hacer"
    #print("STEP 5: Saving the video :)")
    mp4File = urlopen(downloadLink)
    # Feel free to change the download directory
    with open(f"D:/Users/maick/Desktop/Kelly Pero Que Monda/Codigos/Scrapping Tiktok/Videos/{Collection}-{id}.mp4", "wb") as output:
        while True:
            data = mp4File.read(4096)
            if data:
                output.write(data)
                print("Done video {id} of {collection}")
            else:
                break

print("STEP 1: Open Chrome browser")
options = Options()
options.add_argument("start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome()

# Change the tiktok link
driver.get("https://vm.tiktok.com/ZM2qk9pYA/")

# IF YOU GET A TIKTOK CAPTCHA, CHANGE THE TIMEOUT HERE
# to 60 seconds, just enough time for you to complete the captcha yourself.
time.sleep(1)

scroll_pause_time = 1
screen_height = driver.execute_script("return window.screen.height;")
i = 1

print("STEP 2: Scrolling page")
while True:
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(scroll_pause_time)
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    if (screen_height) * i > scroll_height:
        break 

# this class may change, so make sure to inspect the page and find the correct class
#LINK
className = "tiktok-c83ctf-DivWrapper"
script  = "let l = [];"
script += "document.getElementsByClassName(\""
script += className
script += "\").forEach(item => { l.push(item.querySelector('a').href)});"
script += "return l;"
urlsToDownload = driver.execute_script(script)
print(urlsToDownload)

#UserName
className = "tiktok-16ou6xi-DivTagCardDesc"
descript=BeautifulSoup(driver.page_source, "html.parser")
span = descript.find_all("span", {"class":className})

descripciones= []
for des in span:
    descripciones.append(des.getText())
print(descripciones)


print(f"STEP 3: Time to download {len(urlsToDownload)} videos")
for index, url in enumerate(urlsToDownload):
    print(f"Downloading video: {index}")
    #print(url)
    #downloadVideo(url, index)
    #time.sleep(10)