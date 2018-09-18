#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/30 17:08
# @Author  : 李强30872
# @File    : test_mapper.py.py
# @Software: PyCharm
"""
import unittest
import reducer
import sys


class TestReucer(unittest.TestCase):
    """
    test reducer
    """
    @classmethod
    def setUpClass(cls):
        sys.stdin = {
            "(51,34)	60,25",
            "(22,131)	15,112",
            "(92,111)	62,99",
            "(73,51)	95,44",
            "(22,131)	11,145",
            "(73,51)	66,55"
        }

    def test_1(self):
        self.assertEqual(reducer.main(), None)
