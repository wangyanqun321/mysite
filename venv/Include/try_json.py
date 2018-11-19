import json
import requests
url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start={}"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
for i in range(20):
    response = requests.get(url.format(i), headers=headers)
    html_str = response.content.decode()
    ret = json.loads(html_str)
    # with open("douban.json", "w", encoding="utf-8") as f:
    #     f.write(json.dumps(ret, ensure_ascii=False, indent=4))
    for i in ret["subjects"]:
        print(i)
