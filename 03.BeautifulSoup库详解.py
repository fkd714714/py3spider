#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:fkd714
@file: 03.BeautifulSoup库详解.py 
@time: 2019/02/18 
@python version: 3.7.1
"""

#######################################################################################################################
# | 解析器	| 使用方法	| 优势	| 劣势 |
# | Python标准库     | BeautifulSoup(markup, "html.parser")   	| Python的内置标准库、执行速度适中 、文档容错能力强 |
# | lxml HTML 解析器	| BeautifulSoup(markup, "lxml")	            | 速度快、文档容错能力强 | 需要安装C语言库 |
# | lxml XML 解析器	| BeautifulSoup(markup, "xml")              | 速度快、唯一支持XML的解析器 | 需要安装C语言库 |
# | html5lib	    | BeautifulSoup(markup, "html5lib")	        | 容错性最好、以浏览器的方式解析文档、生成HTML5格式文档 | 速度慢、不依赖外部扩展 |
#######################################################################################################################

from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')

'''基本使用'''
# print(soup.prettify())


'''##################################标签选择器################################'''

'''选择元素'''
# 通过这种soup.标签名 我们就可以获得这个标签的内容
# 如果文档中有多个这样的标签，返回的结果是第一个标签的内容，
# 如上面我们通过soup.p获取p标签，而文档中有多个p标签，但是只返回了第一个p标签内容
# print(soup.title)
# print(type(soup.title))
# print(soup.title.string)
# print(soup.head)
# print(soup.p)


'''获取名称'''
# 通过soup.title.name的时候就可以获得该title标签的名称，即title # #
# print(soup.title.name)


'''获取属性'''
# # 下面两种方式都可以获取p标签的name属性值# #
# print(soup.p.attrs['name'])
# print(soup.p['name'])


'''获取内容'''
# # 结果就可以获取第一个p标签的内容# #
# print(soup.p.string)


'''嵌套选择'''
# 我们直接可以通过下面嵌套的方式获取
# print(soup.head.title.string)


'''子节点和子孙节点'''
# #01 contents的使用# 子节点 #
# print(soup.p.contents)


# #02 children(迭代)的使用# 子节点 #
# print(soup.p.children)
# for i, child in enumerate(soup.p.children):
#     print(i, child)

# #03 descendants(迭代)的使用 # 子孙节点 #
# print(soup.p.descendants)
# for i, child in enumerate(soup.p.descendants):
#     print(i, child)


'''父节点和祖先节点'''
# #01 parent的使用 # 父节点 #
# print(soup.a.parent)


# #02 parents(迭代)的使用 # 父节点 #
# print(soup.a.parents)
# for i, parent in enumerate(soup.a.parents):
#     print(i, parent)


# #通过list(enumerate(soup.a.parents))可以获取祖先节点，这个方法返回的结果是一个列表，会分别将a标签的父节点的信息存放到列表中，
# 以及父节点的父节点也放到列表中，并且最后还会讲整个文档放到列表中，所有列表的最后一个元素以及倒数第二个元素都是存的整个文档的信息
# print(list(enumerate(soup.a.parents)))


'''兄弟节点'''
# #获取后面的兄弟节点
# print(soup.a.next_siblings)

# #获取前面的兄弟节点
# print(soup.a.previous_siblings)

# #获取下一个兄弟标签
# print(soup.a.next_sibling)

# #获取上一个兄弟标签
# print(soup.a.previous_sinbling)


'''##################################标准选择器################################'''

html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')

'''find_all'''
# # find_all(name,attrs,recursive,text,**kwargs) # #
# # 可以根据标签名，属性，内容查找文档  # #


# 01 name的用法
# print(soup.find_all('ul'))
# print(type(soup.find_all('ul')[0]))

# #同时我们是可以针对结果再次find_all,从而获取所有的li标签信息
# for ul in soup.find_all('ul'):
#     print(ul.find_all('li'))


# 02 attrs的用法
# print(soup.find_all(attrs={'id': 'list-1'}))
# print(soup.find_all(attrs={'name': 'elements'}))
# print(soup.find_all(id='list-1'))
# print(soup.find_all(class_='element'))

# attrs可以传入字典的方式来查找标签，但是这里有个特殊的就是class,因为class在python中是特殊的字段，
# 所以如果想要查找class相关的可以更改attrs={'class_':'element'}或者soup.find_all('',{"class":"element})，
# 特殊的标签属性可以不写attrs，例如id


# 03 text的用法
# print(soup.find_all(text='Foo'))


'''find'''
# find( name , attrs , recursive , text , **kwargs )
# find返回的匹配结果的第一个元素, find_all返回所有元素

# print(soup.find('ul'))
# print(type(soup.find('ul')))
# print(soup.find('page'))

'''其他一些类似的用法：'''
# ### find_parents()  find_parent()
# find_parents()返回所有祖先节点，find_parent()返回直接父节点。

# ### find_next_siblings()  find_next_sibling()
# find_next_siblings()返回后面所有兄弟节点，find_next_sibling()返回后面第一个兄弟节点。

# ### find_previous_siblings()  find_previous_sibling()
# find_previous_siblings()返回前面所有兄弟节点，find_previous_sibling()返回前面第一个兄弟节点。

# ### find_all_next()  find_next()
# find_all_next()返回节点后所有符合条件的节点, find_next()返回第一个符合条件的节点

# ### find_all_previous() 和 find_previous()
# find_all_previous()返回节点后所有符合条件的节点, find_previous()返回第一个符合条件的节点


'''##################################CSS选择器################################'''

html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')

'''   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
通过select()直接传入CSS选择器就可以完成选择
熟悉前端的人对CSS可能更加了解，其实用法也是一样的
.表示class #表示id
标签1，标签2 找到所有的标签1和标签2
标签1 标签2 找到标签1内部的所有的标签2
[attr] 可以通过这种方法找到具有某个属性的所有标签
[atrr=value] 例子[target=_blank]表示查找所有target=_blank的标签
'''

# print(soup.select('.panel .panel-heading'))
# print(soup.select('ul li'))
# print(soup.select('#list-2 .element'))
# print(type(soup.select('ul')[0]))

# for ul in soup.select('ul'):
#     print(ul.select('li'))


'''获取内容'''
# 通过get_text()就可以获取文本内容
# for li in soup.select('li'):
#     print(li.get_text())


'''获取属性'''
# 或者属性的时候可以通过[属性名]或者attrs[属性名]
# for ul in soup.select('ul'):
#     print(ul['id'])
#     print(ul.attrs['id'])


'''##################################总结################################'''
# * 推荐使用lxml解析库，必要时使用html.parser
# * 标签选择筛选功能弱但是速度快
# * 建议使用find()、find_all() 查询匹配单个结果或者多个结果
# * 如果对CSS选择器熟悉建议使用select()
# * 记住常用的获取属性和文本值的方法
'''######################################################################'''
