#!/usr/bin/env python

class test(object):
    def __init__(self,xixi):
        self.a=xixi
    def __enter__(self):
        print 'haha comein'
        return self.a
    def __exit__(self,type,value,traceback):
        print 'haha come out'
        
with test("qq") as t:
    print t