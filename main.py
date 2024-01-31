import requests
from bs4 import BeautifulSoup

class siteParse:
    def __init__(self, site: str) -> None:
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
        self.site = requests.get(site, headers=self.headers)
        if (self.site.status_code != 200):
            print(f"status_code error code: {self.site.status_code}")
        else:
            print(f"Successful code: {self.site.status_code}")
    
    def getCompanyName(self) -> list:
        SiteSource = self.site.text
        self.ParseSource = BeautifulSoup(SiteSource, "html.parser")
        print(self.ParseSource.select("#content > div.site-wrapper > div > div > div.bsj-template__b > ul.jobs-list-items > li:nth-child(1) > div > div.bjs-jlid__header > div > h4 > a"))


Site = siteParse("https://berlinstartupjobs.com/engineering/")
Site.getCompanyName()