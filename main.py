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
    
    def getSource(self) -> str:
        return self.site.text

    def bs4Parser(self, text: str, select: str, parser: str  = "html.parser") -> str:
        # html 파싱초기화(?)
        ParseSource = BeautifulSoup(text, parser)

        # 그룹 나누기
        Group = ParseSource.select(select)

        # 특정클래스 값들 가져오기
        Result = ParseSource.find_all("h4", "bjs-jlid__h")

        # 리스트 초기화
        parsed_results = list()
        
        for result in Result:
            a_tag = result.find('a')
            if a_tag:
                href = a_tag['href']
                text = a_tag.text.strip()
                parsed_results.append({'href': href, 'text': text})

        # 리턴
        return parsed_results



def main() -> None:
    # 파싱시작
    Site = siteParse("https://berlinstartupjobs.com/skill-areas/javascript/")

    # 사이트 소스얻기
    SiteSource = Site.getSource()

    # 컨테인 
    Result = Site.bs4Parser(SiteSource, "#content > div.site-wrapper > div > div > div.bsj-template__b > ul.jobs-list-items")
    
    print(Result)



if (__name__ == "__main__"):
    main()