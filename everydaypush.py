import os

print("这次拥护啥要提交:",end="")
reason = input()

os.system('git add .')
os.system('git commit -m\"'+reason+'\"')
os.system('git push -u origin master')


# TODO csdn更新博文
# TODO 项目文档->概述

