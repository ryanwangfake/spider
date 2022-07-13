import re
import requests
translate = input("what you want to translate")
url = "https://fanyi.baidu.com/#en/zh/" + translate
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}

page = requests.post(url=url, headers=headers, verify=False)
page.encoding = "utf-8"
print(page.text)