#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:fkd714
@file: 04.PyQuery详解.py 
@time: 2019/03/30 
@python version: 3.7.1
"""  
from pyquery import PyQuery as pq

html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)

# PyQuery库也是一个非常强大又灵活的网页解析库，如果你有前端开发经验的，都应该接触过jQuery,那么PyQuery就是你非常绝佳的选择，
# PyQuery 是 Python 仿照 jQuery 的严格实现。语法与 jQuery 几乎完全相同，所以不用再去费心去记一些奇怪的方法了。

'''##################################初始化################################'''

'''字符串初始化'''
# doc = pq(html)
# print(doc('li'))

# 这里我们可以知道上述代码中的doc其实就是一个pyquery对象，我们可以通过doc可以进行元素的选择，其实这里就是一个css选择器，
# 所以CSS选择器的规则都可以用，直接doc(标签名)就可以获取所有的该标签的内容，
# 如果想要获取class 则doc('.class_name'),如果是id则doc('#id_name')....

'''URL初始化'''
# doc = pq(url="https://www.baidu.com", encoding='utf-8')
# print(doc('head'))


'''文件初始化'''
# doc = pq(filename='demo.html')
# print(doc('li'))


'''##################################基本CSS选择器################################'''

# CSS选择器 具体查看 http://www.w3school.com.cn/cssref/css_selectors.asp

'''查找元素'''

# # 01子元素
# children,find

# items = doc('.list')
# print(type(items))
# print(items)
# lis = items.find('li')
# print(type(lis))
# print(lis)

# 从结果里我们也可以看出通过pyquery找到结果其实还是一个pyquery对象，可以继续查找，
# 上述中的代码中的items.find('li') 则表示查找ul里的所有的li标签
# 这里可以通过children查找直接子元素，可以实现同样的效果,并且通过.children方法得到的结果也是一个pyquery对象

# li = items.children()
# print(type(li))
# print(li)


# # 02父元素
# parent,parents

# 通过.parent就可以找到父元素的内容
# items = doc('.list')
# container = items.parent()
# print(type(container))
# print(container)

# 通过.parents就可以找到祖先节点的内容
# items = doc('.list')
# parents = items.parents()
# print(type(parents))
# print(parents)

# 再次筛选
# parent = items.parents('.wrap')
# print(parent)


# # 03兄弟元素
# siblings

# li = doc('.list .item-0.active')
# print(li.siblings())
# print(li.siblings('.active'))

# 代码中doc('.list .item-0.active') 中的.tem-0和.active是紧挨着的，所以表示是交集的关系，
# 这样满足条件的就剩下一个了：thired item的那个标签了
# 这样在通过.siblings就可以获取所有的兄弟标签，当然这里是不包括自己的
# 同样的在.siblings()里也是可以通过CSS选择器进行筛选


'''遍历'''
# # 01单个元素

# li = doc('.item-0.active')
# print(li)
#
# # 02多个元素遍历
#
# lis = doc('li').items()
# print(type(lis))
# for li in lis:
#     print(li)

# 我们可以看出通过items()可以得到一个生成器，并且我们通过for循环得到的每个元素依然是一个pyquery对象。


'''获取信息'''

# # 01获取属性
# pyquery对象.attr(属性名)
# pyquery对象.attr.属性名

# a = doc('.item-0.active a')
# print(a)
# print(a.attr('href'))
# print(a.attr.href)

# 获得属性值的时候可以直接a.attr(属性名)或者a.attr.属性名


# # 02获取文本
# 通过.text()就可以获取文本信息

# a = doc('.item-0.active a')
# print(a)
# print(a.text())


# # 03获取HTML
# 通过.html()的方式可以获取当前标签所包含的html信息

# li = doc('.item-0.active')
# print(li)
# print(li.html())


'''DOM操作'''

# # 01addClass、removeClass
# 添加和删除属性

# li = doc('.item-0.active')
# print(li)
# li.removeClass('active')
# print(li)
# li.addClass('active')
# print(li)


# # 02attr,css
# 通过attr给标签添加和修改属性，如果之前没有该属性则是添加，如果有则是修改
# 也可以通过css添加一些css属性，这个时候，标签的属性里会多一个style属性

# li = doc('.item-0.active')
# print(li)
# li.attr('name', 'link')
# print(li)
# li.css('font-size', '14px')
# print(li)

# # 03remove
# 我们获取文本信息的时候可能并列的会有一些其他标签干扰，通过remove就可以将无用的或者干扰的标签直接删除，从而方便操作

# html = '''
# <div class="wrap">
#     Hello, World
#     <p>This is a paragraph.</p>
#  </div>
# '''
#
# doc = pq(html)
# wrap = doc('.wrap')
# print(wrap.text())
# wrap.find('p').remove()
# print(wrap.text())


# # 04伪类选择器

# li = doc('li:first-child')
# print(li)
# li = doc('li:last-child')
# print(li)
# li = doc('li:nth-child(2)')
# print(li)
# li = doc('li:gt(2)')
# print(li)
# li = doc('li:nth-child(2n)')
# print(li)
# li = doc('li:contains(second)')
# print(li)

# :first-child选择某个元素的第一个子元素；
# :last-child选择某个元素的最后一个子元素；
# :nth-child()选择某个元素的一个或多个特定的子元素；
# :nth-last-child()选择某个元素的一个或多个特定的子元素，从这个元素的最后一个子元素开始算；
# :nth-of-type()选择指定的元素；
# :nth-last-of-type()选择指定的元素，从元素的最后一个开始计算；
# :first-of-type选择一个上级元素下的第一个同类子元素；
# :last-of-type选择一个上级元素的最后一个同类子元素；
# :only-child选择的元素是它的父元素的唯一一个了元素；
# :only-of-type选择一个元素是它的上级元素的唯一一个相同类型的子元素；
# :empty选择的元素里面没有任何内容。


# # 05其他DOM方法
# http://pyquery.readthedocs.io/en/latest/api.html


# 更多CSS选择器可以查看
# http://www.w3school.com.cn/css/index.asp

# ## 官方文档
# http://pyquery.readthedocs.io/
