import requests
url = "https://fanyi.baidu.com/sug"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}
word = input("what you want to translate")
data = {
    "kw": word
}
resp = requests.post(url, headers=headers, data=data)
resp.encoding = "utf-8"
#print(resp.text)
print(resp.json())
print("finish")

