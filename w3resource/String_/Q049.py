# -*- coding: UTF-8 -*-
# Q049
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: 
# Description: Write a Python program to count and display the vowels of a given text. 

vowels = [x for x in 'aeiouAEIOU']
text = 'Information retrieval'
for i in vowels:
    print(i, text.count(i))
