import re

headers= """
sfzx: 1
tw: 1
area: 香港特别行政区 油尖旺区
city: 油尖旺区
province: 香港特别行政区
address: ddd
geo_api_info: 123
sfcyglq: 0
sfyzz: 0
qtqk: 
ymtys: 0
"""

header = ''
for i in headers:
    if i == '\n':
        i = "',\n'"
    header += i
header=re.sub(': ',"': '",header)

ret=header[2:].replace(' ', '')+'\''
print(ret[:-4])