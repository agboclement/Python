# -*- coding: UTF-8 -*-
# Q024
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: 
# Description: Write a Python program to check whether a string starts with specified characters. 

def func(text, ch):
    return True if text.startswith(ch) else False

print(func('david','Da'))
print(func('david','da'))
