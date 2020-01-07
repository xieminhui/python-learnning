"""
@Date: 2020-01-06 19:16:18
@LastEditors: xieminhui
@LastEditTime: 2020-01-06 19:35:25
"""
"""
@Date: 2020-01-06 19:16:18
@LastEditors: xieminhui
@LastEditTime: 2020-01-06 19:16:34
"""
from urllib.request import urlopen

str = urlopen(
    "http://mock.bobo.netease.com/mockjsdata/96/open/api/pay/privilege/autorenew/turnoff"
)
for line in urlopen(
    "http://mock.bobo.netease.com/mockjsdata/96/open/api/pay/privilege/autorenew/turnoff"
):
    line = line.decode("utf-8")  # Decoding the binary data to text.
    if "EST" in line or "EDT" in line:  # look for Eastern Time
        print(line)


print(__name__)
