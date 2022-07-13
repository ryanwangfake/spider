#拿到页面源代码，提取到子页面的地址
#拿到图片的地址
#下载图片

#拿到页面源代码
import requests
from bs4 import BeautifulSoup
import time
#proxies = {
#    "https": "https://42.192.22.233"
#}
url = "https://www.umei.cc/bizhitupian/weimeibizhi/"
headers = {
    "user-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
resp = requests.get(url, headers=headers)
resp.encoding = "utf-8"
page_content = resp.text
#print(page_content)

#把源代码交给beautifulsoup
main_page = BeautifulSoup(resp.text, "html.parser")
name = main_page.find("ul", class_="pic-list after").find_all("span")
href = main_page.find("ul", class_="pic-list after").find_all("a")
#name = main_page.find_all("span", attrs{"class" = "table"})
#print("名称：------")
print("--------------")
#print(name)
#print("\n\n")
#print("子页面地址：-----")
#print(href)
print("--------------")
for a in href:
    child_href = a.get('href')
    final_href = "https://www.umei.cc" + child_href
    #print(final_href)
    print("-------------")
    #拿到子页面的源代码
    child_href_resp = requests.get(final_href, headers=headers)
    child_href_resp.encoding = "utf-8"
    child_href_text = child_href_resp.text

    #从子页面中拿到下在路径
    href_page = BeautifulSoup(child_href_text, "html.parser")
    d = href_page.find("section", class_="img-content")
    download = d.find("img")
    img = download.get("src")
    #print(img)
    print("--------")

    #下载图片
    img_resp = requests.get(img)
    print("-----")

    #取最后几个数为名字
    img_name = img.split("/")[-1]
    with open("img/"+img_name, mode="wb") as f:#写入image文件夹
        f.write(img_resp.content) #把文件保存

    print("over")
    print("\n")
    time.sleep(0.8)

print("all over--------------------all over!!!!!!")









