#!/usr/bin/env python
# For backup file

import os
import time

Date = time.strftime('%Y%m%d')
Source_Path = ["/etcff","/boot"]
Target_Dir = "/backup"
Target_Path = Target_Dir+os.sep+Date

if not os.path.exists(Target_Path):
    os.makedirs(Target_Path)

for i in Source_Path:
    name = i.split('/')[-1]
    Command = "tar -zcf %s/%s.tar.gz %s >/dev/null 2>&1" % (Target_Path,name,i)
    Target = Target_Path+os.sep+name+".tar.gz"
    if os.path.exists(Target):
        print "%s already exists!" % Target
        continue
    if os.system(Command) == 0:
        print "%s backup to %s Successfully." % (i,Target_Path)
    else:
        os.remove(Target)
        print "%s Backup Failed!" % i