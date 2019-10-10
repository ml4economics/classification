# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 11:59:59 2019

@author: Karsten
"""

class DataDescriptor:
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Retrieving', self.name)
        return self.val

    def __set__(self, obj, val):
        print('Updating', self.name)
        self.val = val
        
    def __delete__(self, obj):
        print('Deleting', self.name)
        del self.val
        
class MyClass:
    x = DataDescriptor(10, 'var "x"')


class PropertySample:
    def __init__(self, initval=None):
        self._x = initval

    @property
    def x(self):
        print('Retrieving _x')
        return self._x

    @x.setter
    def x(self, value):
        print('Setting _x')
        self._x = value

    @x.deleter
    def x(self):
        print('Deleting _x')
        del self._x