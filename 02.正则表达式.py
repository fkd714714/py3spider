#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:fkd714
@file: 02.正则表达式.py 
@time: 2019/02/16 
@python version: 3.7.1
"""  

# '''常见匹配模式'''
# | 模式| 描述|
# \w      匹配字母数字及下划线
# \W      匹配非字母数字下划线
# \s      匹配任意空白字符，等价于[\t\n\r\f]
# \S      匹配任意非空字符
# \d      匹配任意数字
# \D      匹配任意非数字
# \A      匹配字符串开始
# \Z      匹配字符串结束，如果存在换行，只匹配换行前的结束字符串
# \z      匹配字符串结束
# \G      匹配最后匹配完成的位置
# \n      匹配一个换行符
# \t      匹配一个制表符
# ^       匹配字符串的开头
# $       匹配字符串的末尾
# .       匹配任意字符，除了换行符，re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符
# [....]  用来表示一组字符，单独列出：[amk]匹配a,m或k
# [^...]  不在[]中的字符：[^abc]匹配除了a,b,c之外的字符
# *       匹配0个或多个的表达式
# +       匹配1个或者多个的表达式
# ?       匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
# {n}     精确匹配n前面的表示
# {m,m}   匹配n到m次由前面的正则表达式定义片段，贪婪模式
# a|b     匹配a或者b
# ()      匹配括号内的表达式，也表示一个组
#

import re
import requests


'''re.match()'''
'''尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配的话，match（）就会返回None'''
# 语法如下：
# re.match(pattern,string,flags=0)

content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))

'''最常规的匹配'''
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$', content)
# print(result)

# # #result.group()获取匹配的结果 # #
# print(result.group())
# # #result.span()获去匹配字符串的长度范围 # #
# print(result.span())


'''泛匹配'''
# result = re.match('^Hello.*Demo$', content)


'''匹配目标'''
'''如果为了匹配字符串中具体的目标，则需要通过（）括起来，例子如下：'''
# result = re.match('^Hello\s(\d+)\sWorld.*Demo$', content)
# print(result)
# # 通过re.group()获得结果后，如果正则表达式中有括号，则re.group(1)获取的就是第一个括号中匹配的结果
# print(result.group(1))
# print(result.span())


'''贪婪匹配'''

'''# 从结果中可以看出只匹配到了7，并没有匹配到1234567，
   # 出现这种情况的原因是前面的.* 给匹配掉了，
   # .*在这里会尽可能的匹配多的内容，也就是我们所说的贪婪匹配，
   # 如果我们想要匹配到1234567则需要使用下面的非贪婪模式'''

# result = re.match('^He.*(\d+).*Demo$', content)
# print(result)
# print(result.group(1))


'''非贪婪匹配'''
# result = re.match('^he.*?(\d+).*Demo',content)
# # 多了一个问号，匹配尽可能少的数字
# # 匹配尽量写成 .*? 形式


'''匹配模式'''
'''很多时候匹配的内容是存在换行的问题的，这个时候的就需要用到匹配模式re.S来匹配换行的内容'''

# content = '''Hello 1234567 World_This
# is a Regex Demo
# '''
# result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
# print(result.group(1))


'''转义'''
'''我们要匹配的内容中存在特殊字符的时候，就需要用到转义符号\ '''
# content = 'price is $5.00'
# result = re.match('price is \$5\.00', content)
# print(result)


###############################################################################
# #总结：尽量使用泛匹配、使用括号得到匹配目标、尽量使用非贪婪模式、有换行符就用re.S # #
###############################################################################


''' re.search '''
'''扫描整个字符串并返回第一个成功的匹配。'''

# content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# result = re.match('Hello.*?(\d+).*?Demo', content)
# print(result)
#
# result = re.search('Hello.*?(\d+).*?Demo', content)
# print(result)
# print(result.group(1))


###########################################
# #总结：为匹配方便，能用search就不用match # #
###########################################


# ################中间插个小练习######################## #

html = '''
<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>'''

# # 齐秦 往事随风
# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
# if result:
#     print(result.group(1), result.group(2))
#
#
# # 任贤齐 沧海一声笑
# result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
# if result:
#     print(result.group(1), result.group(2))
#
#
# # beyond 光辉岁月
# result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html)
# if result:
#     print(result.group(1), result.group(2))


# ################小练习结束######################## #


''' re.findall '''
'''搜索字符串，以列表形式返回全部能匹配的子串。'''

# # 例1
# results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(results)
# print(type(results))
# for result in results:
#     print(result)
#     print(result[0], result[1], result[2])


# # 例2
# # \s*? 这种用法其实就是为了解决有的有换行，有的没有换行的问题
# # (<a.*?>)? 这种用法是因为html中有的有a标签，有的没有的，？表示匹配一个或0个，正好可以用于匹配
# results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)
# print(results)
# for result in results:
#     print(result[1])


''' re.sub '''
'''替换字符串中每一个匹配的子串后返回替换后的字符串。'''
'''re.sub(正则表达式，替换成的字符串，原字符串)'''

content = "Extra things hello 123455 World_this is a regex Demo extra things"

# # 例1
# content = re.sub('\d+', '', content)
# print(content)

# # 例2
# # 在有些情况下我们替换字符的时候，还想获取我们匹配的字符串，然后在后面添加一些内容，可以通过下面方式实现：
# # 这里需要注意的一个问题是\1是获取第一个匹配的结果，为了防止转义字符的问题，我们需要在前面加上r
# content = re.sub('(\d+)', r'\1', content)
# print(content)

# # 例3
# html = re.sub('<a.*?>|</a>', '', html)               #删除所有a标签
# print(html)
# results = re.findall('<li.*?>(.*?)</li>', html, re.S)
# print(results)
# for result in results:
#     print(result.strip())


''' re.compile '''
'''将正则表达式编译成正则表达式对象，方便复用该正则表达式'''

# content = '''Hello 1234567 World_This
# is a Regex Demo'''
# pattern = re.compile('Hello.*Demo', re.S)
# result = re.match(pattern, content)
# # result = re.match('Hello.*Demo', content, re.S)    #等价于上一条代码
# print(result)


# #######################实战练习######################## #
# #####################豆瓣网书籍信息###################### #

content = requests.get('https://book.douban.com/').text
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
results = re.findall(pattern, content)
for result in results:
    url, name, author, date = result
    author = re.sub('\s', '', author)
    date = re.sub('\s', '', date)
    print(url, name, author, date)


