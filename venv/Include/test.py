import requests

response = requests.get("https://www.baidu.com/img/bd_logo1.png")

r = response.content
with open("img/baidu.jpg", "wb") as f:
    f.write(r)
