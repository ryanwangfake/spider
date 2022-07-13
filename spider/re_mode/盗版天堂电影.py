import re
import requests
url = "https://www.dytt89.com/"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}
resp = requests.get(url, headers=headers, verify=False)#verify=False去掉验证
resp.encoding = "gb2312"#(gbk)
page_content = resp.text
#print(page_content)
project = re.compile(r"""<li><a href='(?P<child_href>.*?)' title="(?P<title>.*?)">""", re.S)
result = project.finditer(page_content)

child_href_list = []
for it in result:
    child_href = it.group("child_href")
    title = it.group("title")
    final_child_href = "https://www.dytt89.com" + child_href
    child_href_list.append(final_child_href)
    print(title)
    print(final_child_href)
    print("\n")





