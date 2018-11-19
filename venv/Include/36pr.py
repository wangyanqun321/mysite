import re
import requests
import json

url = "http://36kr.com/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
response = requests.get(url, headers)
html_str = response.content.decode()
ret = re.findall("<script>var props=(.*?),locationnal=", html_str)[0]
ret = json.loads(ret)
for k, v in ret.items():
    for i in v:
        print(k, v)
