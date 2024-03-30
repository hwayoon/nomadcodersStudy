from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
options=Options()
browser=webdriver.Chrome(options=options)


def get_page_count(keyword):
    base_url="https://kr.indeed.com/jobs?q="
    browser.get(f"{base_url}{keyword}")
    soup=BeautifulSoup(browser.page_source, "html.parser")
    pagination=soup.find("ul", class_="css-1g90gv6 eu4oa1w0")
    if pagination==None:
        return 1
    pages=pagination.find_all("li", recursive=False)
    count=len(pages)
    if count >=5:
        return 5
    elif count==0:
        return count+1
    else: 
        return count



def extract_indeed_jobs(keyword):
    pages=get_page_count(keyword)
    print("Found", pages, "pages")
    results=[]
    for page in range(pages):
        base_url="https://kr.indeed.com/jobs"
        final_url=f"{base_url}?q={keyword}&start={page*10}"
        print("Requesting", final_url)
        browser.get(final_url)
        soup=BeautifulSoup(browser.page_source, "html.parser")
        job_list=soup.find("ul",class_="css-zu9cdh")
        jobs=job_list.find_all('li',recursive=False)
        for job in jobs:
            zone=job.find("div", class_="mosaic-zone")
            if zone==None:
                anchor = job.select_one("h2 a", class_="jcs-JobTitle")
                title = job.select_one("h2 a span")
                link= anchor['href'] #here get some problems
                company=job.select_one("span", attrs={"data-testid":"company-name"})
                location=job.select_one("div", attrs={"data-testid":"text-location"})
                job_data={
                    'link':f"https://kr.indeed.com{link}",
                    'company':company.string,
                    'location':location.string,
                    'position':title.string
                }
                results.append(job_data)
    return results