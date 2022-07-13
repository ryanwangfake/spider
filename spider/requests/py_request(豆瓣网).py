import requests
url = "https://movie.douban.com/chart"      #如果很长，需要封装
#param = {
#}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}
resp = requests.get(url, headers=headers)
resp.encoding = "utf-8"
#print(resp.text)
print(resp.json())
resp.close()#关闭访问，断开连接

