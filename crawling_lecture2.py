#%%

import requests
from bs4 import BeautifulSoup
import pandas as pd

page_list = []
for i in range(1, 4002, 10):
    page_list.append(str(i))

title_list = [] # 제목리스트
content_list = [] # 내용리스트

for page in page_list:
    raw = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query=딥러닝&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=34&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={page}")
    html = BeautifulSoup(raw.text, "html.parser")
    # ======================================================================================
    articles = html.select("ul.list_news > li") # 뉴스기사 요소 덩어리를 가져와줘야함. (li)
    for i in range(len(articles)):
        title = articles[i].select_one(".news_tit").text # list_news 안에 li 들이 여러개가 있는데 
                                                    # 그중 첫번째 li 안쪽에 a가 여러개 있는데, 원하는값은 news_tit 라는 클래스임
        content = articles[i].select_one(".dsc_txt_wrap").text
        title_list.append(title)
        content_list.append(content)

sdict = {'제목' : title_list, # 뉴스 제목 list를 제목의 컬럼에 값으로 넣기
         '내용' : content_list # 뉴스 내용 list를 내용 컬럼에 값으로 넣기
         }

df=pd.DataFrame(sdict)
df.to_csv('./naver_news_crawling_result.csv',index=False)
print(sdict)
# %%
print('a')