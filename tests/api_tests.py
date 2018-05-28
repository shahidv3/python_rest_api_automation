# -*- coding: utf-8 -*-

import unittest
import os
import requests

from context import helpers

from helpers import csvreader
from helpers import logger
from helpers import api_crud

import nose

path = "../data/input.csv"
input=helpers.csvreader.read_csv(None,path)

print "Start executing API tests"

class test_api_ccc:
    ''' Run API automation '''
    helpers.logger.log_level()
    helpers.api_crud.api_methods_all(input)

if __name__ == '__main__':
    mytests = test_api_ccc()