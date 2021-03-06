# -*- coding: utf-8 -*-
# Q099
# Created by JKChang
# Tag: Ring
# 09/05/2017, 15:37
# Description: 使用列表实现循环数据结构

class Ring(object):
    def __init__(self, l):
        if not len(l):
            raise "ring must have at least one element"
        self._data = l

    def __repr__(self):
        return repr(self._data)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, i):
        return self._data[i]

    def turn(self):
        last = self._data.pop(-1)
        self._data.insert(0, last)

    def first(self):
        return self._data[0]

    def last(self):
        return self._data[-1]

l = [{1:1}, {2:2}, {3:3}]
r = Ring(l)

print(r.first())
print(r.last())
print(r.__getitem__(len(r)-2))