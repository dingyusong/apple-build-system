#!/usr/bin/env python3

import os
from build_ipa import IPABuilder

scriptsDir=os.path.dirname(os.path.abspath(__file__))
demoDir=os.path.dirname(scriptsDir)

path_xp = os.path.join(demoDir,'projects/demo01/demo01.xcodeproj')
builder = IPABuilder(path_xp=path_xp)
builder.exec()

