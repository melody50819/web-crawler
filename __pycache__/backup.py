# cookies = driver.get_cookies()
# driver1 = webdriver.Chrome()
# driver1.get("https://www.potatomedia.co/posts/recommended") 
# sleep(2)
# for cookie in cookies:
#     cookie_list= {
#         'domain':".potatomedia.co",
#         'expiry': cookie["expiry"],
#         #'hostOnly': cookie["hostOnly"],
#         'httpOnly': cookie["httpOnly"],
#         'name': cookie["name"],
#         'path': '/',
#         #'sameSite': cookie["sameSite"],
#         #'secure': cookie["secure"],
#         #'session': cookie["session"],
#         #'storeId': cookie["storeId"],
#         'value': cookie["value"],
#     }
#     driver1.add_cookie(cookie)
# driver1.get("https://www.potatomedia.co/posts/recommended") 

# print(driver.get_cookie('__gpi'))
# driver.refresh()