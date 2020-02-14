import requests
from bs4 import BeautifulSoup


# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://finance.naver.com/',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')
indice = soup.select('#content > div.article > div.section2 > div.section_stock_market > div.section_stock')


#코스닥 #content > div.article > div.section2 > div.section_stock_market > div.section_stock > div.kospi_area.group_quot > div.heading_area > a > span > span.num
#코스피 #content > div.article > div.section2 > div.section_stock_market > div.section_stock > div.kosdaq_area.group_quot > div.heading_area > a > span > span.num


for index in indice :
    kospi1 = index.select_one('div.kospi_area.group_quot > div.heading_area > a > span > span.num')
    kospi2 = index.select_one('div.kospi_area.group_quot > div.heading_area > a > span > span.num2')
    kospi3 = index.select_one('div.kospi_area.group_quot > div.heading_area > a > span > span.num3')
    kospi4 = index.select_one('div.kospi_area.group_quot > div.heading_area > a > span > span.blind')

    kosdaq1 = index.select_one('div.kosdaq_area.group_quot > div.heading_area > a > span > span.num')
    kosdaq2 = index.select_one('div.kosdaq_area.group_quot > div.heading_area > a > span > span.num2')
    kosdaq3 = index.select_one('div.kosdaq_area.group_quot > div.heading_area > a > span > span.num3')
    kosdaq4 = index.select_one('div.kosdaq_area.group_quot > div.heading_area > a > span > span.blind')
    print(kospi1.text,' ', kospi2.text, kospi3.text, kospi4.text)
    print(kosdaq1.text, '   ',kosdaq2.text, kosdaq3.text, kosdaq4.text)