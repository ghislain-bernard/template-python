#!/usr/bin/env python3
#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#

import unittest

#----------------------------------------------------------------------------------------------------------------------#

import template

class TestTemplate(unittest.TestCase):

  def test_project(self):
    self.assertTrue(hasattr(template, 'PROJECT_NAME'))
    self.assertTrue(hasattr(template, 'PROJECT_VERSION_MAJOR'))
    self.assertTrue(hasattr(template, 'PROJECT_VERSION_MINOR'))
    self.assertTrue(hasattr(template, 'PROJECT_VERSION_PATCH'))
    self.assertTrue(hasattr(template, 'PROJECT_VERSION'))

#----------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
  unittest.main()

#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#
