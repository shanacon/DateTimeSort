import os
from datetime import datetime
directory = os.getcwd()
dict = {}
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and filename != 'DateTimeSort.py':
        statinfo = os.stat(f)
        dict[f] = datetime.fromtimestamp(statinfo.st_mtime)
list = sorted(dict.items(), key=lambda x:x[1])
count = 0
for item in list :
    ext = os.path.splitext(item[0])[1]
    os.rename(item[0], str(count).zfill(8) + ext)
    count += 1