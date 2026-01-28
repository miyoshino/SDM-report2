#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        # 追加したテストケース

        def test_case_01(self):
                self.assertEqual(250000, calc(500, 500))

        def test_case_02(self):
                self.assertEqual(1, calc(1, 1))

        def test_case_03(self):
                self.assertEqual(998001, calc(999, 999))

        # 境界値（無効）のテスト

        def test_case_04(self):
                self.assertEqual(-1, calc(0, 500))

        def test_case_05(self):
                self.assertEqual(-1, calc(1000, 500))

        def test_case_06(self):
                self.assertEqual(-1, calc(500, 0))

        # 実数値・文字列のテスト

        def test_case_07(self):
                self.assertEqual(-1, calc(500, 1000))

        def test_case_08(self):
                self.assertEqual(-1, calc(-10, 500))

        def test_case_09(self):
                self.assertEqual(-1, calc(1.5, 500))
        
        # 特殊な入力のテスト

        def test_case_10(self):
                self.assertEqual(-1, calc(500, "aaa"))

        def test_case_11(self):
                self.assertEqual(-1, calc(None, 500))