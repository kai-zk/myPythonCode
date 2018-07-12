 # -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 10:33:38 2018

@author: ZhangKai
"""

# o和1相当于一个开关，为0时打开b开关，为1时打开a开关
# 0 and 'a' or 'b'
# IN[1]:'b'

# 1 and 'a' or 'b'
# IN[2]:'a'

# lambda s:""

# str的方法：
# join， split
# ljust
    # 'abc'.ljust(10)
    # Out[13]: 'abc  



def info(object, spacing=15, collapse=0):
    """
    遍历一遍Object对象，把里面可以被调用的方法及方法的doc string打印出来
    """
    # 第一步：提取出当前object可以被调用的方法列表
    # callable(getattr(object, method)) 哪些是可以被调用的
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    # print(methodList)
    # 需要把doc string的内容显示出来
    processFun = collapse and (lambda s:" ".join(s.split())) or (lambda s:s)
    
    # 打印出方法的名称及其文档的说明
    print('\n\n'.join(["【%s】 %s"%(method.ljust(1),processFun(str(getattr(object,method).__doc__))) for method in methodList
            ]))
    
    
# Test Code：
s = 'str'
info(s,collapse=1)
