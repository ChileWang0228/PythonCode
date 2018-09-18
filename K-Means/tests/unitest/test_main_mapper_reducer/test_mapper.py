#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/30 17:08
# @Author  : 李强30872
# @File    : test_mapper.py.py
# @Software: PyCharm
"""
import unittest
import sys
import mapper


class TestMapper(unittest.TestCase):
    """
    # test mapper
    """

    @classmethod
    def setUpClass(cls):
        sys.stdin = {
            '62	99',
            '66	55',
            '11	145',
            '95	44',
            '60	25',
            '15	112'
        }

    def test_1(self):
        self.assertEqual(mapper.main(), None)


if __name__ == "__main__":
    unittest.main()
