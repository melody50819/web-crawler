import mechanize
br = mechanize.Browser()
br.set_handle_robots(False)

#打開除錯用的設定
br.set_debug_http(True)
br.set_debug_responses(True)
br.set_debug_redirects(True)

br.addheaders = [("user-agnet", "Mozilla/5.0")]

br.open('https://www.potatomedia.co/auth/signin')

response1 = br.follow_link(text_regex=r"cheese\s*shop", nr=1)

print(response1.info()) 