import requests
import pandas as pd
from io import StringIO

# 確保 lxml 和 BeautifulSoup4 安裝
try:
    import lxml
    import bs4
except ImportError:
    print("請執行 `pip install lxml beautifulsoup4` 安裝所需的依賴")

# 定義目標 URL
url = 'https://www.taifex.com.tw/cht/5/optIndxFSP'

# 發送 GET 請求
response = requests.get(url)
response.encoding = 'utf-8'  # 設定編碼

# 解析 HTML 表格
try:
    tables = pd.read_html(StringIO(response.text))  # 使用 StringIO 避免 FutureWarning
    df = tables[0]  # 取第一個表格
    print(df.head())
except Exception as e:
    print("讀取表格失敗，請檢查錯誤：", e)
