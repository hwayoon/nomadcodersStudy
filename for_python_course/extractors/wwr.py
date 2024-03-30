from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
    base_url="https://weworkremotely.com/remote-jobs/search?term="
    response=get(f"{base_url}{keyword}")
    if response.status_code !=200:
        print("Can't request website")
    else:
        results=[]
        soup=BeautifulSoup(response.text, "html.parser")
        jobs=soup.find_all('section', class_="jobs")
        for job_section in jobs:
            job_posts=job_section.find_all('li')
            job_posts.pop(-1)
            for post in job_posts:
                anchors = post.find_all('a') #.find_all 항목당 모든대상 찾을 때
                anchor=anchors[1] #[1]; 두번째 anchor만 꺼낸다는 뜻?
                link = anchor['href']
                company, kind, region = anchor.find_all('span', class_="company")
                title=anchor.find('span', class_='title') #.find 항목당 가장 첫번째 것만 찾을때
                job_data={
                    'link': f"https://weworkremotely.com/{link}", 
                    'company':company.string.replace(",", " "), 
                    #.string: html 태그를 제거하고 사이의 text만 추출.
                    'location':region.string.replace(",", " "),
                    'position':title.string.replace(",", " ")
                    #문자열.strip(): 문자열 좌우 공백을 제거
                }
                results.append(job_data)
        return results