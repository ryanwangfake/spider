import re

#findall：匹配字符串中所有符合正则的内容
#ls = re.findall(r"\d+", "我的电话号码是：10086")
#print(ls)

#finditer:匹配字符串中符合正则的内容(返回的是迭代器),从迭代器中拿到内容需要.group（）
#用的很多
#item = re.finditer(r"\d+", "我的电话号码是13052353274,我的母亲的电话号码是13002144755")
#for i in item:
#    print(i.group())

#search返回的是match对象，那数据需要group（）
#找到一个立马返回
#s = re.search(r"\d+", "我的电话号码是13052353274,我的母亲的电话号码是13002144755")
#print(s.search)

#match从头开始匹配
#s = re.match(r"\d+", "13052353274,我的母亲的电话号码是13002144755")
#print(s.group())

#预加载正则表达式
#obj = re.compile(r"\d+")
#item = obj.finditer("的电话号码是13052353274,我的母亲的电话号码是13002144755")
#for i in item:
#    print(i.group())
s = "<div class='hi'><span id='123'>hihihi</span></div>"
obj = re.compile(r"<div class='.*?'><span id='\d+'>(?P<hi>.*?)</span></div>", re.S)
 #re.S 让正则可以匹配换行符
result = obj.finditer(s)
for it in result:
    print(it.group("hi"))





