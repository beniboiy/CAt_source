#!/usr/bin/env python
"""
__author__ = "Yohan Francis"
__copyright__ = ""

__license__ = ""
__version__ = "0.1"
__maintainer__ = "Yohan Francis"
__email__ = "yohan.maneesh@gmail.com"
__status__ = "Development"
"""

import hashlib

hashs = hashlib.sha256('2345')

def newuser(user,password):
    user = str(user)
    password = str(password )
    for _ in range(len(user)):

