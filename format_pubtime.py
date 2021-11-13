import os
import re
from datetime import datetime

re_pubtime = r'(?<=<span class="pubtime">).*?(?=</span>\s*</div>)'

dir = '/Users/aibee/codes/my/gsysbrj.github.io/chzhshch'
prefix = '缠中说禅博客'

def fmt_week(dt):
    w = dt.isoweekday()
    if w == 1:
        return '周一'
    if w == 2:
        return '周二'
    if w == 3:
        return '周三'
    if w == 4:
        return '周四'
    if w == 5:
        return '周五'
    if w == 6:
        return '周六'
    if w == 7:
        return '周日'

def repl(m):
    dt = datetime.strptime(m.group(0), '%Y/%m/%d %H:%M:%S')
    return dt.strftime('%Y/%m/%d %H:%M:%S') + ' ' + fmt_week(dt)

filenames = os.listdir(dir)
for filename in filenames:
    if filename.startswith(prefix):
        file = dir + '/' + filename
        print(file)
        content = ''
        with open(file) as f:
            content = f.read()
            content = re.sub(re_pubtime, repl, content)
        with open(file, 'w') as f:
            f.write(content)
