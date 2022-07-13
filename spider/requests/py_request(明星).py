import requests
url = "https://www.sogou.com/web?query=薛之谦"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}
resp = requests.get(url, headers=headers)
resp.encoding = "utf-8"
#print(resp)
print(resp.text)


