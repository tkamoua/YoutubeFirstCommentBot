import bs4
import requests
from selenium.webdriver.common.keys import Keys
import pprint
import time

from selenium import webdriver

# Start ~5 min before video scheduled release
# Just change the url to the url of the channel you want to bot
# change the prevVid variable to the name of the current newest video.
# Change the message variable to the comment you want to say
# Change the options.add_argument path to the path of your chrome User Data
# Change the browser variable path to the path of your chromedriver
# Close all instances of chrome
# Run python commentBot.py in terminal



iterator = 0
xd=True
while xd:
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=C:\Users\Basel\AppData\Local\Google\Chrome\User Data")
    url = "https://www.youtube.com/user/MrBeast6000"
    prevVid = "Last To Leave Pool Of $20,000 Keeps It"
    message = '1'
    
    iterator+=1
    print(iterator)
    
    
    req = requests.get(url)
    #mrbeast = open('mrbeast.html','w')
    #mrbeast.write(req.text)
    #mrbeast.close()

    soup = bs4.BeautifulSoup(req.text, features="lxml")

    video = soup.select("ul.yt-lockup-meta-info > li:nth-child(1)")[0].getText()
 
    #if video != "Last To Leave Pool Of $20,000 Keeps It - Duration: 17 minutes.":
    print(video)
    if True:
        xd=False
        
        print("video found")
       
        #browser.get('https://www.youtube.com/user/MrBeast6000')
        browser = webdriver.Chrome(executable_path=r"C:\Users\Basel\Desktop\chromedriver.exe",options=options)
        browser.get(url)
        linkElem = browser.find_element_by_id("video-title")
        while linkElem.text == prevVid:
            browser.refresh()
            linkElem = browser.find_element_by_id("video-title")
        linkElem.click()


        browser.execute_script("window.scrollTo(0, document.body.scrollHeight + 2000);")
        time.sleep(.5)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight + 500);")
        commentBool = True
        while commentBool:
            try:
                commentElem = browser.find_element_by_id("placeholder-area")
                commentBool=False
            except:
                print("Try again")

        commentElem.click()
        typeElem = browser.find_element_by_id("contenteditable-root")
        typeElem.send_keys(message)
        time.sleep(.1)
        commentButton = browser.find_element_by_id("submit-button")
        commentButton.click()



