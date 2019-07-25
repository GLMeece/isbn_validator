#! /usr/bin/env python
# -*- coding: utf-8 -*-

def allSame(s):
    return not [x for x in s if x != s[0]]


def hasDigit(s):
    return any([x.isdigit() for x in s])


def getVersion(data):
    data = data.splitlines()
    return [x_y for x_y in zip(data, data[1:]) if len(x_y[0]) == len(x_y[1]) and allSame(x_y[1]) and hasDigit(x_y[0]) and "." in x_y[0]][0][0]
