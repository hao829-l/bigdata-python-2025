import requests, pandas as pd, re, time
url = 'https://movie.douban.com/top250'
headers = {'User-Agent': 'Mozilla/5.0'}
titles = []
for start in range(0, 250, 25):
    params = {'start': start}
    html = requests.get(url, headers=headers, params=params).text
    titles += re.findall(r'<span class="title">([^&].*?)</span>', html)
    time.sleep(1)  # 礼貌爬取
pd.DataFrame({'电影名': titles}).to_excel('douban250.xlsx', index=False)
print('已保存 douban250.xlsx')