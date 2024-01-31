from selenium import webdriver
from bs4 import BeautifulSoup

import time

class ChromeDriver:
    def __init__(self) -> None:
        self.browser = webdriver.Chrome()

    def getUrl(self, Url: str) -> None:
        self.browser.get(url=Url)

    def getSourceAsFile(self, Path:str = "SiteSource.txt"):
        Source = self.browser.page_source
        with open(Path, "w") as f:
            f.write(str(Source.encode("utf-8")))

    def getSource(self):
        self.Source = self.browser.page_source

    def getCompanyName(self):
        Text = BeautifulSoup(self.Source, 'html.parser')
        print(Text.select("#content > div.site-wrapper > div > div > div.bsj-template__b > ul.jobs-list-items > li:nth-child(1) > div > div.bjs-jlid__header > div > h4 > a"))

    

# 객체생성
Chrome = ChromeDriver()

# 오픈
Chrome.getUrl("https://berlinstartupjobs.com/skill-areas/python/")

# 사이트 소스 가져오기
Chrome.getSource()

Chrome.getCompanyName()

time.sleep(10)