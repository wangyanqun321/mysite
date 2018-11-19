import requests
from retrying import retry

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}


@retry(stop_max_attempt_number=3)
def _parse_url(url, method, data, proxies):
    if method == "POST":
        response = requests.get(url, headers=headers, timeout=3, verify=False, proxies=proxies)
    else:
        response = requests.post(url, data=data, headers=headers, timeout=3, verify=False, proxies=proxies)
    assert response.status_code == 200
    return response.content.decode()


def parse_url(url, method="GET", data=None, proxies={}):
    try:
        str_html = _parse_url(url, method, data, proxies)
    except:
        str_html = None
    return str_html


if __name__ == "__main__":
    html_str = parse_url("http://www.baidu.com")
    print(html_str)
