import requests

session = requests.session()
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
response = session.get(url, headers=headers)
