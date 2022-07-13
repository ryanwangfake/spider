#拿到页面的源代码
#通过re模块提取到需要的内容
import re
import requests
url = "https://movie.douban.com/chart"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}
resp = requests.get(url, headers=headers)
resp.encoding = "utf-8"
page_content = resp.text

obj = re.compile(r'<a class="nbg" href=".*?"  title="(?P<title>.*?)">.*?/ <span style="font-size:13px;">(?P<othername>.*?)</span>.*?<p class="pl">(?P<detail>.*?)</p>.*?<span class="pl">(?P<people>.*?)</span>', re.S)
data = obj.finditer(page_content)
for it in data:
    print("电影名：----")
    print(it.group("title"))
    print(it.group("othername"))
    print("时间，演员：----")
    print(it.group("detail"))
    print("评价----")
    print(it.group("people"))
    print("\n\n\n")

