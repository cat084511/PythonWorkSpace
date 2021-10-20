import requests
r = requests.session()
url = "https://www.amazon.co.jp/%E6%A9%8B%E6%9C%AC-%E7%A5%90%E5%8F%B2/e/B01GR7RR3C/ref=dp_byline_cont_pop_book_1"
res = r.get(url=url)
print(res.text)