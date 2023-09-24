# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


class TestTriangles(unittest.TestCase):

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 should be scalene')

    def testIsocelesTrianglesA(self):
        self.assertEqual(classifyTriangle(2,2,3),'Isoceles','2,2,3 should be isoceles')

    def testIsocelesTrianglesB(self):
        self.assertEqual(classifyTriangle(2,3,2),'Isoceles','2,3,2 should be isoceles')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle','1,2,3 is not a triangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(5,3,9),'NotATriangle','5,3,9 is not a triangle')

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(-1,1,1),'InvalidInput','Negative values are invalid')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(0,1,1),'InvalidInput','Zero values are invalid')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(201,201,201),'InvalidInput','Values over 200 are invalid')

    def testInvalidInputD(self):
        self.assertEqual(classifyTriangle('a',1,1),'InvalidInput','Non-integer values are invalid')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
