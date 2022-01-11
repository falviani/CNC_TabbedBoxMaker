# -*- coding: utf-8 -*-

import os, sys

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

RESPATH = os.path.join(os.path.dirname(__file__), "resources")
CMDPATH = os.path.join(os.path.dirname(__file__), "commands")
sys.path.append(CMDPATH)
