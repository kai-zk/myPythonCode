# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def minMax(L):
    # 对输入参数进行判断，可以使用assert断言
    assert(len(L) > 0)
    # 在参数合法的情况下，做真正的逻辑    
    if len(L) <= 0:
        print('Input Error')
        return None
    # 返回一个合法的输出值
    return myminMax(L, 0, len(L)-1)       

def myminMax(L, start, end):
    """
    返回一个元组，用来记录list的最大值和最小值
    """
    if end - start <= 1:
        return (max(L[start],L[end]), min(L[start],L[end]))
    else:
        # 把L分为两部分，分别调用这个方法myminMax
        # 得到（max1,min1) 和 （max2,min2）
        max1,min1 = myminMax(L, start, (start+end)//2)
        max2,min2 = myminMax(L, (start+end)//2+1, end)
        # 比较max1，max2可以得到最终的最大值
        # 比较min1，min2可以的到最终的最小值
        return (max(max1,max2),min(min1,min2))
    
    
# Test Case
L = [3,5,6,1,7,-5,21,0,75,-45,23]
print(minMax(L))

# (start+end)/2 可以优化为 start + (end-start)/2 防止内存溢出