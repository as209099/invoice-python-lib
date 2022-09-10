# invoice-python-lib
中華民國財政部統一發票 - Python

## 簡介
本程式主要用於取得中華民國財政部統一發票號碼，並用於發票號碼兌獎。

## 安裝
### 本地端安裝
```
git clone git@github.com:as209099/invoice-python-lib.git
python3 -m setup.py install
```
### Pip PyPI安裝
```
pip install invoice
```

## 使用方法

```python
# 初始化時會自動下載當期與上期統一發票之資料
>>> from invoice import Invoice
>>> invoice = Invoice()
```

```python
# 取得當期民國年與月份
>>> invoice.get_years_and_months()
'111年05-06月'

# 取得當期的開獎發票號碼
>>> invoice.get_numbers()
[['特別獎', '46438476'],
['特獎', '54769852'],
['頭獎', '17858097'],
...]

# 也能取得上期的民國年與月份
>>> invoice.get_previous_years_and_months()
'111年03-04月'

# 以及上期的開獎發票號碼
>>> invoice.get_previous_numbers()
[['特別獎', '32220402'],
 ['特獎', '99194290'],
 ...,
 ['頭獎', '27854976']]
```

```python
# 兌獎
>>> invoice_list = invoice.get_numbers()
>>> my_numbers = [
    '12345678',
    '12345677',
    ...,
    '123'
]
>>> prize_list = invoice.redeem(invoice_list, my_numbers)
>>> print(prize_list)
[
    ['12345678', None],
    ['12345677', '六獎'],
    ...,
    ['123', '格式有誤']
]
```

## 使用之Library
- <a href="https://docs.aiohttp.org/en/stable/">aiohttp</a>
- <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">BeautifulSoup4</a>

enjoy coding!

## 授權
採用<a href="https://zh.m.wikipedia.org/zh-tw/MIT%E8%A8%B1%E5%8F%AF%E8%AD%89">MIT授權條款</a>，可以自行運用，也可以發起Issue或Pull Request給我。
