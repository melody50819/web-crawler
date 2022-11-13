from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep, time
import json
from common import scroll, read_json, potatomediaLogin

def openChrome(url):
    # open Chrome
    global driver
    driver = webdriver.Chrome()
    driver.get(url) #login
    sleep(5)
    craw_post(driver)

def craw_post(driver):
    address = account.getHomeUrl() #'https://www.potatomedia.co'
    post_json = []
    x = 0
    while(x < int(post_cnt)):
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        posts = soup.find_all("span", class_="article-card-article-card__FooterLikeCount--DsCDd")
        for post in posts:
            href = address + post.select_one("a").get("href")
            if href not in post_json:
                post_json.append(href)
                x+=1
                if x == int(post_cnt): break
        scroll(driver)
    print('Writing to Json...')
    with open("json/post.json", "w") as f:
        json.dump(post_json, f, indent=2)
        #f.write(soup.prettify())  輸出排版後的HTML內容 line:506
    print('Finish!')
    driver.close()

if __name__ == '__main__':
    global account, post_cnt

    post_cnt = input('Please print the post number you want to craw: ')
    start = time()
    account = read_json()
    
    openChrome(account.getHomeUrl()) #https://www.potatomedia.co/posts/recommended
    #openChrome(account.getLoginUrl()) #https://www.potatomedia.co/auth/signin
    #potatomediaLogin(driver)
    end = time()
    print("執行時間：%f 秒" % (end - start))
